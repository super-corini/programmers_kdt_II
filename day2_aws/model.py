import torch
import itertools
from utils import clean_text


class ModelHandler:
    def __init__(self):
        self.id2label = {0: 'negative', 1: 'positive'}

    def _clean_text(self, text):
        model_input = []
        if isinstance(text, str):
            cleaned_text = clean_text(text)
            model_input.append(cleaned_text)
        elif isinstance(text, (list, tuple)) and len(text) > 0 and (all(isinstance(t, str) for t in text)):
            cleaned_text = itertools.chain((clean_text(t) for t in text))
            model_input.extend(cleaned_text)
        else:
            model_input.append('')
        return model_input


class MLModelHandler(ModelHandler):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self, ):
        # De-serializing model and loading vectorizer
        import joblib
        self.model = joblib.load('model/ml_model.pkl') #
        self.vectorizer = joblib.load('model/ml_vectorizer.pkl')

    def preprocess(self, text):
        # cleansing raw text
        model_input = self._clean_text(text) # 텍스트데이터를 클린징

        # vectorizing cleaned text
        model_input = self.vectorizer.transform(model_input) # 벡터 형태로 변환
        return model_input

    def inference(self, model_output):
        # get predictions from model as probabilities
        model_output = self.model.predict_proba(model_output) # 예측
        return model_output

    def postprocess(self, model_output):
        # process predictions to predicted label and output format
        predicted_probabilities = model_output.max(axis=1) # 결과중 가장 높은 확률값을 뽑기
        predicted_ids = model_output.argmax(axis=1) # 뽑아온 확률값이 어떤 id값인지(어떤 레이블인지) 뽑아온다.
        predicted_labels = [self.id2label[id_] for id_ in predicted_ids] # 뽑은 id값이 id2label api에 의해 사람이 이해할 수 있는 형태로 변환
        return predicted_labels, predicted_probabilities # 결과: 각 텍스트에대한 분석결과, 결과에 대한 확률값

    def handle(self, data):
        # do above processes
        model_input = self.preprocess(data) # 입력이 들어왔을 때 전처리 해주기
        model_output = self.inference(model_input) # 모델이 들어왔을 때 inference를 통해 output을 내고
        return self.postprocess(model_output) #최종적으로 후처리를 통해 결과를 반환한다.


class DLModelHandler(ModelHandler):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self, ):
        #de-serializing model and loading vectorizer
        from transformers import AutoTokenizer, AutoModelForSequenceClassification # 추상화된 형태로 제공하기 때문에 개발에 편하고 속도도 빠르다
        self.model_name_or_path = 'sackoh/bert-base-multilingual-cased-nsmc' 
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path) # 해당 경로에 있는 저장된 파일을 바탕으로 tokenizer와 model을 불러온다.
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name_or_path)
        self.model.to('cpu') # cpu에서 돌아가도록 설정

    def preprocess(self, text):
        # preprocess raw text
        model_input = self._clean_text(text) # 텍스트데이터를 클린징 - 전처리

        # vectorize cleaned text
        model_input = self.tokenizer(text, return_tensors='pt', padding=True) # pytorch의 tensor형태로 반환
        return model_input

    def inference(self, model_input):
        with torch.no_grad():
            model_output = self.model(**model_input)[0].cpu() 
            model_output = 1.0 / (1.0 + torch.exp(-model_output))
            model_output = model_output.numpy().astype('float')
        return model_output

    def postprocess(self, model_output):
        # process predictions to predicted label and output format
        predicted_probabilities = model_output.max(axis=1) # 결과중 가장 높은 확률값을 뽑기
        predicted_ids = model_output.argmax(axis=1) # 뽑아온 확률값이 어떤 id값인지(어떤 레이블인지) 뽑아온다.
        predicted_labels = [self.id2label[id_] for id_ in predicted_ids] # 뽑은 id값이 id2label api에 의해 사람이 이해할 수 있는 형태로 변환
        return predicted_labels, predicted_probabilities # 결과: 각 텍스트에대한 분석결과, 결과에 대한 확률값

    def handle(self, data):
        model_input = self.preprocess(data)
        model_output = self.inference(model_input)
        return self.postprocess(model_output)


import itertools
from utils import clean_text
import torch

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

# 데이터 처리나 모델, config 등 초기화
    def initialize(self, ):
        import joblib
        self.model = joblib.load('./model/ml_model.pkl')
        self.vectorizer = joblib.load('./model/ml_vectorizer.pkl')

# 입력을 전처리 및 모델 입력 가능 형태로 변환
    def preprocess(self, text):
        model_input = self._clean_text(text)
        model_input = self.vectorizer.transform(model_input)
        return model_input

# 입력된 값 예측 및 추론
    def inference(self, model_input):
        model_output = self.model.predict_proba(model_input)
        return model_output

# 모델의 예측값 후처리
    def postprocess(self, model_output):
        predicted_probabilities = model_output.max(axis=1)
        predicted_ids = model_output.argmax(axis=1)
        predicted_labels = [self.id2label[id_] for id_ in predicted_ids]
        return predicted_labels, predicted_probabilities

# 요청한 정보를 받아 적절한 응답 반환
    def handle(self, data):
        model_input = self.preprocess(data)
        model_output = self.inference(model_input)
        return self.postprocess(model_output)

class DLModelHandler(ModelHandler):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self, ):
        from transformers import AutoTokenizer, AutoModelForSequenceClassification
        self.model_name_or_path = 'sackoh/bert-base-multilingual-cased-nsmc'
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name_or_path)
        self.model.to('cpu')

    def preprocess(self, text):
        model_input = self._clean_text(text)
        model_input = self.tokenizer(text, return_tensors='pt', padding=True)
        return model_input

    def inference(self, model_input):
        with torch.no_grad():
            model_output = self.model(**model_input)[0].cpu()
            model_output = 1.0 / (1.0 + torch.exp(-model_output))
            model_output = model_output.numpy().astype(float)
        return model_output

    def postprocess(self, model_output):
        predicted_probabilities = model_output.max(axis=1)
        predicted_ids = model_output.argmax(axis=1)
        predicted_labels = [self.id2label[id_] for id_ in predicted_ids]
        return predicted_labels, predicted_probabilities

    def handle(self, data):
        model_input = self.preprocess(data)
        model_output = self.inference(model_input)
        return self.postprocess(model_output)

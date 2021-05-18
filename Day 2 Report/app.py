from flask import Flask, request, json
from model import MLModelHandler, DLModelHandler
from time import time
from train_ml import *

app = Flask(__name__)

# assign model handler as global variable [2 LINES]

@app.route("/predict", methods=["POST"])
def predict():
	# handle request and body
    body = request.get_json()
    text = body.get('text', '')
    text = [text] if isinstance(text, str) else text
    do_fast = body.get('do_fast', True)
    
	# model inference
    if do_fast:
    	predictions = ml_handler.handle(text)
    else:
    	predictions = dl_handler.handle(text)
    # predictions => (['positive', 'negative'], array([0.98683823, 0.79660478]))
    
	#response
    result = json.dumps({str(i): {'text' : t, 'label' : l, 'confidence' : c}
    					for i, (t, l, c) in enumerate(zip(text, predictions[0], predictions[1]))})
    return result

@app.route("/train")
def train():
    start_time = time.now()
    for mode in ['train', 'test']:
        download_data(mode)

    model, vectorizer = train_and_evaluate()
    serialization(model, vectorizer)
    response = time.now() - start_time

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)

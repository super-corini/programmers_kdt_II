from flask import Flask, request, json
from model import MLModelHandler, DLModelHandler
from train_ml import train_new_model

app = Flask(__name__)


ml_handler = MLModelHandler()
dl_handler = DLModelHandler()


@app.route("/train", methods=["GET"])
def train():
    elapsed_time = train_new_model()
    return {"Elapsed time" : str(elapsed_time)}


@app.route("/predict", methods=["POST"])
def predict():
    # handle request and body
    body = request.get_json()
    text = body.get('text', '')
    text = [text] if isinstance(text, str) else text
    do_fast = body.get('do_fast', True)

    # model inference [2 LINES]
    if do_fast:
        predictions = ml_handler.handle(text)
    else:
        predictions = dl_handler.handle(text)

    # response
    result = json.dumps({str(i): {'text': t, 'label': l, 'confidence': c}
                         for i, (t, l, c) in enumerate(zip(text, predictions[0], predictions[1]))})
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
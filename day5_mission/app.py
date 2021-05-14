from flask import Flask, json, jsonify, request

app = Flask(__name__)

@app.route('/whoami')
def whoami():
    return jsonify({"name": "Han-D-Peter"})

@app.route('/echo')
def echo_parameter():
    param = request.args.to_dict()['string']
    param = str(param)
    return jsonify({"value": param})
    

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify, request
import json
import os
from error_handling.error import error_handler
from preprocessing.cleaning_data import preprocess
from predict.prediction import prediction

app = Flask(__name__)


@app.route('/', methods=['GET'])
def start():
    return "The server is alive"


@app.route('/predict', methods=['GET', 'POST'])
def price_predict():
    if request.method == 'GET':

        with open("preprocessing/template.json") as file:
            output_template = json.load(file)

        # Beautify output using Flask templates
        return jsonify(output_template), 200

    if request.method == 'POST':

        if not request.content_type == 'application/json' or not isinstance(
                request.get_json(),
                dict) or not request.get_json().get('data'):
            return 'Refer input format available at: http://immo-price-predictor.herokuapp.com/predict', 400

        json_data = request.get_json().get('data')

        # Test if input provided is as requested. If not, send error message
        error_check = error_handler(json_data)

        if error_check == "No errors":
            # If input provided as expected, pass it through for pre-processing
            prepped_df = preprocess(json_data)

            # Use pre-processed data as an input for model and return the output in JSON
            price = prediction(prepped_df)
            return jsonify({"prediction": price, "error": None}), 200
        else:
            return jsonify({"errors": error_check, "prediction": None}), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)
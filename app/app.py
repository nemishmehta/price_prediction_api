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
        output_template = {
            "data": {
                "building-state": [
                    "As new", "Just renovated", "Good", "To be done up",
                    "To renovate", "To restore"
                ],
                "equipped-kitchen": [
                    "USA uninstalled", "Not installed", "Installed",
                    "USA installed", "Semi equipped", "USA semi equipped",
                    "Hyper equipped", "USA hyper equipped"
                ],
                "furnished":
                "[bool]",
                "facades-number":
                "[int]",
                "land-area":
                "[float]",
                "area":
                "[float]",
                "property-type": ["APARTMENT", "HOUSE"],
                "property-sub-type": [
                    "BUNGALOW", "CASTLE", "CHALET", "COUNTRY_COTTAGE",
                    "DUPLEX", "EXCEPTIONAL_PROPERTY", "FARMHOUSE",
                    "FLAT_STUDIO", "GROUND_FLOOR", "KOT", "LOFT",
                    "MANOR_HOUSE", "MANSION", "MIXED_USE_BUILDING",
                    "PENTHOUSE", "SERVICE_FLAT", "TOWN_HOUSE", "TRIPLEX",
                    "VILLA"
                ],
                "city":
                "Enter a city in Flanders or Brussels",
                "terrace":
                "[bool]",
                "garden":
                "[bool]"
            }
        }

        # Beautify output using Flask templates
        return jsonify(output_template)

    if request.method == 'POST':
        json = request.get_json(
        )  # This will result in a 400 error when input data is not in JSON format

        # Test if input provided is as requested. If not, send error message
        error_check = error_handler(json)

        if error_check == "No errors":
            # If input provided as expected, pass it through for pre-processing
            prepped_df = preprocess(json)

            # Use pre-processed data as an input for model and return the output in JSON
            price = prediction(prepped_df)
            return jsonify({"prediction": price, "error": None})
        else:
            return jsonify({"errors": error_check, "prediction": None})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)
    #app.run()
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def start():
    return "The server is alive"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        output_template = """
        {
            "data": {
                "Building condition": "As new" | "Just renovated" | "Good" | "To be done up" | "To renovate" | "To restore",
                "Kitchen type": "USA uninstalled" | "Not installed" | "Installed" | "USA installed" | "Semi equipped" | "USA semi equipped" | "Hyper equipped" | "USA hyper equipped",
                "Furnished": bool,
                "Number of frontages": int,
                "Surface of the plot": float
                "Living area": float,
                "Property type": "APARTMENT" | "HOUSE",
                "Property sub-type": "BUNGALOW" | "CASTLE" | "CHALET" | "COUNTRY_COTTAGE" | "DUPLEX" | "EXCEPTIONAL_PROPERTY" | "FARMHOUSE" | "FLAT_STUDIO" | "GROUND_FLOOR" | "KOT" | "LOFT" | "MANOR_HOUSE" | "MANSION" | "MIXED_USE_BUILDING" | "PENTHOUSE" | "SERVICE_FLAT" | "TOWN_HOUSE" | "TRIPLEX" | "VILLA"
                "City": str,
                "Terrace": bool,
                "Garden": bool
            }
        }"""
        # Beautify output using Flask templates
        return f'The POST method requires a JSON input in the following format: \n {output_template}'

    if request.method == 'POST':
        json = request.get_json()

        # Test if input provided is as requested. If not, send error message

        # If input provided as expected, pass it through for pre-processing
        preprocess(json)

        # Use pre-processed data as an input for model and return the output in JSON
        predict()


if __name__ == '__main__':
    app.run()
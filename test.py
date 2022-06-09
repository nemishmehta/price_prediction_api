import json
import unittest
import requests
from flask import jsonify

class FlaskTest(unittest.TestCase):
    
    base_url = "http://127.0.0.1:5000/"
    price_predict_url = f"{base_url}predict"

    # Check for response 200
    def test_base_url(self):
        r = requests.get(self.base_url)

        self.assertEqual(r.status_code, 200)

    """
    def test_predict_url(self):
        r = requests.get(self.price_predict_url)

        self.assertEqual(r.status_code, 200)
        
        with open("preprocessing/template.json") as file:
            output_template = json.load(file)

        self.assertEqual(r.json(), jsonify(output_template))
    """

if __name__ == "__main__":
    unittest.main()
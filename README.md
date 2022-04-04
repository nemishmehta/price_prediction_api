# Price Prediction API

The goal of this repository is to provide web developers with price prediction of properties in Belgium based on the property's features (area, building-state, city, etc.). The Price Prediction API is organized around REST principles. Our API has a resource-oriented URL, accepts JSON requests and returns JSON-encoded responses, and uses standard HTTP response codes.

### Base URL
http://immo-price-predictor.herokuapp.com/

### Price Prediction
http://immo-price-predictor.herokuapp.com/predict

#### Methods
1. GET - Returns a dictionary containing all required parameters and their formats to predict a property's price.

2. POST - Accepts a JSON request that should contains the required parameters and returns a JSON response containing the predicted price.

### Success and Errors
1. 200 - OK : Everything worked as expected.

2. 400 - Bad Request : The request was unacceptable. Depending on the cause of the error, the response will either return the price prediction URL or identify the missing parameters or formats.


## Cloning Repository 

### Installation
The project has been coded in Python 3.8.10 and requires the following packages and libraries:

1. [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask)
2. [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
3. [Pydantic](https://pydantic-docs.helpmanual.io/install/)
4. [Scikit-learn](https://scikit-learn.org/stable/install.html)
5. [Docker](https://docs.docker.com/engine/install/ubuntu/) --> if you want to wrap the app in a container.
6. Heroku - `sudo snap install --classic heroku`

Note: It is recommended to use virtual environment while installing the above packages and libraries.

### Usage
1. To deploy the program on a local machine, navigate to the root directory of the project and run `python3 app.py` on the terminal.
2. This will launch the app on a browser window where you can check the response for GET requests to the base URL (/) and the Price prediction (/predict).
3. Use a service like Postman to send a POST request with the required parameters to receive the price prediction.
4. To update/modify the data preprocessing elements, navigate to `preprocessing>cleaning_data.py`.
5. To update/modify the regression model, navigate to `model>model.py`.
6. To update/modify the error handling, navigate to `error_handling>error.py`.
7. To wrap app in a container, run `docker build . -t image-name` in the `/app` directory.
8. To deploy the container, run `docker run -t image-name`.
9. To deploy container on Heroku, refer [official documentation](https://devcenter.heroku.com/articles/container-registry-and-runtime).

### Contributors
1. Nemish Mehta
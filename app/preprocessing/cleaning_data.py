import pandas as pd
import pickle


def preprocess(data):
    """
    Clean data to be suitable for model requirements
    """
    # Change input data keys in the format available in dataframe
    keys = {
        "building-state": "Building condition",
        "equipped-kitchen": "Kitchen type",
        "furnished": "Furnished",
        "facades-number": "Number of frontages",
        "land-area": "Surface of the plot",
        "area": "Living area",
        "property-type": "Property type",
        "property-sub-type": "Property sub-type",
        "city": "City",
        "terrace": "Terrace",
        "garden": "Garden"
    }
    new_dict = {keys[key]: value for key, value in data['data'].items()}
    data['data'] = new_dict

    # Transform building condition to ordinal values
    build_cond_map = {
        'As new': 6,
        'Just renovated': 5,
        'Good': 4,
        'To be done up': 3,
        'To renovate': 2,
        'To restore': 1
    }
    for cond, val in build_cond_map.items():
        if data["data"]["Building condition"] == cond:
            data["data"]["Building condition"] = val

    # Transform Kitchen type to ordinal values
    kit_type_map = {
        "USA uninstalled": 0,
        "Not installed": 0,
        "Installed": 1,
        "USA installed": 1,
        "Semi equipped": 1,
        "USA semi equipped": 1,
        "Hyper equipped": 2,
        "USA hyper equipped": 2
    }
    for cond, val in kit_type_map.items():
        if data["data"]["Kitchen type"] == cond:
            data["data"]["Kitchen type"] = val

    # Convert Furnished to binary
    data["data"]["Furnished"] = convert_to_binary(data, "Furnished")

    # Convert Terrace to binary
    data["data"]["Terrace"] = convert_to_binary(data, "Terrace")

    # Convert Garden to binary
    data["data"]["Garden"] = convert_to_binary(data, "Garden")

    # Convert data to a dataframe to one hot encode variables
    # Add columns present in model columns but not data dataframe
    df = pd.DataFrame(data['data'], index=[0])

    # One Hot Encoding of categorial variables like property type, property sub-type, City
    df = pd.get_dummies(df)

    model_columns = pickle.load(open('model/model_columns.pkl', 'rb'))

    df = df.reindex(columns=model_columns, fill_value=0)

    return df


def convert_to_binary(data, category):
    if data["data"][category]:
        return 1
    else:
        return 0
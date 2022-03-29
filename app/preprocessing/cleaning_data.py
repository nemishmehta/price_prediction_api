import pandas as pd


def preprocess(data):
    """
    Clean data to be suitable for model requirements
    """

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
    if data["data"]["Furnished"]:
        data["data"]["Furnished"] = 1
    else:
        data["data"]["Furnished"] = 0

    # Convert data to a dataframe to one hot encode variables
    # Add columns present in model columns but not data dataframe
    df = pd.DataFrame(data, index=[0])

    # Property type

    # Property sub-type

    # City


"""
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
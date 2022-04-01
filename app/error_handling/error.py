from pydantic import BaseModel, Field, PositiveInt, ValidationError, validator
from typing import Literal


def error_handler(json_data):
    """
    Function to handle errors in user-provided input
    """

    # Check if input is a valid JSON
    # try:
    #     input_data = json.loads(json_data)
    # except ValueError:
    #     return {"error": "The input data is not in a valid JSON format"}

    # Check if input data is in the required format
    class Error(BaseModel):
        building_state: Literal["As new", "Just renovated", "Good",
                                "To be done up", "To renovate",
                                "To restore"] = Field(...,
                                                      alias="building-state")
        equipped_kitchen: Literal["USA uninstalled", "Not installed",
                                  "Installed", "USA installed",
                                  "Semi equipped", "USA semi equipped",
                                  "Hyper equipped",
                                  "USA hyper equipped"] = Field(
                                      ..., alias="equipped-kitchen")
        furnished: bool
        facades_number: int = Field(..., alias="facades-number")
        land_area: PositiveInt = Field(..., alias="land-area")
        area: PositiveInt
        property_type: Literal["APARTMENT",
                               "HOUSE"] = Field(..., alias="property-type")
        property_sub_type: Literal["BUNGALOW", "CASTLE", "CHALET",
                                   "COUNTRY_COTTAGE", "DUPLEX",
                                   "EXCEPTIONAL_PROPERTY", "FARMHOUSE",
                                   "FLAT_STUDIO", "GROUND_FLOOR", "KOT",
                                   "LOFT", "MANOR_HOUSE", "MANSION",
                                   "MIXED_USE_BUILDING", "PENTHOUSE",
                                   "SERVICE_FLAT", "TOWN_HOUSE", "TRIPLEX",
                                   "VILLA"] = Field(...,
                                                    alias="property-sub-type")
        city: str
        terrace: bool
        garden: bool

        @validator('facades_number', allow_reuse=True)
        def facades(cls, v):
            if v <= 0 or v > 4:
                raise ValueError(
                    'unexpected value; permitted: between 1 and 4')

        @validator('city', allow_reuse=True)
        def city_select(cls, v):
            city_options = [
                'Aalst', 'Antwerpen', 'Arlon',
                'Arrondissement Brussel-Hoofdstad', 'Ath', 'Bastogne',
                'Brugge', 'Charleroi', 'Dendermonde', 'Diksmuide', 'Dinant',
                'Eeklo', 'Gent', 'Halle-Vilvoorde', 'Hasselt', 'Huy', 'Ieper',
                'Kortrijk', 'Leuven', 'Liège', 'Maaseik', 'Marche-en-Famenne',
                'Mechelen', 'Mons', 'Mouscron', 'Namur', 'Neufchâteau',
                'Nivelles', 'Oostende', 'Oudenaarde', 'Philippeville',
                'Roeselare', 'Sint-Niklaas', 'Soignies', 'Thuin', 'Tielt',
                'Tongeren', 'Tournai', 'Turnhout', 'Verviers', 'Veurne',
                'Virton', 'Waremme'
            ]
            if v not in city_options:
                raise ValueError(
                    f'unexpected value; permitted: {city_options}')
            return v

    try:
        Error(**json_data)
        return "No errors"
    except ValidationError as e:
        capture_error = {}
        for item in e.errors():
            capture_error[item["loc"][0]] = item["msg"]

        return capture_error
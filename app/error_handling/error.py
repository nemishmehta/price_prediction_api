import json
from pydantic import BaseModel, ValidationError, validator


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
        building_state: str
        equipped_kitchen: str
        furnished: bool
        facades_number: int
        land_area: float
        area: float
        property_type: str
        property_sub_type: str
        city: str
        terrace: bool
        garden: bool

        @validator('building_state')
        def build_state(cls, v):
            build_options = [
                "As new", "Just renovated", "Good", "To be done up",
                "To renovate", "To restore"
            ]
            if v not in build_options:
                raise ValueError(
                    f'Choose one of these options for building_state: {build_options}'
                )
            return v

        @validator('equipped_kitchen')
        def kitchen(cls, v):
            kitchen_options = [
                "USA uninstalled", "Not installed", "Installed",
                "USA installed", "Semi equipped", "USA semi equipped",
                "Hyper equipped", "USA hyper equipped"
            ]
            if v not in kitchen_options:
                raise ValueError(
                    f'Choose one of these options for equipped_kitchen: {kitchen_options}'
                )
            return v

        @validator('facades_number')
        def facades(cls, v):
            if v <= 0 or v > 4:
                raise ValueError('Please choose between 1 and 4 facades.')

        @validator('land_area')
        def plot_area(cls, v):
            if v <= 0:
                raise ValueError('Please choose a plot area greater than 0.')
            return v

        @validator('area')
        def living_area(cls, v):
            if v <= 0:
                raise ValueError('Please choose a living area greater than 0.')
            return v

        @validator('property_type')
        def prop_type(cls, v):
            prop_options = ["APARTMENT", "HOUSE"]
            if v not in prop_options:
                raise ValueError(
                    f'Choose one of these options for property_type: {prop_options}.'
                )
            return v

        @validator('property_sub_type')
        def prop_sub_type(cls, v):
            prop_sub_options = [
                "BUNGALOW", "CASTLE", "CHALET", "COUNTRY_COTTAGE", "DUPLEX",
                "EXCEPTIONAL_PROPERTY", "FARMHOUSE", "FLAT_STUDIO",
                "GROUND_FLOOR", "KOT", "LOFT", "MANOR_HOUSE", "MANSION",
                "MIXED_USE_BUILDING", "PENTHOUSE", "SERVICE_FLAT",
                "TOWN_HOUSE", "TRIPLEX", "VILLA"
            ]
            if v not in prop_sub_options:
                raise ValueError(
                    f'Choose one of these options for property_type: {prop_sub_options}.'
                )
            return v

        @validator('city')
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
                    f'Choose one of these options for city: {city_options}.')
            return v

    try:
        Error(**json_data['data'])
        return "No errors"
    except ValidationError as e:
        return e
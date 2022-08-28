import pickle
import json
from pathlib import Path
import os
import numpy as np

# Parent directory of util.py file
CURRENT_DIR = Path(__file__).resolve().parent

# Global variables
__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    """Return price for given feature"""

    try:
        # Find index for specific location
        loc_index = __data_columns.index(location).lower()
    except:
        # If given location doesn't found in the list
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    # predict(): Takes an input X, and for that given input it returns the output.
    # In our example, it will return estimated price.
    return round(__model.predict([x])[0], 2)


def get_location_names():
    """Returns location names"""

    return __locations


def load_saved_artifacts():
    """Load the columns and model artifacts when app is loaded"""

    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # If __data_columns, __locations, and __model is not set, load them and set till the app is running
    if not __data_columns or not __locations or not __model:
        # Load columns from the columns.json and returns all the columns starting from index 3,
        # as first three columns are not locations columns
        with open(os.path.join(CURRENT_DIR, "artifacts/columns.json"), "r") as f:
            __data_columns = json.load(f)["data_columns"]
            __locations = __data_columns[3:]

        # Load the model we got from the data cleaning
        with open(
            os.path.join(CURRENT_DIR, "artifacts/banglore_home_prices_model.pickle"),
            "rb",
        ) as f:
            __model = pickle.load(f)

        # Artifacts loaded successfully!
        print("Including saved artifacts...done!")


load_saved_artifacts()

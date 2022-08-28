from flask import Flask, request, jsonify, render_template
from . import util

# Initialized an flask app
app = Flask(__name__)


@app.route("/")
def index():
    """Index Page"""

    # Returns an UI to predict the house prices
    return render_template("app.html")


@app.route("/get_location_names")
def get_location_names():
    """The function returns the all locations names of banglore"""

    # Converts the locations dict to json format
    response = jsonify({"locations": util.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    """The function which returns the predicted estimated price for the given house based on house specifications"""

    # Get posted data from the request
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = request.form["bhk"]
    bath = request.form["bath"]

    # Predict the house price using linear regression classifier
    response = jsonify(
        {"estimated_price": util.get_estimated_price(location, total_sqft, bhk, bath)}
    )
    return response


if __name__ == "__main__":
    app.run()

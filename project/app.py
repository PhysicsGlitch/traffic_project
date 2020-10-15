from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import json


# Create an instance of Flask
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/accident_app"
mongo = PyMongo(app)
accidents = mongo.db.accident_data


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # I created an index for me mongodb beecause it was an easy collection method and also made it easy to reference
    # it in the html file  

    with open("static/data/fatalities.json") as d:
        fatalities = json.load(d)
    with open("static/data/hit_n_run_2020.json") as d:
        hit_n_run_2020 = json.load(d)
    with open("static/data/hit_n_run_2019.json") as d:
        hit_n_run_2019 = json.load(d)
    chicago_accidents = mongo.db.collection.find_one()
    mongo.db.collection.update({}, fatalities, upsert=True)
    mongo.db.collection.insert_one(hit_n_run_2020)
    mongo.db.collection.insert_one(hit_n_run_2019)
    # Return template and data
    return render_template("index.html", chicago_accidents=chicago_accidents)

# Route that will trigger the scrape function

# One function per button to update the data in our data frame

@app.route("/update")
def updater():
    traffic_data = traffic_data.update_data()
    mongo.db.collection.update({}, traffic_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
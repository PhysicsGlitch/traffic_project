import pandas as pd
from flask import Flask

# create instance of Flask app
app = Flask(__name__)

@app.route("/")
def basic_data():

    accident_data = {}
    pd.read_json("/static/data/fatalities.json")

    accident_data.update
    
    
    return accident_data
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
@app.route("/update")
def export():
   
    accident_data = {}
    pd.read_json("fatalities.json")

    accident_data.update
    
    
    return accident_data
    
if __name__ == "__main__":
    app.run(debug=True)
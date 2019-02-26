from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#from scrape_mars import scrape
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    final_output = mongo.db.mars_list.find_one()
    return render_template("index.html", final_output=final_output)


@app.route("/scrape")
def scraper():
    mars_db = mongo.db.mars_list
    mars_dict = scrape_mars.scrape()
    mars_db.update({}, mars_dict, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

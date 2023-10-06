from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["MONGO_URI"] = "mongodb://localhost:27017/HackZ"
mongo = PyMongo(app)
db = mongo.db


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/attend/<search>", methods=["POST", "GET"])
@app.route("/attend")
def attend(search=None):
    name = db.hackathons.find({})
    if request.method == 'POST':
        search = request.form.get("search")
    if not search:
        return render_template("attend.html", name=name, search=search)
    for hack in name:
        if search == hack["title"]:
            return render_template("attend.html", name=[hack], search=search)
    return render_template("attend.html", name=None)


if __name__ == "__main__":
    app.run(debug=True)

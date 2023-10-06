from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import os
from werkzeug.utils import secure_filename
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


@app.route("/host")
def host():
    return render_template("host.html")


@app.route("/description")
def description():
    return render_template("description.html")


@app.route("/submission", methods=["POST"])
def submission():
    image = request.files["field7"]
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    db.hackathons.insert_one({"name": request.form.get("field1"), "email": request.form.get("field2"), "phone": request.form.get("field3"), "website": request.form.get(
        "field4"), "location": request.form.get("field5"), "title": request.form.get("field6"), "image": filename, "description": request.form.get("field8")})
    return "Submitted Successfully!!"


if __name__ == "__main__":
    app.run(debug=True)

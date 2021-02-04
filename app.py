import os
from flask import (
    Flask, flash, render_template,
    request, redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# app.config["MONG_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_URI"] = "mongodb+srv://root:TheMentalist@myFristcluster.olwxq.mongodb.net/task_manager?retryWrites=true&w=majority"
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = mongo.db.tasks.find()
    return render_template("get_tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

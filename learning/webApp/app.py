from flask import Flask, request, render_template

import datetime

# datetime.datetime.now().ctime()

app = Flask(__name__)


@app.route("/")  # register that with the web server.
def index():
    return datetime.datetime.now().ctime()  # the http resonse


def hello():
    return "yolo swagger"


@app.get("/showform")
def display_form():
    return render_template("cv.html", the_title="My CV")


@app.get("/games")
def games():
    return render_template("games.html", the_title="My favourite games")

@app.get("/pd")
def personaldetails():
    return render_template("pd.html", the_title="My personal details")

@app.get("/destiny")
def destiny():
    return render_template("destiny.html", the_title="Destiny")

@app.get("/interests")
def interests():
    return render_template("interests.html", the_title="My interests")


@app.get("/godOfWar")
def godOfWar():
    return render_template("godOfWar.html", the_title="God OF War")


@app.get("/lastOfUs")
def lastOfUs():
    return render_template("lastOfUs.html", the_title="The Last Of Us")


@app.route("/home")
def home():
    return render_template("home.html", the_title="welcome")


@app.post("/processform")
def process_form():
    the_name = request.form["theName"]
    the_dob = request.form["thedob"]
    return f"HI There,{the_name}, we know you were born on the {the_dob} "


if __name__ == "__main__":
    app.run(debug=True)

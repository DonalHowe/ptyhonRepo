from flask import Flask, request,render_template

import datetime

#datetime.datetime.now().ctime() 

app = Flask(__name__)

@app.route("/") #register that with the web server.
def index():
    return datetime.datetime.now().ctime() #the http resonse

def hello():
    return "yolo swagger"

@app.get("/showform")
def display_form():
    return render_template("form.html",the_title="give us your details")



@app.route("/home")
def home():
    return render_template("home.html",the_title="welcome")


@app.post("/processform")
def process_form():
    the_name=request.form["theName"]
    the_dob=request.form["thedob"]
    return f"HI There,{the_name}, we know you were born on the {the_dob} "   


if __name__ == "__main__":
    app.run(debug=True)
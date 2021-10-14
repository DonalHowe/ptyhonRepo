from flask import Flask

import datetime

#datetime.datetime.now().ctime() 

app = Flask(__name__)

@app.route("/") #register that with the web server.
def index():
    return datetime.datetime.now().ctime() #the http resonse

def hello():
    return "yolo swagger"

if __name__ == "__main__":
    app.run()
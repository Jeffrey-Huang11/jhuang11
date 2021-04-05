# Team Jam Juice (Jonathan Lee, Jeffrey Huang)
# SoftDev
# K19 - - A RESTful Journey Skyward
# 2021-04-05

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import os, urllib, json

app = Flask(__name__)

@app.route("/")
def root():
    nasa_key = open("key_nasa.txt").read()
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key="+ nasa_key) #api key as file
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic = data["url"], explanation = data["explanation"])

if __name__ == "__main__":
    app.debug = True
    app.run()

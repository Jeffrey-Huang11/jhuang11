# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

#This version is similar to v0, except that no extra text will be printed in the terminal
#As predicted, v1 app.py just prints the quote in the body of the page, with nothing additional to the terminal log

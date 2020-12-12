# Team Elephant (Jeffrey Huang, Matthew Hui, Winnie Huang, Ethan Machleder)
# SoftDev
# K15 -- Sessions Greetings
# 2020-12-14

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )

@app.route("/welcome", methods=['GET', 'POST']) #, methods=['GET', 'POST'])
def disp_welcomepage():
    username = abracadabra
    password = 123456

    if request.args['username'] != username and request.args['password'] != password:
        return ('Invalid Login Attempt. Bad juju Human (>-<) ')
    if request.args['username'] != username:
        return ('Invalid Login Attempt. Hint: Check your Username (>-<)')
    if request.args['password'] != password:
        return ('Invalid Login Attempt. Hint: Check your Password (>-<)')

    return render_template( 'welcome.html', user = request.args['username'])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()

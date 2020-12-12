# Team Elephant (Jeffrey Huang, Matthew Hui, Winnie Huang, Ethan Machleder)
# SoftDev
# K15 -- Sessions Greetings
# 2020-12-14

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import sessions
import secrets

app = Flask(__name__)    #create Flask object
secret_key = secrets.token_hex(16)
app.secret_key= secret_key

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )

@app.route("/", methods=['GET', 'POST']) #, methods=['GET', 'POST'])
def disp_welcomepage():

    username = 'abracadabra'
    password = '123456'

    if request.args['username'] != username and request.args['password'] != password:
        return (''' <h1> Invalid Login Attempt. Bad juju Human \(^-^)/ </h1>
                    <a href="http://127.0.0.1:5000/">Go Back</a> ''')
    if request.args['username'] != username:
        return (''' <h1> Invalid Login Attempt. Hint: Check your Username (>-<) </h1>
                   <a href="http://127.0.0.1:5000/">Go Back</a> ''')
    if request.args['password'] != password:
        return (''' <h1> Invalid Login Attempt. Hint: Check your Password (>-<) </h1>
                   <a href="http://127.0.0.1:5000/">Go Back</a> ''')

    return render_template( 'welcome.html', user = request.args['username'])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()

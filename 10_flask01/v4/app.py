# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#Line 10 will print "the __name__ of this module is…” in the terminal
#Line 11 will print “__main__” in the terminal
#Line 12 prints "No hablo queso!" in the webpage
#If true, decided by whether the file is imported or not, line 15 will enable the debugging mode (makes available: variable names, line numbers, etc. from the source code)
#Upon running, the terminal prints that Debug mode is on and that the Debugger is active (also provided a debugger pin), and detects changes to the source code and restarts with stat

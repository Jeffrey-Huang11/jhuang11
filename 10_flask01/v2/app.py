# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

#Because it’s all wrapped in quotes, line 10, will print "about to print __name__..." straight into the terminal
#print(__name__) will print __main__ into the terminal, exactly like v0’s print statement
#Return “No hablo queso!” will do the same as in versions 0 and 1.
#Upon running the app.py, “about to print __name__…” and “__main__” are both printed in the terminal

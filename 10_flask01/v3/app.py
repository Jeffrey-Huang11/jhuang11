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

app.debug = True
app.run()

#Line 10 prints "about to print __name__..." in the terminal
#Line 11 prints “__main__” in the terminal
#Line 12 prints "No hablo queso!" in the webpage
#Line 14 will enable the debugging mode

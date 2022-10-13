# DWS: David, Wan Ying, Shinji
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # Makes a flask app

# @app.route("/")

# def new_funct():
#     print("aaaaa")
#     return "Por favor"

@app.route("/") # Defines the route/filepath to the app.

def hello_world():
    print(__name__) # Prints in the terminal where the app is being run(__main__). Doing print(__main__) causes an error.
    return "No hablo queso!"  # What's printed on the browser when the link is clicked.

@app.route("/test")
def new_funct():
        return "Por favor"
app.run()  # Runs the process. If this line doesn't exist, nothing is run.
# Runs the first method attached to @app.route("/"), only one method can be attached to
# a decorator. When the link is clicked, the method attached to @app.route("/") is run
# Another route can be defined by a /[text] and multiple routes can exist at once.
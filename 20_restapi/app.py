# Team NPC: Shafiul Haque, David Deng
# SoftDev pd08
# K20: A RESTful Journey Skyward
# 2022-11-21
# time spent: 0.3hrs

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

app = Flask(__name__) 

@app.route('/')
def show():
    return render_template('main.html', ) #if user isn't already logged in go to login page

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
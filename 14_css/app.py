# Team Mykolyk Fan Club: Shafiul Haque, David Deng, April Li
# SoftDev pd08
# K14: Serving Looks
# 2022-10-19
# time spent: 0.3hrs

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

mydict = {

}

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'index.html' )

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
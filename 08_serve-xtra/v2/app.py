# DWS: David, Wan Ying, Shinji
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

'''
Differences: Has an extra statement print("about to print __name__...")

Notes:
Prints the statement in the terminal when the link is clicked.
'''
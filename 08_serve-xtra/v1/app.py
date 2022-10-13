# DWS: David, Wan Ying, Shinji
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

'''
Differences: No print statement in hello_world()

Notes:
Doesn't print __main__ in the terminal when the link is clicked
'''
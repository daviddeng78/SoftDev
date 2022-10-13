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

app.debug = True
app.run()

'''
Differences: app.debug = True(debug mode is turned on)

Notes:
Debug mode is active and a debugger pin is printed. The debug mode detects when a change
is made to the file while it's currently running and then restarts again. Gives further
information on certain errors that the non-debug mode does not give. For example, if you
comment out the return statement in the hello_world() function,rather than opening a page
that just says internal server error, it opens a page than says what function caused the
error, what the error was and a copy of the traceback to the error.
Also says "The debugger caught an exception in your WSGI application. You can now look
at the traceback which led to the error."
'''
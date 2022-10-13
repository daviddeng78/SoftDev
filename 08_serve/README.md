## DWS: David, Wan Ying, Shinji
## SoftDev pd 8
## K08: serve
## 2022-10

### v0
we observed that 
- print(__name__): Prints in the terminal where the app is being run(__main__). Doing print(__main__) causes an error
- return "No hablo queso!": what's printed on the browser when the link is clicked.
- app.run(): Runs the process. If this line doesn't exist, nothing is run. Moreover, this line runs the first method attached to @app.route("/"), only one method can be attached to a decorator. 
we discovered that
- Another route can be defined by a /[text] and multiple routes can exist at once.

### v1
differences from v0: No print statement in hello_world()
we observed that
- No __main__ is printed in the terminal when the link is clicked

### v2
differences from v0: Has an extra statement print("about to print __name__...")
we observed that
- terminal prints this statement when user clicked the link.

### v3
differences from v0: app.debug = True (debug mode is turned on)
we observed that
- Debug mode is active and a debugger pin is printed. The debug mode detects when a change is made to the file while it's currently running and then restarts again. 
The Debuger gives further information on certain errors that the non-debug mode does not give. For example, if you comment out the return statement in the hello_world() function, rather than opening a page that just says internal server error, it opens a page than says what function caused the error, what the error was and a copy of the traceback to the error. 

### v4
differences from v0: Extra if statement to run the app and set debug to true
we observed that
- __name__ is __main__, at least when the code is run normally

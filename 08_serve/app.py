'''
DWS: David, Wan Ying, Shinji
SoftDev
K06 duo mission
2022-10-7
Time spent: 1.5 hours
DISCO:
You can use HTML formatting in the strings to make it appear on the browser in the way you want it to.
QCC:
'''

from flask import Flask
import random as rng
app = Flask(__name__)


def csv_to_dict(file):
    data = file.read()
    result = {}
    lines = data.split("\n")
    lines = lines[1:len(lines)-1]

    for oneline in lines:
        if '"' in oneline:
            oneline = oneline[1::]
            values = oneline.split('"')
            values[1] = values[1][1::]
            result[values[0]] = float(values[1])
        else:
            values = oneline.split(",")
            result[values[0]] = float(values[1])
    return result

def weighted_random(dnary):
    randval = rng.uniform(0, 100)
    current_val = 0
    if randval >= dnary["Total"]: #to account of the 0.2% not in total
        return "Other"
    for i in dnary.keys():
        if randval >= current_val and randval < current_val + dnary[i]:
            return i
        else:
            current_val += dnary[i]
            
@app.route("/")
def occupation_chooser(): ## Cant use \n to linebreak, use </br> instead
    occ_file = open("occupations.csv", "r")
    a = csv_to_dict(occ_file)
    b = weighted_random(a)
    c = list(a.keys())
    c = c[0:len(c)-1:]
    tname = "<h1 align = 'center'> DWS: David, Wan Ying, Shinji </h1> </br> </br> </br>"
    choice = "<h2 align = 'center'>" + b + "</h2> </br> </br> </br> </br>"
    occupationlist = "<h2 align = 'center'> Occupations: </h2> </br> <h4 align = 'center'>"
    for i in range(len(c)):
        splitstring = c[i].split(" ")
        occupationlist += "<a href= https://www.youtube.com/results?search_query=how+to+become+a+"
        for j in range(len(splitstring)):
            occupationlist += splitstring[j]
            if j < len(splitstring) - 1:
                occupationlist += "+"
        occupationlist += ">" + c[i] + "</a>" + "</br>"
    occupationlist += "Other </br>"
    occupationlist += "</h4>"
    return tname + choice + occupationlist

if __name__ == "__main__":
    app.debug = True
    app.run()
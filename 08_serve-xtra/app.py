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
    tname = "<h1 align = 'center'> DWS: David, Wan Ying, Shinji </h1> </br> </br> </br>"
    splitup = b.split(" ")
    choice = "<h2 align = 'center'>" + "<a href= https://www.youtube.com/results?search_query=how+to+go+into+"
    for i in range(len(splitup)):
        choice += splitup[i]
        if i < len(splitup) - 1:
            choice += "+"
    choice += ">" + b + "</a> </h2> </br> </br> </br> </br>"
    occupationlist = "<h2 align = 'center'> <a href= static/occupationlist.html> All occupations: </a> </h2> </br> <h4 align = 'center'>"
    return tname + choice + occupationlist

if __name__ == "__main__":
    app.debug = True
    app.run()
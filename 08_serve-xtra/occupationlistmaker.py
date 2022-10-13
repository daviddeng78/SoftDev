import random as rng

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


def occupationlist(): ## Cant use \n to linebreak, use </br> instead
    occ_file = open("occupations.csv", "r")
    a = csv_to_dict(occ_file)
    c = list(a.keys())
    c = c[0:len(c)-1:]
    occupationlist = "<h2 align = 'center'> Occupations: </h2> </br> <h4 align = 'center'>"
    for i in range(len(c)):
        splitstring = c[i].split(" ")
        occupationlist += "<a href= https://www.youtube.com/results?search_query=how+to+go+into+"
        for j in range(len(splitstring)):
            occupationlist += splitstring[j]
            if j < len(splitstring) - 1:
                occupationlist += "+"
        occupationlist += ">" + c[i] + "</a>" + "</br>"
    occupationlist += "Other </br>"
    occupationlist += "</h4>"
    return occupationlist

print(occupationlist())
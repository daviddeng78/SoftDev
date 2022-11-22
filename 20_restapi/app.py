# Team NPC: Shafiul Haque, David Deng
# SoftDev pd08
# K20: A RESTful Journey Skyward
# 2022-11-21
# time spent: 0.3hrs

from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__)
key = open("key_nasa.txt", "r").read()

@app.route('/')
def show():
    # print(key)
    url = request.urlopen(f"https://api.nasa.gov/planetary/apod?api_key={key}").read()
    # print(url)
    dict = json.loads(url)
    # print(dict)
    return render_template('main.html', picture=dict['url'], explanation=dict['explanation'], head = dict['title'])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()

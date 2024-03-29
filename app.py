import webbrowser
import requests
import os
from pprint import pprint
from flask import Flask, render_template, jsonify, request

apikey = "NAzhAKbEBS7c1rLBGsArGFo7Gw3Oyp3D"

query_url = f"http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key={apikey}"

r = requests.get(query_url)

data = r.json()

num = len(data["results"])

x = 0

namearr = [None] * num
abstractarr = [None] * num
updatedarr = [None] * num
urlarr = [None] * num

while x < num:
  namearr[x] = (data["results"][x]["title"])
  abstractarr[x] = (data["results"][x]["abstract"])
  updatedarr[x] = (data["results"][x]["updated"])
  urlarr[x] = (data["results"][x]["url"])
  
  x = x + 1

webbrowser.open("http://localhost:5000/")

app = Flask(__name__)

@app.route('/')
def index():
    namearrx = namearr
    numx = num
    abstractarrx = abstractarr
    updatedarrx = updatedarr
    urlarrx = urlarr
    return render_template('index.html', name=namearrx,abstract = abstractarrx,updated = updatedarrx,url = urlarrx,num=numx)

@app.route('/details')
def details():
    
    index = request.args.get('index')
    abstract = request.args.get('abstract')
    updated = request.args.get('updated')
    url = request.args.get('url')
    return f"Abstract: {abstract}<br>Last updated: {updated}<br>Url to Article: {url}"

if __name__ == '__main__':
    app.run()
    




    
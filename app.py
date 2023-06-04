import webbrowser
import requests
import os
from pprint import pprint
from flask import Flask, render_template, jsonify, request

apikey = "NAzhAKbEBS7c1rLBGsArGFo7Gw3Oyp3D"

# Top Stories:
# https://developer.nytimes.com/docs/top-stories-product/1/overview
section = "science"
# query_url = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={apikey}"
query_url = f"http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key={apikey}"

r = requests.get(query_url)

data = r.json()

num = len(data["results"])

x = 0
#namearr = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]
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

"""
i = 0


while i < num:
  print(namearr[i])
  i += 1
"""

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
    # Retrieve the output value from the array based on the index
    index = request.args.get('index')
    abstract = request.args.get('abstract')
    updated = request.args.get('updated')
    url = request.args.get('url')

    # Pass the output value to a new template or perform any desired action
    #render_template('output.html', abstract=abstract,updated=updated,url=url)
    return f"Abstract: {abstract}<br>Last updated: {updated}<br>Url to Article: {url}"

if __name__ == '__main__':
    app.run()
    
"""
<div id="name" data-value= {{name}}></div>

<script>
  var name = document.getElementById('name');
  var attributeValue = name.getAttribute('data-value');
"""    



    
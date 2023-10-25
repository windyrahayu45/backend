from Cors import App 
from flask import request, jsonify
import json
import requests
from bs4 import BeautifulSoup


data = []

# modified
@App.route("/", methods=["GET", "POST"])
def sample_api():
    if request.method == "GET":
        data.append('wndi')
    return json.dumps(data)


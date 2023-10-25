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

@App.route('/infosumbar', methods=["GET", "POST"])
def getInfoSumbar():
    if request.method == "GET":
        last_page_num = request.get['pagination']
        total_words = []
        for i in range(1,int(last_page_num+1)):
            r = requests.get("https://infosumbar.net/page/"+format(i)+"/?s=padang+panjang")
            soup = BeautifulSoup(r.content.lower(), 'html.parser')
            words = soup.findAll('article')

            for word in words:
                url = word.find(attrs={'class': 'jeg_thumb'}).a['href']
                #title = word.find(attrs={'class': 'jeg_postblock_content'}).a.text
                #berita = word.find(attrs={'class': 'jeg_post_excerpt'}).p.text
                tgl = word.find(attrs={'class': 'jeg_post_meta'}).find(attrs={'class': 'jeg_meta_date'}).a.text
                #author = word.find(attrs={'class': 'jeg_post_meta'}).find(attrs={'class': 'jeg_meta_author'}).a.text
                data={'url' : url,'tgl' : tgl}
                total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)
   
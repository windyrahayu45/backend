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
        data.append('Windi Sri Rahayu')
    return json.dumps(data)

@App.route('/infosumbar', methods=["GET", "POST"])
def getInfoSumbar():
    if request.method == "GET":
        #last_page_num = pagination
        last_page_num = request.args['pagination']
        total = int(last_page_num)
        total_words = []
        for i in range(1,total):
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

@App.route('/antara', methods=["GET", "POST"])
def getAntara():
    if request.method == "GET":
        startDate = request.args['mulai']
        endDate = request.args['sampai']
        total_words = []
        output = []
        r = requests.get("https://www.antaranews.com/search?q=padang+panjang&startDate="+format(startDate)+"&endDate="+format(endDate)+"&inTitle=1&submit=Submit")
        soup = BeautifulSoup(r.content.lower(), 'html.parser')
        words = soup.findAll('article',{"class" : "simple-post simple-big clearfix"} )
        count = len(words)
        for word in words:
            url = word.find(attrs={'class': "simple-thumb"}).a['href']
            tgl = word.find('header').span.text
            data={'url' : url,'tgl':tgl}
            total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)

@App.route('/haluan', methods=["GET", "POST"])
def getHaluan():
    if request.method == "GET":
        #last_page_num = pagination
        last_page_num = request.args['pagination']
        total = int(last_page_num)
        total_words = []
        for i in range(1,total):
            url = "https://www.harianhaluan.com/search?q=padang%20panjang&page="+format(i)
            headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
            webpage = requests.get(url,headers=headers)
            soup = BeautifulSoup(webpage.content, 'html.parser')
            words = soup.findAll('div',{"class" : "latest__item"} )

            for word in words:
                url = word.find(attrs={'class': 'latest__title'}).a['href']
                tgl = word.find(attrs={'class': 'latest__date'}).get_text()
                data={'url' : url,'tgl' : tgl}
                total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)
   
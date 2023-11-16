from Cors import App 
from flask import request, jsonify
import json
import requests
from bs4 import BeautifulSoup
import datetime


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

@App.route('/pasbana', methods=["GET", "POST"])
def getPasBana():
    if request.method == "GET":
        totalBerita = request.args['total']
        total_words = []
        output = []
        r = requests.get("https://www.pasbana.com/search/label/Padang%20Panjang?max-results="+format(totalBerita))
        soup = BeautifulSoup(r.content.lower(), 'html.parser')
        words = soup.findAll('div',{"class" : "post-outer"} )
        for word in words:
            url = word.find(attrs={'class': "post-title entry-title"}).a['href']
            tgl = word.find("abbr",{'class': 'updated published timeago'}).get("title")
            #date_format = '%Y-%m-%d %H:%M:%S'
            d1 = datetime.datetime.strptime(tgl,"%Y-%m-%dt%H:%M:%S%z")
            new_format = "%Y-%m-%d %H:%M:%S"
            tgl2 = d1.strftime(new_format)
            data={'url' : url,'tgl' : tgl2}
            total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)


@App.route('/singgalang', methods=["GET", "POST"])
def getSinggalang():
    if request.method == "GET":
        total_words = []
        output = []
        headers = {
        'User-Agent': 'Mozilla/5.0',
        'X-Api-Key':'adf51226795afbc4e7575ccc124face7',
        }
        url = "https://hariansinggalang.co.id/?s=padang+panjang&post_type=post"

        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
        webpage = requests.get(url,headers=headers)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        words = soup.findAll('article')
        print(soup)

        for word in words:
            url = word.find(attrs={'class': 'entry-title'}).a['href']
            tgl = word.find(attrs={'class': 'meta-content'}).span.text
            data={'url' : url,'tgl' : tgl}
            total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)
   

@App.route('/fajarsumbar', methods=["GET", "POST"])
def getFajarSumbar():
    if request.method == "GET":
        totalBerita = request.args['total']
        total_words = []
        output = []
        r = requests.get("https://www.fajarsumbar.com/search?q=padang+panjang&max-results="+format(totalBerita))
        soup = BeautifulSoup(r.content.lower(), 'html.parser')
        words = soup.findAll('div',{"class" : "date-outer"} )
        count = len(words)
        print(words)
        for word in words:
            url = word.find(attrs={'class': "post-title entry-title"}).a['href']
            tgl = word.find(attrs={'class': 'date-header-home'}).get_text()
           
            data={'url' : url,'tgl' : tgl}
            total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)


@App.route('/investigasi', methods=["GET", "POST"])
def getInvestasi():
    if request.method == "GET":
        last_page_num = request.args['pagination']
        total = int(last_page_num)
        total_words = []
        for i in range(1,total):
            url = "https://investigasi.news/page/"+format(i)+"/?s=padang+panjang"
            headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
            webpage = requests.get(url,headers=headers)
            soup = BeautifulSoup(webpage.content, 'html.parser')
            words = soup.findAll('div',{"class" : "td-block-span6"} )

            for word in words:
                url = word.find(attrs={'class': 'entry-title td-module-title'}).a['href']
                tgl = word.find(attrs={'class': 'td-post-date'}).get_text()
                data={'url' : url,'tgl' : tgl}
                total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)


@App.route('/minangsatu', methods=["GET", "POST"])
def getMinangSatu():
    if request.method == "GET":
        total_words = []
        output = []
        headers = {
        'User-Agent': 'Mozilla/5.0',
        'X-Api-Key':'adf51226795afbc4e7575ccc124face7',
        }
        url = "https://minangsatu.com/cari/padang%20panjang"

        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
        webpage = requests.get(url,headers=headers)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        words = soup.findAll(['a'])

        for word in words:
            url = word['href']
            data={'url' : url}
            total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)

@App.route('/mjnews', methods=["GET", "POST"])
def getMjNews():
    if request.method == "GET":
        total_words = []
        output = []
        headers = {
        'User-Agent': 'Mozilla/5.0',
        'X-Api-Key':'adf51226795afbc4e7575ccc124face7',
        }
        url = "https://www.mjnews.id/?s=padang+panjang&post_type=post"

        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
        webpage = requests.get(url,headers=headers)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        words = soup.findAll('article')

        for word in words:
            url = word.find(attrs={'class': 'box-item'}).a['href']
            tgl = word.find(attrs={'class': 'posted-on'}).get_text()
            data={'url' : url,'tgl' : tgl}
            total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)

@App.route('/topsumbar', methods=["GET", "POST"])
def getTopSumbar():
    if request.method == "GET":
        total_words = []
        output = []
        headers = {
        'User-Agent': 'Mozilla/5.0',
        'X-Api-Key':'adf51226795afbc4e7575ccc124face7',
        }
        url = "https://www.topsumbar.co.id/?s=padang+panjang"

        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
        webpage = requests.get(url,headers=headers)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        words = soup.findAll('article')

        for word in words:
            url = word.find(attrs={'class': 'entry-title'}).a['href']
            tgl = word.find(attrs={'class': 'posted-on byline'}).get_text()
            data={'url' : url,'tgl' : tgl}
            total_words.append(data)
    hasil = {"total" : len(total_words), "data" : total_words}
    return jsonify(hasil)
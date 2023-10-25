from Cors import App 
from flask import request
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import datetime
import requests

data = []

# modified
@App.route("/", methods=["GET", "POST"])
def sample_api():
    if request.method == "GET":
        data.append('wndi')
    return json.dumps(data)


    if request.method == "GET":
        r = requests.get("https://infosumbar.net/?s=padang+panjang")
        soup = BeautifulSoup(r.content.lower(), 'html.parser')
        #last_page_num = soup.find(class_="page_nav next").find_previous_sibling().text
        last_page_num = '5'
        total_words = []
        output = []
        for i in range(1,int(last_page_num)):
            r = requests.get("https://infosumbar.net/page/"+format(i)+"/?s=padang+panjang")
            soup = BeautifulSoup(r.content.lower(), 'html.parser')
            words = soup.findAll('article')
            count = len(words)
            #print(words[4])
            # words_list = [ ele.strip() for ele in words ]

            for word in words:
                url = word.find(attrs={'class': 'jeg_thumb'}).a['href']
                title = word.find(attrs={'class': 'jeg_postblock_content'}).a.text
                berita = word.find(attrs={'class': 'jeg_post_excerpt'}).p.text
                tgl = word.find(attrs={'class': 'jeg_post_meta'}).find(attrs={'class': 'jeg_meta_date'}).a.text
                author = word.find(attrs={'class': 'jeg_post_meta'}).find(attrs={'class': 'jeg_meta_author'}).a.text
                # data={'url' : url,'title' : title,'isi' : berita,
                #     'tgl' : tgl,
                #     'author' : author
                # }
                data={'url' : url,'tgl' : tgl}
                total_words.append(data)
    return json.dumps(total_words)
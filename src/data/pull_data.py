# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 01:43:57 2017

@author: Shashwat Pathak
"""

import requests
from bs4 import BeautifulSoup
import os
path = os.getcwd()


def dl_doc(link):
    page = requests.get(link)
    return page


def parse_it(doc):
    return BeautifulSoup(doc.content, 'html.parser')

such_speech = dl_doc('http://obamaspeeches.com/')
parsed_page = parse_it(such_speech)

text = parsed_page.find_all('font')[-2].get_text()

with open(path+'/data/raw/obamaspeech.txt', 'w', encoding='utf-8') as f:
    print(f.name)
    f.write(text)
    f.close()

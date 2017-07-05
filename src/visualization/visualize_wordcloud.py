# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 02:10:52 2017

@author: Shashwat Pathak
"""

import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
path = os.getcwd()

text = open(path+'/data/raw/obamaspeech.txt').read()

wordcloud = WordCloud().generate(text)

wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig(path+'/reports/figures/obamaspeech.png')

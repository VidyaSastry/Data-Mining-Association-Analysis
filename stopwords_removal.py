#!/usr/bin/python
import nltk
from nltk.corpus import stopwords

word_list = open("familyhistory.txt", "r")
stops = set(stopwords.words('english'))
outfile = open("family.txt","w")

for line in word_list:
    for w in line.split():
        if w.lower() not in stops:
            outfile.write(w + '\n')

outfile.close()

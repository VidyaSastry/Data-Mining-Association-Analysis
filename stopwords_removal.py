#!/usr/bin/python
import nltk
from nltk.corpus import stopwords

word_list = open("familyhistory.txt", "r")
stops = set(stopwords.words('english'))
outfile = open("family.txt","w")

for line in word_list:
	text =' '.join([word for word in line.split() if word not in stops])
	outfile.write(text + '\n')

outfile.close()

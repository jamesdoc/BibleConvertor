#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import re

from unidecode import unidecode

conn = sqlite3.connect("NIV'11.SQLite3")
outputFileName = "NIV 2011"

tags = ["<pb/>", "<v>", "</v>", "<t>", "</t>", "<e>", "</e>", "<J>", "</J>", "<i>", "</i>", "<n>", "</n>"]

c = conn.cursor()

def tidyVerse(text):
  # Remove editorial notations
  text = re.sub("<f>(.*?)</f>", "", text)
  text = re.sub("<n>\[(.*?)\]</n>", "", text)
  
  for tag in tags:
    text = text.replace(tag, "")

  text = unidecode(text)
  
  return text

allTheVerses = c.execute("SELECT books.long_name, verses.chapter, verses.verse, verses.text FROM books INNER JOIN verses ON verses.book_number = books.book_number")

bookName = 0
chapterNo = 0

file = open(outputFileName, "w") 

file.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
file.write('<bible>\n')

# Loop through each verse in the bible…
for row in allTheVerses:
  # If we're switching books…
  if bookName != row[0]:
    if (bookName != 0):
      file.write('</c>\n</b>\n')
    file.write('<b n="%s">\n' % row[0])
    file.write('<c n="%s">\n' % row[1])
    bookName = row[0]
    chapterNo = row[1]

  # If we're entering a new chapter…
  if chapterNo != row[1]:
    if (chapterNo != 0) or (chapterNo > row[1]):
      file.write('</c>\n')

    file.write('<c n="%s">\n' % (row[1]))
    chapterNo = row[1]

  # Spit out the verse…
  file.write('<v n="%s">%s</v>\n' % (row[2], tidyVerse(row[3])))

# Close everything off
file.write('</c>\n')
file.write('</b>\n')
file.write('</bible>')

file.close() 
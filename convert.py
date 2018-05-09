#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from unidecode import unidecode

conn = sqlite3.connect('niv2011.sqlite3')
outputFileName = "niv2011"

c = conn.cursor()

def verseSplitter(chver):
  split = str(chver).split(".")
  chapter = split[0]
  verse = split[1]

  while len(verse) < 3:
    verse = verse + '0'

  return {'c': int(chapter), 'v': int(verse)}

def remove_non_ascii(text):
  text = text.replace("\n", " ")
  text = text.replace("&nbsp;", " ")
  text = unidecode(text)
  return text


allTheVerses = c.execute("SELECT human, verse, unformatted FROM verses LEFT JOIN books on verses.book = books.osis")

bookName = 0
chapterNo = 0

file = open(outputFileName, "w") 

file.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
file.write('<bible>\n')

# Loop through each verse in the bible…
for row in allTheVerses:
  chver = verseSplitter(row[1])
  verseText = remove_non_ascii(row[2])

  # If we're switching books…
  if bookName != row[0]:
    if (bookName != 0):
      file.write('</c>\n</b>\n')
    file.write('<b n="%s">\n' % row[0])
    file.write('<c n="%s">\n' % chver['c'])
    bookName = row[0]
    chapterNo = chver['c']

  # If we're entering a new chapter…
  if chapterNo != chver['c']:
    if (chapterNo != 0) or (chapterNo > chver ['c']):
      file.write('</c>\n')

    file.write('<c n="%s">\n' % (chver['c']))
    chapterNo = chver['c']

  # Spit out the verse…
  file.write('<v n="%s">%s</v>\n' % (chver['v'], verseText))

# Close everything off
file.write('</c>\n')
file.write('</b>\n')
file.write('</bible>')

file.close() 
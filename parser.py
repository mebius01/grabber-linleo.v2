#!/usr/bin/env python
# -*- coding: utf-8 -*-
#1 SMP Debian 3.2.51-1 i686 data:2013-12-07

import re, sys, os

open_html=open('LinguaLeo.html')
read_html=open_html.read()
word_value=re.findall('(?<="word_value":").*?(?=",")', read_html)
translate_value=re.findall('(?<=translate_value":").*?(?=",")', read_html)
id_word=re.findall('[0-9]+-[0-9]+.mp3', read_html)
sound_url=re.findall('(?<=sound_url":").*?(?=",")', read_html)
title_text=re.search('(?<=<title>).*?(?= текст перевод)', read_html).group()
open_html.close()

file_hush=open('hush', 'r+')
file_hush_2=file_hush.readlines()

os.mkdir(title_text)
os.chdir(title_text)

for i in sound_url:
	os.system('wget %s' %i)
for i in id_word:
	file_id_word=open(i, 'a+')
	file_id_word.writelines(file_hush_2)
	file_hush.close()
	file_id_word.close()

while len(word_value) != 0:
	a=word_value.pop(0)
	b=translate_value.pop(0)
	c=id_word.pop(0)
	os.rename(c, a+' - '+b+'.mp3')
list_dir=os.listdir('.')
list_dir.sort()
for i in list_dir:
	file_word=open(title_text+'.txt', 'a+')
	file_word.writelines(i[0:-4]+'\n')
	file_word.close()

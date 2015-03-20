#!/usr/bin/env python
# -*- coding: utf-8 -*-
#1 SMP Debian 3.2.51-1 i686 data:2013-12-07

import re, sys, os, shutil

open_html=open('LinguaLeo.html')
read_html=open_html.read()
word_value=re.findall('(?<="word_value":").*?(?=",")', read_html) # список слов
translate_value=re.findall('(?<=translate_value":").*?(?=",")', read_html) # список перевод 
id_word=re.findall('[0-9]+-[0-9]+.mp3', read_html) # id слов в коде html
sound_url=re.findall('(?<=sound_url":").*?(?=",")', read_html) # произношение аудио
title_text=re.search('(?<=<title>).*?(?= текст перевод)', read_html).group() # название текста

open_html.close()
file_hush=open('hush', 'r+')
file_hush_2=file_hush.readlines()
os.mkdir(title_text) #
os.chdir(title_text)
# создаем необходимое количество папок
len_word=len(word_value)/10 
for i in range(1,len_word+1):
	i=str(i)
	os.mkdir(i)
# скачиваем аудио
for i in sound_url:
	os.system('wget %s' %i)
# дописываем в конец аудио файла пустоту
for i in id_word:
	file_id_word=open(i, 'a+')
	file_id_word.writelines(file_hush_2)
	file_hush.close()
	file_id_word.close()
# переименовать аудио файлы по на манер 'rays-лучи.mp3'
while len(word_value) != 0:
	a=word_value.pop(0)
	b=translate_value.pop(0)
	c=id_word.pop(0)
	os.rename(c, a+'-'+b+'.mp3')
# список отсортированных файлов
list_dir=os.listdir('.')
list_dir.sort()
for i in list_dir:
	file_word=open(title_text+'.txt', 'a+')
	file_word.writelines(i[0:-4]+'\n')
	file_word.close()
# 
def F(b):
	z=10
	while z != 0:
		shutil.move(list_file_wav.pop(0), b) 
		z-=1

list_dir=[]
list_file=[]
list_file_wav=[]
#~ for i in os.listdir("."):
	#~ if i[-4:]=='.mp3':
		#~ os.system('ecasound -i ' +i +' -ea:20% -o ' +i[:-4]+'.wav')
for i in os.listdir("."):
	if i[-4:]=='.mp3':
		list_file.append(i)
	if i[-4:]=='.wav':
		list_file_wav.append(i)
	elif i[-4:] != ('.mp3' or '.txt' or '.wav'):
		list_dir.append(i)

for i in list_dir:
	if len(os.listdir(i)) == 0:
		F(i)




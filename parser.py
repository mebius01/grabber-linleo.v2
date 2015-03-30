#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, sys, os, shutil

open_html=open('LinguaLeo.html')
read_html=open_html.read()
word_value=re.findall('(?<="word_value":").*?(?=",")', read_html) # список слов
translate_value=re.findall('(?<=translate_value":").*?(?=",")', read_html) # список перевод 
id_word=re.findall('[0-9]+-[0-9]+.mp3', read_html) # id слов в коде html
sound_url=re.findall('(?<=sound_url":").*?(?=",")', read_html) # произношение аудио
title_text=re.search('(?<=<title>).*?(?= текст перевод)', read_html).group() # название текста
open_html.close()

# создать "пустоту"
file_hush=open('hush', 'r+'); file_hush_2=file_hush.readlines()

# создаем директорию и переходим в нее
os.mkdir(title_text) 
os.chdir(title_text)

# создаем необходимое количество папок mp3 and wav
len_word=len(word_value)/10 
for i in range(1,len_word+1):
	i=str(i)
	os.mkdir(i+'-mp3')
	os.mkdir(i+'-wav')

# скачиваем аудио
for i in sound_url:
	os.system('wget %s' %i)
 
# дописываем в конец аудио файла "пустоту"
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
	os.rename(c, a+' - '+b+'.mp3')
# создаем файл слово - перевод
def word_text():
	list_dir=os.listdir('.')
	list_dir.sort()
	for i in list_dir:
		file_word=open(title_text+'.txt', 'a+')
		file_word.writelines(i[0:-4]+'\n')
		file_word.close()
word_text()

# удаляем пробелы, для ecasound
def space(s, e):

	for i in os.listdir("."):
		if s in i:
			os.rename(i, i.replace(s, e))
space(" ", "_")

# конвертируем mp3 в wav
for i in os.listdir("."):
	if i[-4:]=='.mp3':
		os.system('ecasound -i ' +i +' -ea:20% -o ' +i[:-4]+'.wav')
#~ 
# вернуть пробелы
space("_", " ")

# раскидываем по спискам wav и mp3 + списки директорий
list_dir_mp3=[]
list_dir_wav=[]
list_file_mp3=[]
list_file_wav=[]
for i in os.listdir("."):
	if i[-4:]=='.mp3':
		list_file_mp3.append(i)
	elif i[-4:]=='.wav':
		list_file_wav.append(i)
	elif (i[-4:]!='.mp3') and (i[-4:]!='.txt') and (i[-4:]!='.wav') and (i[-4:]=='-wav'):
		list_dir_wav.append(i)
	elif (i[-4:]!='.mp3') and (i[-4:]!='.txt') and (i[-4:]!='.wav') and (i[-4:]=='-mp3'):
		list_dir_mp3.append(i)

# раскидываем файлы по нужным директориям
def list_dir(list_d, list_f):
	def rec(d, z):
		while z != 0:
				shutil.move(list_f.pop(0), d) 
				z-=1
	while len(list_f) >0:
		for i in list_d:
			rec(i, 1)
try:
	list_dir(list_dir_mp3, list_file_mp3)
except IndexError:
	print "pop from empty list MP3"
try:
	list_dir(list_dir_wav, list_file_wav)
except IndexError:
	print "pop from empty list WAV"

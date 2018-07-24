#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import re, sys, os, shutil

open_html=open('LinguaLeo.html')
read_html=open_html.read()
block_id=re.findall('(?<="dict-item-word).*?(?=</div><div)', read_html) # блоки id
open_html.close()
print(len(block_id))

id_list=[]
for i in block_id:
	word_value=re.findall('(?<=data-word-value=").*?(?=[\">])', i)
	translate_value=re.findall('(?<=t-ellps"> ).*?(?=[</span])', i)
	sound_url=re.findall('(?<=data-voice-url=").*?(?=[",])', i)
	id_word=re.findall('[0-9]+-[0-9]+.mp3', i)
	id_list.append([word_value,translate_value,sound_url,id_word])
	"""
	word_value i[0][0]
	translate_value i[1][0]
	sound_url i[2][0]
	id_word i[3][0]
	
	"""

# создать "пустоту" WORK
file_hush=open('hush', 'r+'); file_hush_2=file_hush.readlines()

#~ # создаем директорию и переходим в нее not work OR WORK
#os.mkdir(title_text) 
#os.chdir(title_text)

#~ # создаем необходимое количество папок mp3 WORK
len_word=len(id_list)/10 
for i in range(1,len_word+1):
	i=str(i)
	os.mkdir(i+'-mp3')

#~ # скачиваем аудио WOEK
for i in id_list:
	os.system('wget %s' %i[2][0])
 
# дописываем в конец аудио файла "пустоту"  WORK
for i in id_list:
	file_id_word=open(i[3][0], 'a+')
	file_id_word.writelines(file_hush_2)
	file_hush.close()
	file_id_word.close()

# переименовать аудио файлы по на манер 'rays-лучи.mp3' WORK
for i in id_list:
	os.rename(i[3][0], i[0][0]+' - '+i[1][0]+'.mp3')

# раскидываем по спискам wav и mp3 + списки директорий WORK
list_dir_mp3=[]
list_file_mp3=[]
for i in os.listdir("."):
	if i[-4:]=='.mp3':
		list_file_mp3.append(i)
	elif (i[-4:]!='.mp3') and (i[-4:]!='.txt') and (i[-4:]!='.wav') and (i[-4:]=='-mp3'):
		list_dir_mp3.append(i)

# раскидываем файлы по нужным директориям WORK
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
	print("pop from empty list MP3")

# файлы ang-rus.txt ang.txt rus.txt создать и наполнить
for i in list_dir_mp3:
	os.chdir(i)
	b=os.listdir('.')
	file_word=open('ang-rus.txt', 'a+')
	file_word_translate=open('rus.txt', 'a+')
	file_word_value=open('ang.txt', 'a+')
	for i in b:
		a=i[:-5]
		b=i.split(' - ')[0]
		c=i.split(' - ')[1][:-5]

		file_word.writelines(a+'\n')
		file_word_value.writelines(b+'\n')
		file_word_translate.writelines(c+'\n')
	file_word_translate.close()
	file_word_value.close()
	file_word.close()
	os.chdir('..')

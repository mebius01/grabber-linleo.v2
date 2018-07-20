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

# создаем директорию и переходим в нее not work OR WORK
#~ os.mkdir(title_text) 
#~ os.chdir(title_text)

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
	#~ s=i[0][0]+' - '+i[1][0]+'.mp3'
	os.rename(i[3][0], i[0][0]+' - '+i[1][0]+'.mp3')
	#~ print(i[3][0], i[0][0]+' - '+i[1][0]+'.mp3')
	"""
	word_value i[0][0]
	translate_value i[1][0]
	sound_url i[2][0]
	id_word i[3][0]
	
	"""
	

# создаем файл слово - перевод NOT WORK
#~ def word_text(a):
	#~ os.chdir(a)
	#~ b=os.listdir('.')
	#~ z=0
	#~ file_word=open('ang-rus.txt', 'a+')
	#~ file_word_translate=open('rus.txt', 'a+')
	#~ file_word_value=open('ang.txt', 'a+')
	#~ while len(b) > z:
	#~ for i in b:
		#~ file_word.writelines(i+'\n')
		#~ file_word_translate.writelines(translate_value[z]+'\n')
		#~ z+=1
	#~ file_word_translate.close()
	#~ file_word_value.close()
	#~ file_word.close()


# раскидываем по спискам wav и mp3 + списки директорий WORK
list_dir_mp3=[]
list_file_mp3=[]
for i in os.listdir("."):
	if i[-4:]=='.mp3':
		list_file_mp3.append(i)
	elif (i[-4:]!='.mp3') and (i[-4:]!='.txt') and (i[-4:]!='.wav') and (i[-4:]=='-mp3'):
		list_dir_mp3.append(i)

print(len(list_dir_mp3), len(list_file_mp3))

#~ # раскидываем файлы по нужным директориям WORK
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


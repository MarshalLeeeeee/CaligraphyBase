import requests
import json
import re
import os
import cv2
import numpy as np
import sys
from pypinyin import lazy_pinyin
from bs4 import BeautifulSoup
from PIL import Image

def gif2png(name):
	img = Image.open(name+'.gif')
	img.seek(0)
	frame = img.copy()
	frame.save(name+'.png',**frame.info)

def formulate(name):
	img = cv2.imread(name+'.png')
	img2 = img[:378,:,:]
	img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
	_,img2 = cv2.threshold(img2,120,255,cv2.THRESH_BINARY)
	cv2.imwrite(name+'.png',img2)

def saveCali(url,path):
	response = requests.get(url)
	#name = re.split(r'\/', url)[-1].split('.')[0]
	try:
		response.raise_for_status()
		with open(path+'.gif', 'wb') as f:
			f.write(response.content)
		gif2png(path)
		formulate(path)
	except:
		print("Error in saving the image...")

def getCali(path,target,char,cnt):
	url = 'http://www.sfzd.cn/s.php'
	targetName = ''.join(lazy_pinyin(target))
	if not os.path.exists(os.path.join(path,targetName)):
		os.mkdir(os.path.join(path,targetName))
	path = os.path.join(path,targetName)
	header = {
		'accept':'*/*',
		'accept-encoding':'gzip, deflate',
		'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
		}
	data = {'wd':char,'ziti':'x','leibie':'mb'}
	r = requests.post(url, headers = header, data = data)
	r.encoding = 'utf-8'
	soup = BeautifulSoup(r.text, "html.parser")
	dup = 0
	for img in soup.find_all('img'):
		if 'onclick' in img.attrs: 
			author = re.search(r'1,.*,',str(img)).group().split(',')[1][1:-1]
			if author == target:
				saveCali('http://www.sfzd.cn/'+img.attrs['src'],os.path.join(path, str(cnt)+'-'+str(dup)))
				dup += 1


if __name__ == '__main__':
	author = sys.argv[1]
	path = '..\demo'
	#getCali(path,author)
	with open('../characters/simple.txt', 'r', encoding='utf-8') as f:
		char = f.read().split()
	#getCali(path,author,char[0],0)
	for i in range(len(char)):
		getCali(path,author,char[i],i+1)
		print('character ', i+1,' is over...')
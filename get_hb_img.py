#coding:utf-8
from bs4 import BeautifulSoup
import requests
import os
import re
import sys
import random
import urllib
import time
import json
import shutil
from PIL import Image


search_word = raw_input('输入你要搜集图片的关键字\n')
get_img_count = raw_input('输入你要的搜集的图片数量\n')
get_range = int(get_img_count)/19
print get_range
file_name_dir = '/Users/tei/Desktop/python_exr/img/%s'%search_word
if os.path.exists(file_name_dir):
	file_name_dir = file_name_dir
else:
	os.mkdir(file_name_dir)

#图片整理

def filter_img_size():
	path = '/Users/tei/Desktop/python_exr/img/hb/'
	target_path = '/Users/tei/Desktop/python_exr/img/middle_folder/'
	for root,dirs,files in os.walk(path):
		for i in files:
			if i != '.DS_Store':
				get_img_path = root+i		

				imagesize = Image.open(get_img_path)
				get_scale_img = max(imagesize.size)-min(imagesize.size)
				get_scale_img_t =float(max(imagesize.size)) / float(min(imagesize.size))
				
				print float(get_scale_img_t)
				if get_scale_img == 0:	
					
					shutil.copyfile(get_img_path,target_path+i)
				elif get_scale_img_t < 1.3:
					shutil.copyfile(get_img_path,target_path+i)

			#print target_path_dir
			#shutil.copyfile(get_img_path,target_path_dir)

headers = {
	"Accept":"application/json",
	"Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
	"Connection":"keep-alive",
	"Referer":"http://huaban.com/search/?q=%E9%A3%8E%E6%99%AF&iqkl4t5n&page=4&per_page=20&wfl=1",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
	"X-Request":"JSON",
	"X-Requested-With":"XMLHttpRequest",
}

#图片抓取

a = 1
for i in range(get_range):
	
	encoding = urllib.quote(search_word)
	base_url = "http://huaban.com/search/?q=%s&iqkll625&page=%s&per_page=20&wfl=1"%(encoding,i)

	wb_data = requests.get(base_url,headers = headers)
	soup = BeautifulSoup(wb_data.text,'html.parser')
	print soup
	value = json.loads(str(soup))
	for i in value['pins']:
		get_pins = i[u'file']
		base_url_pre = 'http://hbimg.b0.upaiyun.com/'
		collpa_url = base_url_pre+get_pins[u'key']

		
		urllib.urlretrieve(collpa_url,'/Users/tei/Desktop/python_exr/img/%s/%s.jpg'%(search_word,a))
		a=a+1
		print  '下载%s张图片'%a
		time.sleep(0.5)
	time.sleep(2)

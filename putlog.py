import datetime
import sys
import os
IsExists = os.path.exists('py.log')
if not IsExists:
	os.mkdir('py.log')
def put(data):
	log_file_name=datetime.datetime.now().strftime('%Y-%m-%d')
	fo = open('py.log/'+log_file_name,'ab+')
	fo.write((datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')+'\t'+data+'\n').encode('utf-8'))
	fo.close()
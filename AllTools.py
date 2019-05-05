import SunPosition
import Image2Char
import putlog
import web
import requests
import os
from PIL import Image
table =  ' 8*&$@<>p)i=+;:,. '
urls = (
'/GetSunSetDay','GetSunSetDayClass',
'/Index','GetIndex',
'/GetCurrentIp','GetCurrentIpClass',
'/GetImageChar','GetImageCharClass',
'/GetImageWord','GetImageWordClass',
)
show_web=web.template.render("/root/weixin/web")
app = web.application(urls,globals())
class GetSunSetDayClass:
	def GET(self):
		return open(r'./web/GetSunSet.html').read()
	def POST(self):
		ChoseLayerNumber = web.input()['ChoseLayerNumber']
		FloorSpacing = web.input()['FloorSpacing']
		LayerHeight = web.input()['LayerHeight']
		LayerNumber = web.input()['LayerNumber']
		return str(SunPosition.GetSunSetDay(LayerNumber,FloorSpacing,LayerHeight,ChoseLayerNumber))
class GetCurrentIpClass:
	def GET(self):
		return str(web.ctx.env['REMOTE_ADDR']+":"+web.ctx.env["REMOTE_PORT"])
class GetImageCharClass:
	def  GET(self):
		return open(r'./web/Image2Char.html').read()
	def POST(self):
		upload_image=web.input(Image={})
		print(upload_image.Image.filename)
		new_file_name=upload_image.Image.filename.split('.')[0]+Image2Char.GetRandom()+'.'+upload_image.Image.filename.split('.')[1]
		fout=open(new_file_name,'wb')
		fout.write(upload_image.Image.file.read())
		fout.close()
		return Image2Char.covertImageToAscii(new_file_name,100,0.45,False)
class GetImageWordClass:
	def GET(self):
		return open(r'./web/Image2Word.html').read()
	def POST(self):
		upload_image=web.input(Image={})
		print(upload_image.Image.filename)
		new_file_name=upload_image.Image.filename.split('.')[0]+Image2Char.GetRandom()+'.'+upload_image.Image.filename.split('.')[1]
		fout=open(new_file_name,'wb')
		fout.write(upload_image.Image.file.read())
		fout.close()
		return Image2Char.convertImageToWord(new_file_name)


class GetIndex:
	def GET(self):
		return open(r'./web/AllTools.html').read()
#========================================================================================
#程序入口

if __name__ == '__main__':
     app.run()
     pass
from PIL import Image
import datetime
import codecs
import os
import sys, random, argparse#argparse库用于命令行解析
import numpy as np          #numpy库用于大型矩阵计算
import math
import pytesseract
# 图片转ASCII的基本原理是将灰度图片分割成众多小网格，将小网格的平均亮度计算出来用不同亮度字符代替
# 灰度梯度对应字符可参考：http://paulbourke.net/dataformats/asciiart/
# 70级灰度梯度（越来越亮）
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10级灰度梯度
gscale2 = '@%#*+=-:. '

#计算每一小块平均亮度
def getAverageL(image):
    im = np.array(image)#小块转成二维数组
    w, h = im.shape#保存小块尺寸
    return np.average(im.reshape(w * h))#将二维数组转成一维，求均值

#根据每一小块平均亮度匹配ASCII字符
def covertImageToAscii(fileName, cols, scale, moreLevels):
    global gscale1, gscale2#灰度梯度
    image = Image.open(fileName).convert('L')#打开图片并转换成灰度图
    # W, H = image.size[0], image.size[1]#保存图像宽高
    W, H = image.size[0], image.size[1]#保存图像宽高
    w = W / cols#计算小块宽度
    h = w / scale#计算小块高度，此处除垂直比例系数用于减少图像违和感，经测试scale为0.43时效果较好
    rows = int(H / h)#计算行数
    # print("共有%d行 %d列小块" % (rows,cols))
    # print("每一小块宽高: %dx%d" % (w, h))
    #图像太小则退出
    # if cols > W or rows > H:
    #     print("图像太小不足分割！（提高图像分辨率或降低精细度）")
    #     exit(0)
    aimg = []#文本图形存储到列表中
    #逐个小块匹配ASCII
    for j in range(rows):
        y1 = int(j * h)#小块开始的y坐标
        y2 = int((j + 1) * h)#小块结束的y坐标
        if j == rows - 1:
            y2 = H#最后一个小格不够大，结束y坐标用图像高度H表示
        aimg.append("")#先插入空串
        for i in range(cols):
            x1 = int(i * w)#小块开始的x坐标
            x2 = int((i + 1) * w)#小块结束的x坐标
            if i == cols - 1:
                x2 = W#最后一个小格不够大，结束x坐标用图像宽度W表示
            img = image.crop((x1, y1, x2, y2))#提取小块
            avg = int(getAverageL(img))#计算平均亮度
            if moreLevels:
                gsval = gscale1[int((avg * 69) / 255)]#平均亮度值[0,255]对应到十级灰度梯度[0,69]，获得对应ASCII符号
            else:
                gsval = gscale2[int((avg * 9) / 255)]#平均亮度值[0,255]对应到七十级灰度梯度[0,9]，获得对应ASCII符号
            aimg[j] += gsval#更新文本图形
    append = ''
    # append += '<!DOCTYPE html>\n'
    # append += '<html>\n'
    # append += '<meta charset="ansi" name="viewport" content="width=device-width, initial-scale=1"/>'
    # append += '<div style="text-align-last:justify;">'
    for temstr in aimg:
        # append += '<div style="white-space:nowrap;">'
        append += temstr+'\n'
        # append += '</div>'   
    # append += '</div>'    
    
    rand_name = GetRandom()
    imgtxt = open('/var/ftp/pub/'+GetRandom()+'.txt','wb')
    imgtxt.write(append.encode())
    imgtxt.close()
    # append += '<a href="ftp://140.143.18.125/pub/'+rand_name+'.txt" download="111">'+'ascii img'+rand_name+'</a>'
    # append += '</html>'
    os.remove(fileName)
    print(append)
    return append
def GetRandom():
	return datetime.datetime.now().strftime('%H%M%S')
def convertImageToWord(filepath):
    img = Image.open(filepath)
    img.convert('L')
    vcode =pytesseract.image_to_string(img,lang='chi_sim')
    fd = codecs.open('temp','wb','gbk')
    fd.write(vcode)
    fd.close()
    append=""
    append += '<!DOCTYPE html>\n'
    append += '<html>\n'
    append += '<meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1"/>'
    fd = codecs.open('temp','r','gbk')
    gbk_res=fd.read()
    append += gbk_res
    append += '</html>'
    print(vcode)
    img.close()
    os.remove(filepath)
    return append
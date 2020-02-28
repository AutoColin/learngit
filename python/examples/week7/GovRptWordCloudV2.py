#GovRptWordCloudV2.py 
import jieba
import wordcloud
from imageio import imread
mk = imread('./bbb.jpg')
'''imread使用的图片背景需要为全白，可以用win10的paint3d对图片进行编辑设为背景全白后使用，这里注意要使用magic select功能
    将主目标提取出来后新建然后复制过去才会将背景设为全白，在这里坑了好久'''      
#f = open('./新时代中国特色社会主义.txt', 'r', encoding = 'utf-8')
f = open('./关于实施乡村振兴战略的意见.txt', 'r', encoding = 'utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(mask = mk, font_path = 'msyh.ttf', width = 1000, height = 700, background_color = 'white')
w.generate(txt)
#w.to_file('socialismV22.png')
w.to_file('countrysideV21.png')

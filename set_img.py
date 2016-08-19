#coding:utf-8
from PIL import Image
import ImageDraw
import ImageFilter
import PSDraw
import random
import time
from PIL import ImageEnhance,ImageFont,ImageDraw,ImageMath,ImageSequence
f = Image.open('/Users/tei/Desktop/python_exr/img/美女/8.jpg')
fresize = f.resize((500,500))

box_blur = (20,20,220,80) 
box_region = (40,40,240,100)
str_name = (280,40,400,100)
str_name_1 = (280+120,40,400,100)
ISOTIMEFORMAT = '%Y-%m-%d %X'
get_time = time.strftime(ISOTIMEFORMAT,time.localtime())
text_wrap = zip([get_time,'title:discrable','is discrable'],[box_region,str_name,str_name_1])
crop = fresize.crop(box_blur).filter(ImageFilter.BLUR)
fresize.paste(crop,box_region)
draw = ImageDraw.Draw(fresize)
font_pick = ImageFont.truetype('Arial.ttf',12)
for text,region in text_wrap:
	draw.text(region,text,font= font_pick,) 

fresize.show()
f2 = Image.open('/Users/tei/Desktop/python_exr/img/美女/198.jpg')
f2resize = f2.resize((500,500))

#out = ImageMath.eval("min(a,b),'L'",a = fresize,b=f2resize)
#out.show()
fmask = Image.open('/Users/tei/Desktop/python_exr/circle.jpg')
fmask_resize = fmask.resize((500,500))
# def set_func(recive):
# print recive
# draw = ImageDraw.Draw(f)
#set_evale = Image.eval(f2resize,set_func(list_agr))
enhancer = ImageEnhance.Sharpness(fresize)
contrast = ImageEnhance.Contrast(enhancer.enhance(10.00))
contrast_img = contrast.enhance(2.0)
#contrast_img.filter(ImageFilter.FIND_EDGES).convert('L').show()

draw.line(((0,0),(f.size[0],f.size[1])),fill=255,width = 2)
get_pixel = f.getpixel((127,127))
pixel = (127,127)
color = (255,255,255,255)
f.putpixel(pixel,color)
blend_img = Image.blend(fresize,f2resize,0.5)
#blend_img.show()
mask = fmask_resize.convert('L')
composite = Image.composite(fresize,f2resize,mask)
#composite.show()
rotate_img = f.rotate(90)
#f.show()
box = (300,420,500,550)
#box_region = (420,300,550,500)
count = 0
auto_raise = 0

filter_list = ('BLUR','FIND_EDGES','CONTOUR','EMBOSS','SMOOTH')
for i in range(10):
	set_random = random.random()
	region = f.crop(box)
	box_region = (500,220+count,700,350+count)
	rgb2xyz = (
        set_random, 0.357580, 0.180423, auto_raise,
        0.212671, set_random, 0.180423, auto_raise,
        set_random, set_random, set_random, auto_raise  )
	out = region.convert("RGB", rgb2xyz)
	set_filter = out.filter(ImageFilter.EDGE_ENHANCE)
	#make_filter = region.filter(ImageFilter)
	conver_img = set_filter.convert('L')
	find_edges = conver_img.filter(ImageFilter.FIND_EDGES)
	pase_f = f.paste(find_edges,box_region)
	count+=100
	auto_raise += 10
#set_region.show()
f.show()
region.show()
rgb2xyz = (
        0.412453, 0.357580, 0.180423, 1,
        0.212671, 0.715160, 0.072169, 1,
        0.019334, 0.119193, 0.950227, 100 )
out = f.convert("RGB", rgb2xyz)
size = (300,500)
resize_f = f.resize((size[0],size[1]),Image.ANTIALIAS)
#make_filter = resize_f.filter(ImageFilter.CONTOUR)
#make_find_edges = resize_f.filter(ImageFilter.FIND_EDGES)
#make_filter.show()
#make_find_edges.show()
#resize_f.show()
#out.show()

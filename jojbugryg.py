from __future__ import print_function
import math
import random
from PIL import Image


image = Image.open('wpid-oau-kf1.jpg')
width = image.size[0]
length = image.size[1]


flipnumber = 20
for i in range(0,flipnumber):
	startx = math.floor(random.uniform(0,width))
	endx = math.floor(random.uniform(startx,width))

	starty = math.floor(random.uniform(0,length))
	endy = math.floor(random.uniform(starty,length))

	box = (startx,starty,endx,endy)

	region = image.crop(box)
	r, g, b = region.split()
	region = [r,g,b]

	value0 = 0*random.random()
	value1 = 1*random.random()
	value2 = 1-value1
	values = [value0,value1,value2]
	random.shuffle(values)
	[R,G,B] = values

	r = r.point(lambda i: i * R)
	g = g.point(lambda i: i * G)
	b = b.point(lambda i: i * B)

	region = Image.merge("RGB", (b, g, r))
	image.paste(region, box)
	


image.save('wpod-iau-lf1.jpg')

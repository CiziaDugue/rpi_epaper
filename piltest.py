#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import print_function
import time
from PIL import Image,ImageDraw,ImageFont
import traceback


# im = Image.open('../img/oslogo.png')
# # im = Image.open('../img/oslogo.svg')
# print(im.format, im.size, im.mode)
# im.show()
# out = im.resize((405, 428))
# print(out.format, out.size, out.mode)
# out.show()

imb = Image.open('img/oslogo-b.png')
imb.show()
# print(imb.format, imb.size, imb.mode)
# outb = imb.resize((405, 428))
# print(outb.format, outb.size, outb.mode)
# outb.show()

imr = Image.open('img/oslogo-r.png')
imr.show()
# print(imr.format, imr.size, imr.mode)
# outr = imr.resize((405, 428))
# print(outr.format, outr.size, outr.mode)
# outr.show()

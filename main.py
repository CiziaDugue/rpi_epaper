#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import print_function
import epd7in5b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback


try:
    epd = epd7in5b.EPD()
    epd.init()
    print("Clear...")
    epd.Clear(0xFF)

    print("read png file")
    imb = Image.open('img/oslogo-b.png')
    # outb = imb.resize((405, 428))
    print(imb.format, imb.size, imb.mode)
    imr = Image.open('img/oslogo-r.png')
    # outr = imr.resize((405, 428))
    print(imr.format, imr.size, imr.mode)
    epd.display(epd.getbuffer(imb), epd.getbuffer(imr))
    time.sleep(2)

    epd.sleep()

except:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()

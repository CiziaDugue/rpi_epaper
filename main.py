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
    outb = imb.resize((405, 428))
    print(outb.format, outb.size, outb.mode)
    imr = Image.open('img/oslogo-r.png')
    outr = imr.resize((405, 428))
    print(outr.format, outr.size, outr.mode)
    epd.display(epd.getbuffer(outb), epd.getbuffer(outr))
    time.sleep(2)

    epd.sleep()

except:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()

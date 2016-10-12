#!/bin/python
# encoding: utf-8

import Image, ImageDraw, ImageFont
import os, sys
import re
class image(object):
    def __init__(self):
        self.__im = None

    def open_image(self):
        try:
            for path in os.listdir("."):
                image_name, image_format = os.path.splitext(path)
                if re.match( r"jpg|raw|bmp", image_format[1:]):
                    self.__im = Image.open(path)
                    dr = ImageDraw.Draw(self.__im)
                    font = ImageFont.truetype('msyh.ttf', 60)
                    dr.text((self.__im.size[0]*0.8, self.__im.size[1]*0.05), "1", fill="#ff0000", font=font)
                    self.__im.save(image_name + "_change" + image_format)
                else:
                    pass
        except IOError, e:
            print "%s file no exist" % self.__path

if __name__ == '__main__':
    im = image()
    im.open_image()
    pass







































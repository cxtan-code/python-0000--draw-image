#!/bin/python
# encoding: utf-8

import Image
import ImageDraw
import ImageFont

image_path = "./test.jpg"


class image(object):
    def __init__(self, path):
        self.__path = path
        self.__im = None

    def get_path(self):
        path = self.__path
        return path

    def open_image(self, path):
        try:
            self.__im = Image.open(path)
            print self.__im.mode,self.__im.size,self.__im.format
            dr = ImageDraw.Draw(self.__im)
            font = ImageFont.truetype('msyh.ttf', 60)
            dr.text((self.__im.size[0]*0.8, self.__im.size[1]*0.05), "1", fill="#ff0000", font=font)
            self.__im.show()
            self.__im.save('result.jpg')
        except IOError :
            print "file no exist"

if __name__ == '__main__':
    im = image(image_path)
    im.open_image(im.get_path())
    pass







































#!/bin/python
# encoding: utf-8

import Image
import ImageDraw

image_path = "./test.jpg"
class image(object):
    def __init__(self, path):
        self.__path = path
        self.__im = None

    def get_path(self):
        path = self.__path
        return path

    def open_image(self, path):
        self.__im = Image.open(path)
        print self.__im.mode,self.__im.size,self.__im.format
        self.__im.show()

if __name__ == '__main__':
    im = image(image_path)
    im.open_image(im.get_path())
    pass




































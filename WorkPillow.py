#coding=utf-8

'Work: Third Party Lib Pillow'

__author__ = 'Hammurabi'

from PIL import Image

if __name__ == '__main__':
    im = Image.open('pic.jpg')
    print im.format, im.size, im.mode
    im.thumbnail((2000, 1000))
    im.save('thumb.png', 'PNG')

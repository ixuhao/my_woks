#!/usr/bin/env python
# coding: utf-8

import os, time
from SimpleCV import *

def match_img(source, template, outfile, thr=11,  med='CCOEFF_NORM'):
    # the various types of template matching available
    # ["SQR_DIFF","SQR_DIFF_NORM","CCOEFF","CCOEFF_NORM","CCORR","CCORR_NORM"]
    sou = Image(source, sample=True)
    width = float(sou.width)
    height= float(sou.height)
    print "source width, height:", width, height
    tmp = Image(template, sample=True)
    result = Image(source, sample=True)
    dl = DrawingLayer((sou.width, sou.height))
    fs = sou.findTemplate(tmp, threshold=thr, method=med)
    for match in fs:
        print "x, y, width, height"
        print match.x, match.y, match.width(), match.height()
        print ', '.join(str(i) for i in (match.x/width,match.y/height,match.width()/width,match.height()/height))
        dl.rectangle((match.x,match.y),(match.width(),match.height()),color=Color.RED)
    result.addDrawingLayer(dl)
    result.applyLayers()
    result.save(outfile)
    disp = Display((960, 600))
    result.save(disp)
    time.sleep(5)

if __name__ == '__main__':
    workdir = '/path/to/pictures/dir'

    origin = os.path.join(workdir, 'origin.png') #1920, 1200
    origin_title = os.path.join(workdir, 'temp/origin_title.png')
    of = os.path.join(workdir, 'temp_result.png')
    #match_img(shop_phy, shop_phy_title, outfile=of)
    match_img(origin, origin_title, outfile=of, thr=8, med='CCOEFF_NORM')

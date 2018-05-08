#!/usr/bin/env python3
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import cv2
import itertools

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return d

def min_nonzero(vec):
    try:
        return min([(d,x) for (d,x) in vec if d > 0])
    except Exception as e:
        return min(vec)

def smooth_but_preserve_corners(path):
    path = path_sort( path )
    newpath = [ path[0] ]
    t = 0
    for p in path:
        if abs(p[0] - newpath[-1][0]) < t or abs(p[1]-newpath[-1][1])< t:
            print( '.', end = '' )
            continue
        newpath.append( p )
    print('')
    return newpath

def path_sort( path ):
    newpath = [ min(path) ]
    path.pop(0)
    while path:
        near, nearI = min_nonzero([ (dist(newpath[-1], x), i) for i, x in enumerate(path)])
        newpath.append(path[nearI])
        path.pop(nearI)
    return newpath

def find_corners( img ):
    corners = cv2.goodFeaturesToTrack(img, 1000, 0.2, 1 )
    new = np.zeros_like(img)
    for c in corners:
        for y, x in c:
            new[int(x),int(y)] = 255
    return corners, new

def find_contours( img ):
    #  thres = cv2.Canny(img, 20, 100 )
    ret, thres = cv2.threshold( img, 100, 255, 0 )
    #  im2, cnts, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    im2, cnts, hierarchy = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    new = np.zeros_like(img)
    goodCnts = [ ]
    for cnt in cnts:
        #  goodCnts.append( cv2.convexHull(cnt) )
        goodCnts.append( cnt )
    new = cv2.drawContours(new, goodCnts, -1, 255)
    return goodCnts, new

def main( ):
    img = cv2.imread( './logo.png', 0 )
    img1 = cv2.bilateralFilter(img, 9, 75, 75)
    #  corners, new = find_corners(img1)
    cnts, new = find_contours(img1)

    for l, cnt in enumerate(cnts):
        path = [ tuple(x[0]) for x in cnt ]
        with open('path%d.txt' % l, 'w' ) as f:
            for x, y in path: #smooth_but_preserve_corners(path):
                new[y,x]=l
                f.write('%g %g\n' % (x,-y))
        print('Wrote labeled path to path%d.txt' % l)
    cv2.imwrite( 'logo.jpg', np.vstack((img1,new)))

if __name__ == '__main__':
    main()


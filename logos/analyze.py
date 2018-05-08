#!/usr/bin/env python3
"""analyze.py: 

"""
    
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
    for p in path[1:]:
        if abs(p[0] - newpath[-1][0]) < t or abs(p[1]-newpath[-1][1])< t:
            print( '.', end = '' )
            continue
        newpath.append( p )
    print('')
    return newpath

def path_sort( path ):
    newpath = [ path[0] ]
    path.pop(0)
    while path:
        near, nearI = min_nonzero([ (dist(newpath[-1], x), i) for i, x in enumerate(path)])
        newpath.append(path[nearI])
        path.pop(nearI)
    return newpath

def main( ):
    img = cv2.imread( './logo.png', 0 )
    img = cv2.bilateralFilter(img, 9, 75, 75)
    img1 = cv2.Canny( img, 50, 200 )
    n, temp = cv2.connectedComponents(img1, 4)
    new = np.zeros_like(temp)

    for l in range(1,int(temp.max())+1):
        p1 = np.where( temp == l )
        with open('path%d.txt' % l, 'w' ) as f:
            for x, y in smooth_but_preserve_corners(list(zip(*p1))):
                new[x,y]=10*l
                f.write('%g %g\n' % (y,-x))
        print('Wrote labeled path to path%d.txt' % l)
    cv2.imwrite( 'logo.jpg', np.vstack((img1,new)))

if __name__ == '__main__':
    main()


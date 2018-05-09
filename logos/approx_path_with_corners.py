"""approx_path_with_corners.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import numpy as np
import math
import cv2

scale_ = 100

def dist(p1, p2):
    a, b = p1
    c, d = p2 
    return ((a-c)**2 + (b-d)**2)**0.5

def atan(y, x):
    if x == 0:
        return math.pi/2.0
    else:
        return math.atan(y/x)

def angle_three_points(pleft, p0, pright):
    # p2 is the where we are computing angle
    a = dist(p0, pleft)
    b = dist(p0, pright)
    c = dist(pleft, pright)
    k = (a**2+b**2-c**2)/(2*a*b)
    return math.acos(min(1, max(k,-1)))

def scale(p):
    return (int(p[0]*scale_), int(p[1]*scale_))

def process( path ):
    # Assumes that path are sorted.
    path = np.array(path)
    newpath = path[:]
    for j in range(20):
        for i, post in enumerate(newpath[2:]):
            prev, cur = newpath[i], newpath[i+1]
            theta = angle_three_points(prev, cur, post )
            if theta < 1.01 * math.pi /2 :
                print( 'v', end = '' )
                continue
            newcur = (prev[0]+post[0])/2.0, (prev[1]+post[1])/2.0
            newpath[i+1] = newcur
    return newpath

def main():
    infile = sys.argv[1]
    path = np.loadtxt( infile ) 
    x, y = zip(*path)
    xmin, ymin = min(x), min(y)
    path = [ (a-xmin, b-ymin) for a, b in path ]

    newpath = process(path)
    a,b = np.min(path), np.max(path)
    d = int(scale_*(b-a))

    img1 =  np.zeros( shape=(d+1, d+1) )
    for p in path:
        p = (p[1], p[0])
        img1 = cv2.circle( img1, scale(p), 3, 200, 1 )

    for a, b in zip(newpath, newpath[1:]):
        p1 = scale(a)
        p2 = scale(b)
        img1 = cv2.line( img1, p1, p2, 255, 2)
    
    cv2.imwrite( '%s.png' % infile, img1 )

if __name__ == '__main__':
    main()


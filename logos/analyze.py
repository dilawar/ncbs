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

def preprocess(path):
    path = path_sort( path )
    newpath = [ path[0] ]
    for p in path[1:]:
        newpath.append( p )
    return newpath

def path_sort( path ):
    newpath = [ path[0] ]
    path.pop(0)
    while path:
        near, nearI = min_nonzero([ (dist(newpath[-1], x), i) for i, x in enumerate(path)])
        newpath.append(path[nearI])
        path.pop(nearI)
    print( newpath )
    return newpath

def find_corners( img ):
    corners = cv2.goodFeaturesToTrack(img, 1000, 0.5, 1 )
    new = np.zeros_like(img)
    for c in corners:
        for y, x in c:
            new[int(x),int(y)] = 255
    return corners, new

def main( ):
    img = cv2.imread( './logo.png', 0 )

    # Find corners and keep them. They are usually lost when other operations
    # are performed.
    corners, new = find_corners( img )

    img = cv2.bilateralFilter(img, 9, 75, 75)
    thres = cv2.Canny( img, 100, 200 )

    # Add corners to thres image
    for cs in corners:
        for x, y in cs:
            thres[int(y),int(x)] = thres.max()

    # Compute connected components.
    n, temp = cv2.connectedComponents(thres, 8)
    new = np.zeros_like(temp)

    for l in range(1,int(temp.max())+1):
        p1 = np.where( temp == l )
        with open('path%d.txt' % l, 'w' ) as f:
            path = preprocess(list(zip(*p1)))
            for x, y in [ path[0], path[-1] ]:
                cv2.putText( new, '%s' % l, (y,x), cv2.FONT_HERSHEY_SIMPLEX, 0.4, 255 )
            for x, y in path:
                new[x,y]=20*l
                f.write('%g %g\n' % (y,-x))

        print('Wrote labeled path to path%d.txt' % l)
    cv2.imwrite( 'connected.png', np.vstack((thres,new)))

if __name__ == '__main__':
    main()


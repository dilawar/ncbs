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

def find_paths(edges):
    paths = [ ]
    while True:
        pmin, pmax, minL, start = cv2.minMaxLoc(edges)
        if pmax == 0:
            break
        path = [start]
        while True:
            x, y = path[-1]
            edges[y,x]=0
            connected = False
            for i, j in itertools.product([-1,1], repeat=2):
                v = edges[y+j,x+i]
                if v == pmax:
                    path.append((x+i,y+j))
                    edges[y+j,x+i] = 0
                    connected = True
            if not connected:
                break
        paths.append(path)
    return paths

def main( ):
    img = cv2.imread( './logo.png', 0 )
    img1 = cv2.Canny( img, 50, 200 )
    n, temp = cv2.connectedComponents(img1, 8)
    new = np.zeros_like(temp)

    for l in range(1,int(temp.max())+1):
        p1 = np.where( temp == l )
        with open('path%d.txt' % l, 'w' ) as f:
            for x, y in zip(*p1):
                new[x,y]=10*l
                f.write('%d %d\n' % (x,y))
        print('Wrote labeled path to path%d.txt' % l)
    cv2.imwrite( 'logo.jpg', np.vstack((img1,new)))

if __name__ == '__main__':
    main()


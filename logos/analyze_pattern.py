#!/usr/bin/env python3
"""analyze_pattern.py: 

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
import cv2 as cv

def main():
    pat = cv.imread( './pattern.png', 0 )
    pat = cv.resize( pat, None, fx=2, fy=2)

    ret, thresh = cv.threshold(pat, 200, 255, 0)
    im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    res = np.zeros_like(pat)
    for i, cnt in enumerate(contours):
        if len(cnt) < 10:
            print( 'c', end='')
        
        #  res = cv.drawContours(res, cnt, -1, 255 )
        #  cnt = cv.convexHull( cnt )
        epsilon = 0.0001*cv.arcLength(cnt,True)
        cnt = cv.approxPolyDP(cnt,epsilon,True)
        data = [ x[0] for x in cnt ]
        for (x0,y0), (x1,y1) in zip(data, data[1:]):
            cv.line(res, (x0,y0), (x1,y1), 255, 1 )
        np.savetxt( 'cnt%s.txt' % i, data )

    cv.imwrite('cnt%s.png' % sys.argv[0], np.vstack((pat,res)))


if __name__ == '__main__':
    main()


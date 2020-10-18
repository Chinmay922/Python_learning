# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:18:47 2020

@author: crath
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
img2 = img.copy()
template = cv2.imread('messi_face.jpg',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    x = cv2.matchTemplate(img,template, method)
    min_val, max_val, mini_loca, maxi_loca = cv2.minMaxLoc(x)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = mini_loca
    else:
        top_left = maxi_loca
    below_right = (top_left[0] + w, top_left[1] + h)
    
    cv2.rectangle(img, top_left, below_right, 255, 2)
    
    plt.subplot(221), plt.imshow(x, cmap = 'gray')
    plt.title('Matched Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(img, cmap = 'gray')   
    plt.title('Detected Points'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)    
    plt.show()
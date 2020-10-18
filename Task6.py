# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 03:53:07 2020

@author: crath
"""
import cv2 
from matplotlib import pyplot as plt 
import matplotlib.image as mpimg

image = mpimg.imread("lena.png")
plt.title('Original Image')
plt.axis('off')
plt.imshow(image)
plt.show()

# Read the image. 
img = cv2.imread('lena.png') 
#plt.imshow(img) 

# Apply bilateral filter
bilat = cv2.bilateralFilter(img, 15, 75, 75)
# Save the output. 
cv2.imwrite('path.jpg', bilat)
 
image2 = mpimg.imread("path.jpg")
plt.title('Filtered Image')
plt.axis('off')
plt.imshow(image2)
plt.show()



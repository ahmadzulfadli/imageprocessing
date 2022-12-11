import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('FaceRecogBlock.png',0)
print (img)

print(img.shape)
print(img.dtype)

plt.imshow(img)
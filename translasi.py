# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:34:24 2024

@author: aurel
"""

import cv2
import numpy as np
img = cv2.imread("C:/Users/Aurel/OneDrive/Pictures/Camera Roll/WIN_20240911_08_49_36_Pro - Salin.jpg")
print(img.shape)

baris, coloms, ghgh = img.shape

MTranslasi = np.float32([[2, 0, 100],[0, 2, 50]])

print(MTranslasi, '\n')

dst = cv2.warpAffine (img, MTranslasi, (coloms, baris))
cv2.imshow("title", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
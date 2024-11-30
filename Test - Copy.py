# memilih warna biru saja pada gambar gambar 
import cv2 # menyertakan library cv2 dari opencv
import numpy as np


img = cv2.imread("module ph.jpg")
cv2.imshow("Original", img)

row, col = img.shape[0:2]

for i in range(row):
    for j in range(col):
        img[i, j] = sum(img[i, j]) * 0.33
    
#gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
#print("img ", img)
#cv2.imshow("Gray", gray)
#print('gray =', gray)
#lowBlue = np.array([30, 10, 10])
#highBlue = np.array([40, 255, 255])

#mask = cv2.inRange (img, lowBlue, highBlue)

#cv2.imshow("img0", img0)
#cv2.imshow("img", img)
#print(img.shape)
#cv2.imshow("img", img)
cv2.imshow("Hasil", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

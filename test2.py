import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img = cv2.imread("module ph.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, BW) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Gray", gray)
cv2.imshow("BW", BW)
cv2.waitKey(0)
cv2.destroyAllWindows()

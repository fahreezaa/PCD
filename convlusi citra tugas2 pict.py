# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 08:26:19 2024

@author: k-ruko
"""

#G64160017
import numpy as np
import cv2

image1 = cv2.imread("C:/Users/ejaau/OneDrive/Dokumen/SEMESTER 5/CITRA DIGITAL/kucing.png",0)#membaca posisi direktori dari image1 
#cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
image2= cv2.imread("C:/Users/ejaau/OneDrive/Dokumen/SEMESTER 5/CITRA DIGITAL/kucing.png",0) #membaca posisi direktori dari image2

#konvolusi manual
def konvolusi(image, kernel):
    row,col= image.shape
    mrow,mcol=kernel.shape
    h =int(mrow/2)

    canvas = np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if i==0 or i==row-1 or j==col-1:
                canvas.itemset((i,j),0)
            else:
                imgsum=0
                for k in range (-h, mrow-h):
                    for l in range (-h, mcol-h):
                        res=image[i+k,j+l] * kernel[h+k,h+l]
                        imgsum+=res
                    canvas.itemset((i,j), imgsum)
    return canvas
 
def kernel1(image):
    kernel = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32)
    canvas = konvolusi(image, kernel)
    return canvas

def kernel2(image):
    kernel = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32)
    canvas2 = konvolusi(image, kernel)
    return canvas2

test1=kernel1(image1)
cv2.imshow("gambar1",image1)#menampilkan hasil image1 dalam bentuk asli
cv2.imshow("High pass",test1) #menampilkan hasil image1 dalam bentuk high pass

test2=kernel2(image2)
cv2.imshow("gambar2",image2)#menampilkan hasil image2 dalam bentuk asli
cv2.imshow("low pass",test2)#menampilkan hasil image2 dalam bentuk low pass

print(" gamabr1 ", image1)  #menampilkan hasil kode warna image1 dalam bentuk asli
print(" gambar2 ", image2)#menampilkan hasil kode warna image2 dalam bentuk asli
print(" gambar1 ", image1.shape)#menampilkan resolusi image1 dalam bentuk asli
print(" gambar2 ", image2.shape) #menampilkan resolusi image2 dalam bentuk asli
print(" high filter image1 ", test1.shape)#menampilkan resolusi image1 setelah mengguankan high filter
print(" lowpass image1 ", test1.shape)#menampilkan resolusi image1 setelah mengguankan LOw pass filter
print(" high filter image2 ", test2.shape)#menampilkan resolusi image2 setelah mengguankan high filter
print(" lowpass image2 ", test2.shape)#menampilkan resolusi image2 setelah mengguankan LOw pass filter
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

 Operating System: Windows 10 Home Single Language 64-bit (10.0, Build 19045) (19041.vb_release.191206-1406)
                 Language: English (Regional Setting: English)
      System Manufacturer: HP
             System Model: HP 245 14 inch G9 Notebook PC
                     BIOS: F.12 (type: UEFI)
                Processor: AMD Ryzen 3 5425U with Radeon Graphics          (8 CPUs), ~2.7GHz
                   Memory: 16384MB RAM
      Available OS Memory: 15722MB RAM
                Page File: 4263MB used, 12483MB available
              Windows Dir: C:\Windows
          DirectX Version: DirectX 12
          
          """
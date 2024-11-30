#Color Filtering

bertujuan untuk memproses gambar dengan menambahkan filter warna yang didasarkan pada konsep emosi dan warna dalam teori psikologi emosi, khususnya merujuk pada roda emosi. Berikut adalah penjelasan tentang langkah-langkah dan fungsi yang ada dalam program tersebut.

##Inisialisasi dan Impor Modul
``` python
import numpy as np, cv2 as cv
```

###Modul numpy digunakan untuk manipulasi array, sedangkan cv2 (OpenCV) digunakan untuk pemrosesan gambar, seperti membaca, menampilkan, dan menyimpan gambar.

##Fungsi imageRead(filename)
``` python
def imageRead(filename):
    readFile = open(filename, 'rb')
    img_str = readFile.read()
    readFile.close()
    img = np.array(bytearray(img_str), np.uint8).reshape((480, 480, 3))  # shape height, width, 3
    cv.cvtColor(img, cv.COLOR_BGR2RGB, img)
    return img
```

###Fungsi ini digunakan untuk membaca gambar dari file dengan nama yang diberikan (filename).
- Gambar dibaca dalam format binary (rb), kemudian diubah menjadi array NumPy dengan tipe data uint8.
- Gambar yang dibaca diubah ukurannya menjadi 480x480 piksel dengan 3 saluran warna (BGR), dan kemudian diubah ke format RGB.
- Gambar yang telah diproses kemudian dikembalikan.

##Fungsi showImage(title, image)
``` python
def showImage(title, image):
    cv.namedWindow(title, cv.WINDOW_AUTOSIZE)
    cv.imshow(title, image)
    cv.waitKey(0)
```

###Fungsi ini digunakan untuk menampilkan gambar pada jendela dengan judul title.
Gambar yang diberikan akan ditampilkan menggunakan OpenCV (cv.imshow), dan program akan menunggu sampai tombol ditekan sebelum melanjutkan.


##Kelas ColorFilter
### Kelas ini bertanggung jawab untuk mengatur dan memanipulasi warna gambar sesuai dengan warna target yang diberikan. Kelas ini memiliki beberapa atribut dan metode:

Atribut:
image: Menyimpan gambar yang akan diproses.
targetColor: Menyimpan warna target dalam format HSV.
colorDict: Sebuah dictionary untuk menyimpan warna yang telah ditransformasikan untuk setiap nilai tertentu.

## Metode:
a. Metode set_image(input_image) 

``` python
def set_image(self, input_image):
    self.image = np.copy(inputImage)
```
### Metode ini menyetel gambar yang akan diproses, yaitu salinan dari gambar yang diberikan sebagai parameter.

## b. Metode set_target_color(color)

``` python
def set_target_color(self, color):
    self.targetColor = cv.cvtColor(color, cv.COLOR_BGR2HSV)
    for iii in range(0,256):
        transformColor = np.array([[[ self.targetColor[0,0,0], iii*100/255,self.targetColor[0,0,2] ]]], dtype=np.uint8)
        self.colorDict[iii] = cv.cvtColor(transformColor, cv.COLOR_HSV2RGB)
```

### Fungsi ini mengubah warna target yang diberikan (dalam format BGR) menjadi format HSV menggunakan cv.cvtColor.
Kemudian, untuk setiap nilai antara 0 dan 255, gambar akan diubah ke format HSV yang berbeda, dengan menyesuaikan nilai saturasi (S), dan menghasilkan warna baru.
Setiap warna hasil transformasi disimpan dalam dictionary colorDict.

## c. Metode filter()

``` python
def filter(self):
    for iii in range(0, self.image.shape[0]):
        for jjj in range(0, self.image.shape[1]):
            data = self.image[iii, jjj]
            data[0] = self.colorDict[data[0]][0,0,0]
            data[1] = self.colorDict[data[1]][0,0,1]
            data[2] = self.colorDict[data[2]][0,0,2]
    return self.image
```

### Fungsi ini memproses setiap piksel dalam gambar.
Untuk setiap piksel, setiap komponen warna (R, G, B) dipetakan berdasarkan nilai dalam colorDict.
Dengan cara ini, setiap warna dalam gambar akan dimodifikasi sesuai dengan transformasi warna yang telah ditetapkan sebelumnya.

## 5. Pemrosesan Gambar dan Penampilan

``` python
inputImage = cv.imread('C:/Users/ejaau/OneDrive/Gambar/Rol Kamera/WIN_20241101_14_46_59_Pro.jpg')
colorFilter = ColorFilter()
colorFilter.set_image(inputImage)
colorFilter.set_target_color(np.array([[[0, 0, 224]]], dtype= np.uint8))
output = (0.4*inputImage + 0.6*colorFilter.filter()).astype(np.uint8)
showImage('Output', output)
cv.imwrite("results.jpg", output)
```

### Gambar yang diinginkan dibaca menggunakan cv.imread.
Objek colorFilter dari kelas ColorFilter dibuat dan gambar serta warna target diset menggunakan metode set_image dan set_target_color.
Gambar akhir (output) dihasilkan dengan mencampurkan gambar asli dan gambar yang telah diproses oleh filter warna. Rasio campuran adalah 40% gambar asli dan 60% gambar hasil filter.
Gambar hasil diproses ditampilkan menggunakan showImage dan disimpan sebagai file results.jpg.

## Penjelasan Alur Program:
### Membaca Gambar: Gambar dibaca menggunakan OpenCV.
Setel Warna Target: Program mengubah warna target (yang dapat diubah sesuai emosi) menjadi format HSV untuk memodifikasi gambar.
Pemrosesan Warna: Menggunakan ColorFilter, gambar akan diproses dengan memodifikasi warna berdasarkan target yang telah ditentukan.
Pencampuran Gambar: Gambar asli dicampur dengan gambar yang telah diproses, dengan proporsi tertentu.
Menampilkan dan Menyimpan Gambar: Gambar akhir ditampilkan dan disimpan dalam file.

## Tujuan dari Program:
### Program ini mencoba untuk memberikan efek visual pada gambar berdasarkan warna yang terinspirasi oleh teori roda emosi Plutchik, di mana setiap warna mewakili emosi tertentu. Dengan memanipulasi warna gambar berdasarkan teori tersebut, program ini dapat menciptakan efek visual yang menambah kedalaman emosional pada gambar yang ditampilkan.

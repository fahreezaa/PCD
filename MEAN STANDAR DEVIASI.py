# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:21:26 2024

@author: ejaau
"""

import cv2                     # Mengimpor pustaka OpenCV untuk pemrosesan citra
import numpy as np             # Mengimpor pustaka NumPy untuk operasi numerik

def calculate_mean(image):
    """
    Fungsi untuk menghitung Mean dari citra.
    Mean adalah rata-rata nilai pixel dari citra.
    """
    mean_value = np.mean(image)  # Menghitung rata-rata dari semua pixel citra
    return mean_value             # Mengembalikan nilai mean

def calculate_variance(image):
    """
    Fungsi untuk menghitung Variance dari citra.
    Variance mengukur seberapa jauh nilai pixel dari rata-ratanya.
    """
    mean_value = calculate_mean(image)  # Menghitung mean citra
    variance_value = np.mean((image - mean_value) ** 2)  # Menghitung varians
    return variance_value                 # Mengembalikan nilai variance

def calculate_covariance(image1, image2):
    """
    Fungsi untuk menghitung Covariance antara dua citra.
    Covariance mengukur bagaimana dua citra berhubungan satu sama lain.
    """
    mean1 = calculate_mean(image1)   # Menghitung mean citra pertama
    mean2 = calculate_mean(image2)   # Menghitung mean citra kedua

    # Menghitung covariance
    covariance_value = np.mean((image1 - mean1) * (image2 - mean2))
    return covariance_value           # Mengembalikan nilai covariance

# Membaca citra dari file
image1 = cv2.imread('C:/Users/ejaau/OneDrive/Dokumen/SEMESTER 5/CITRA DIGITAL/x.jpeg', cv2.IMREAD_GRAYSCALE)  # Mengimpor citra pertama dalam skala abu-abu
image2 = cv2.imread('C:/Users/ejaau/OneDrive/Dokumen/SEMESTER 5/CITRA DIGITAL/x.jpeg', cv2.IMREAD_GRAYSCALE)  # Mengimpor citra kedua dalam skala abu-abu

# Menghitung Mean, Variance, dan Covariance
mean1 = calculate_mean(image1)              # Menghitung mean citra pertama
variance1 = calculate_variance(image1)      # Menghitung variance citra pertama
mean2 = calculate_mean(image2)              # Menghitung mean citra kedua
variance2 = calculate_variance(image2)      # Menghitung variance citra kedua
covariance = calculate_covariance(image1, image2)  # Menghitung covariance antara kedua citra

# Menampilkan hasil
print(f'Mean of Image 1: {mean1}')          # Mencetak nilai mean citra pertama
print(f'Variance of Image 1: {variance1}')  # Mencetak nilai variance citra pertama
print(f'Mean of Image 2: {mean2}')          # Mencetak nilai mean citra kedua
print(f'Variance of Image 2: {variance2}')  # Mencetak nilai variance citra kedua
print(f'Covariance between Image 1 and Image 2: {covariance}')  # Mencetak nilai covariance

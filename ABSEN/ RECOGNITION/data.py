# FILE INI BERFUNGSI UNTUK MENGUBAH FORMAT FOTO .JPG YANG ADA DI DIREKTORI DATA MENJADI FORMAT .XML

import cv2 
import os
import numpy as np


recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #mengimpor file model

dataset_path = "/home/fadlann/LINUX/vscode/PYTHONN/opencv/data" #memasukkan path file yang akan dituju

def get_images(dataset_path): #fungsi untuk memproses data
    face_samples = [] #array kosong untuk menampung data
    for file in os.listdir(dataset_path): #mencari data menggunakan import os
        if file.endswith("jpg"): #mencari data dengan ekstensi jpg
            img_path = os.path.join(dataset_path, file) #mencocokkan data dengan path
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) #membaca data
            imgr=cv2.resize(img, (200, 200))  #mengubah ukuran data
            face_samples.append(imgr) #memasukkan data ke array kosong
    return face_samples #kembalikan fungsi


faces = get_images("data") #panggil fungsi
labels = np.arange(len(faces)) #label untuk menghitung panjang data face
recognizer.train(faces, labels) #membuat file baru 
recognizer.save("/home/fadlann/LINUX/vscode/PYTHONN/opencv/data/traine.xml") #membuat file tujuan 
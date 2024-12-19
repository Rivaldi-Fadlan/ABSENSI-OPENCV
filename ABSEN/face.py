#FILE INI BERFUNGSI UNTUK MEMBUKA KAMERA DAN MEMPROSES DATA YANG ADA DI DIREKTORI DATA (FILE UTAMA)

import cv2 #import library cv
import time 
from services import database #import database file     

recognizer = cv2.face.LBPHFaceRecognizer_create() #fungsi untuk membuat alat pencocokan
try:
    recognizer.read("/home/fadlann/LINUX/vscode/PYTHONN/ABSEN/data/traine.xml") #membaca path dataset
    print("FACE RECOGNITION ON \U0001F923\U0001F923\U0001F923") #pesan jika kamera mendeteksi
except cv2.error as e:
    print(f"KAMERA TIDAK DAPAT MENDETEKSI : {e}") #pesan jika kamera tida mendeteksi
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #impor modul haarcascade_face
eye_ref = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml") #impor modul haarcascade_eye
cam = cv2.VideoCapture(0) #membuka kamera

waktu_kedip_akhir= None  
deteksi_mata = False  
while True:
    ret, frame = cam.read() #membaca kamera
    if not ret:
        print("KAMERA TIDAK TERBUKA  \U0001F923") #kesalahan saat membuka kamera
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #membuat format file dataset menjad abu,agar memperkecil kerja sistem
    faces = face_cascade.detectMultiScale(gray, 1.1, 10) #mencocokan file dateset dengan gambar di kamera
    eyes = eye_ref.detectMultiScale(gray, 1.1, 10)

    for (x, y, w, h) in faces:
        face_img = cv2.resize(gray[y:y + h, x:x + w], (200, 200))#menetapkan ukuran file
        try:
            label, kemiripan = recognizer.predict(face_img)#memprediksi kemiripan dataset dengan gambar di kamera
            if label == 0:
                label = "FADLANN" #mengubah id menjadi sebuah string 
            if label == 1:
                label = "ABAHH"
            
            label_text = f"{label} {round(100 - kemiripan, 2)}%"
            warna = (0, 255, 0) if kemiripan < 50 else (255, 0, 0) #logika untuk membuat kecocokan , jika < 50 % frame warna hijau
            cv2.putText(frame, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, warna, 2) #membuat teks nama diatas frame face
            cv2.rectangle(frame, (x, y), (x + w, y + h), warna, 2)

           
            if len(eyes) > 0: 
                deteksi_mata = True #membuat validasi agar jika mata berkedip maka akan dijalankan
            else:  
                if deteksi_mata:  
                    catatan_waktu = time.time()
                    if waktu_kedip_akhir is None or catatan_waktu - waktu_kedip_akhir > 1:   
                        waktu_kedip_akhir = catatan_waktu
                        cv2.putText(frame, "Kedip terdeteksi", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        NAMA = label
                        ABSEN = "HADIR"
                        result = database.absen(NAMA, ABSEN) #memasukkan variabel absen ke dalam database
                        print(result)

                deteksi_mata = False  

        
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

        except cv2.error as e:
            print(f"Error : {e}") #pesan kesalahan

    cv2.imshow("PSYCHO RECOGNITION", frame) #judul diatas pop up kamera

    if cv2.waitKey(1) & 0xFF == ord('q'): #jika user menekan tobol q maka program selesai
        break

cam.release()#menghentikan / menutup kamera
cv2.destroyAllWindows() # menutup semua tampilan 


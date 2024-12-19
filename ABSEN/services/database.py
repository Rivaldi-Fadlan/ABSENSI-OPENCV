#FILE INI BERFUNGSI UNTUK MENAMBAHKAN DATABASE KEDALAM FILE UTAMA AGAR DATA DARI FILE UTAMA TERHUBUNG KE DATABASE

import mysql.connector #mengimpor library python to sql

databases= mysql.connector.connect( #navigasi ke  sistem database
    host = 'localhost', #beri nama host yang terpakai
    user = 'username_database', #masukkan username mysql
    password = 'password_database', #masukkan password mysql
    database = "nama_database" #masukkan nama database
)

def absen (NAMA,ABSEN):
    cursor = databases.cursor()
    insert = cursor.execute("INSERT INTO ABSEN_JANUARI (NAMA,ABSEN) VALUES (%s,%s)",(NAMA,ABSEN)) #tulis query
    databases.commit() #meminta inputan untuk dimasukkan ke dala query
    return insert #kembalikan nilai insert


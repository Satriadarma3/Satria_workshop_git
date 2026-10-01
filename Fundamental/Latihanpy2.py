print("masukan nilai rata rata")
K =int(input("ada berapa data yang mau di masukan = "))#variabel K menampung sebuah input user
total = 0
Nilai = ()# variabel NIlai berisi kosong



for i in range(K):#melakukan peloopingan sampai varibel K
    angka = float(input(f"Masukkan data ke-{i+1}: "))# nilai angka memuat sebuah semua input user
    total += angka

def Rata():# sebuah prosedur yang menghitung nilai rata rata
    print("Rata-RAta =" ,total/ K)

Rata()   
    
    

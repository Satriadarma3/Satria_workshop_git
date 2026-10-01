print("_____coba masukan nilai untuk mencari faktorial___")
nilai = int(input("masukan sebuah bilangan = "))

def faktorial(nilai):  # ini adalah fungsi yang mencari nilai faktorial
    J = 1 #sebagai nilai pertama di faktorial
    for i in range(1, nilai + 1): # peloopingan 
        J *= i   #nilai pertambahan 
    return J  #menampilan hasil akhir dari sebuah faltorial

if nilai < 0: # pengecekan sebuah variabel nilai apakah kurang dari 0
    print("Faktorial tidak terdefinisi untuk bilangan negatif")
else:
    print("faktorial dari", nilai, "adalah", faktorial(nilai))
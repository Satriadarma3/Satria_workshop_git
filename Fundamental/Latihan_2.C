#include <stdio.h>

int K;
float Angka;
float total = 0;

void Rata() {//sebuah prosedur yang menghitung nilai rata rata
    printf("Rata-rata : %.2f\n", total / K);
}
int main() {
    printf("Masukkan Nilai Rata-Rata\n");
    printf("Ada berapa data yang mau dimasukkan = ");
    scanf("%d", &K);//variabel K menampung sebuah input user

    for (int i = 0; i < K; i++) {//melakukan peloopingan sampai varibel K
        printf("Masukkan data ke-%d : ", i + 1);
        scanf("%f", &Angka);//nilai angka memuat sebuah semua input user
        total += Angka;
    }
    Rata();
    return 0;
}
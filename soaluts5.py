"""
Nama    : Vina Nur Nisa
NIM     : 2408200
Kelas   : RPL 1B

SOAL UTS 5
"""


bilangan = 0
jumlah_nilai_membesar = 0

angka = int(input("Input bilangan : "))
angka2 = angka

while bilangan < 3:
    angka = int(input("Input bilangan : "))
    if angka > angka2:
        angka2 = angka
        bilangan = 0
        jumlah_nilai_membesar += angka
    else:
        angka2 = angka
        bilangan += 1

print(f"Hasil penjumlahan nilai yang membesar : {jumlah_nilai_membesar}")
    
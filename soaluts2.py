"""
Nama    : Vina Nur Nisa
NIM     : 2408200
Kelas   : RPL 1B

SOAL UTS 2
"""

bilangan = 0
genap = 0
ganjil = 0

while bilangan >= 0:
    bilangan = int(input("Input bilangan : "))
    if bilangan < 0:
        break
    if bilangan % 2 == 0:
        genap += bilangan
    else:
        ganjil += bilangan

print(f"Jumlah bilangan genap : {genap}")
print(f"Jumlah bilangan ganjil : {ganjil}")






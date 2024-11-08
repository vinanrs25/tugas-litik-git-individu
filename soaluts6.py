"""
Nama    : Vina Nur Nisa
NIM     : 2408200
Kelas   : RPL 1B

SOAL UTS 6
"""

n = int(input("Masukkan nilai N = "))
m = 0
prima = 0

while n > 0:
    bilangan = int(input("Masukkan bilangan = "))
    prima = 0
    m += bilangan
    while m > 0:
        i = 2
        if bilangan % i == 0:
            prima += 1
            m += bilangan
            break
        else:
            i += 1
        if bilangan < i:
            break
    n -= 1
    
    print("Jumlah Bilangan Prima ")

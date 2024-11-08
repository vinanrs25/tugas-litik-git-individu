"""
Nama    : Vina Nur Nisa
NIM     : 2408200
Kelas   : RPL 1B

SOAL UTS 4
"""

nim = int(input("Input 3 digit NIM terakhir : "))

if nim % 2 == 0:
    if 1 <= nim <= 50:
        print("Silakan masuk ke kelas K2")
    elif 51 <= nim <= 100:
        print("Silakan masuk ke kelas K4")
    elif 101 <= nim <= 150:
        print("Silakan masuk ke kelas K6")
    else:
        print("Silakan masuk ke kelas K8")
else:
    if 1 <= nim <= 50:
        print("Silakan masuk ke kelas K1")
    elif 51 <= nim <= 100:
        print("Silakan masuk ke kelas K3")
    elif 101 <= nim <= 150:
        print("Silakan masuk ke kelas K5")
    else:
        print("Silakan masuk ke kelas K7")
    
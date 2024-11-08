"""
Nama    : Vina Nur Nisa
NIM     : 2408200
Kelas   : RPL 1B

SOAL UTS 3
"""

bebek = int(input("Berapa jumlah bebek kecil yang mau kamu hitung? "))

while bebek > 0:
    print(f"{bebek} bebek kecil berenang")
    print("Menyusuri sungai yang deras")
    print("Induknya mencari kwek kwek kwek")
    bebek -= 1
    if bebek > 0:
        print(f"Hanya {bebek} ekor yang pulang")
    else:
        print("Dan semua bebek kecil pulang, aha!")
"""
Nama    : Vina Nur Nisa
NIM     : 2408200
Kelas   : RPL 1B

SOAL UTS 1
"""

kesempatan_login = 3

print("Silahkan login")


while kesempatan_login > 0:
    username = input("Username : ")
    password = input("Password : ")
    if username == "loginUTS" and password == "rpl2024":
        print("Selamat datang di aplikasi Prodi RPL.")
        break
    else:
        kesempatan_login -= 1
        if kesempatan_login > 0:
            print(f"Login salah! Kesempatan anda {kesempatan_login}x kali lagi.")
        else:
            print("Anda tidak diperkenankan mengakses aplikasi ini.")
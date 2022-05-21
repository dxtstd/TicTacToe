from os import system
from time import sleep as s

clear = lambda: system('clear')

x = "❌"
o = "⭕"
one = "1️⃣"
two = "2️⃣"
three = "3️⃣"
four = "4️⃣"
five = "5️⃣"
six = "6️⃣"
seven = "7️⃣"
eight = "8️⃣"
nine = "9️⃣"

start = ""

credit = """
           ==CREDIT==
Dibuat Oleh: Denta Fahriansyah Triyono

Sosial Media:
  Facebook: Denta Fahriansyah Triyono
  WhatsApp: +6288804280094
  Telegram: +6288804280094
  Instagram: @denta.ft
  
Saya Membuat Ini Seharian :>
Have Fun :)

Python 3.9.5
Code Editor
Termux
            ===END===
"""
clear()
print("Selamat Datang Di Permainan TicTacToe")
while(not start == "Y"):
    start = input("Lanjutkan(Y) Keluar(N) Credits(C) : ").upper()
    if start == "N":
        quit()
    elif start == "C":
        print(credit)
        while(not start == "Y"):
            start = input("Lanjutkan(Y) Keluar(N) : ").upper()
            if start == "N":
                exit()
            else:
                print("Pilihlah Salah Satu!")
    elif start == "Y":
        pass
    else:
        print("Pilihlah Salah Satu!")

inputnama1 = "Nama Player1" + " : "
inputnama2 = "Nama Player2" + " : "
clear()
print("Sebelum Mulai Mainnya. Mari, Mengisi Nama Dulu")
nama_player1 = input(inputnama1)
if nama_player1 == None:
    nama_player1 = "Player1"
    print("Oke Aku Akan Menamai Mu Player1")
nama_player2 = input(inputnama2)
if nama_player2 == None:
    nama_player2 = "Player2"
    print("Oke Aku Akan Menamai Mu Player2")
clear()
print("\nMari Kita Mulai!\n")

xxx = '''TicTacToe
1️⃣2️⃣3️⃣
4️⃣5️⃣6️⃣
7️⃣8️⃣9️⃣
'''

giliran_player1 = "Giliran Player1" + " : "
giliran_player2 = "Giliran Player2" + " : "

menang = "Tidak"
player_X = "Giliran"
player_O = "Bukan Giliran"

while(menang == "Tidak"):
    xxx = f"\nTicTacToe\n{one}{two}{three}\n{four}{five}{six}\n{seven}{eight}{nine}\n"
        
    if player_X == "Giliran":
        clear()
        print(xxx)
        print(f"Nama P1 : {nama_player1}\nNama P2 : {nama_player2}\n")
        jawaban = input(giliran_player1)
        if jawaban == "1":
            if not one == "1️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)

            else:
                one = one.replace("1️⃣", "❌")
                player_X = player_X.replace("Giliran", "Bukan Giliran")
                player_O = player_O.replace("Bukan Giliran", "Giliran")
        elif jawaban == "2":
            if not two == "2️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                two = two.replace("2️⃣", "❌")
                player_X = player_X.replace("Giliran", "Bukan Giliran")
                player_O = player_O.replace("Bukan Giliran", "Giliran")
        elif jawaban == "3":
            if not three == "3️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                three = three.replace("3️⃣", "❌")
                player_X = player_X.replace("Giliran", "Bukan Giliran")
                player_O = player_O.replace("Bukan Giliran", "Giliran")
        elif jawaban == "4":
            if not four == "4️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                four = four.replace("4️⃣", "❌")
                player_X = player_X.replace("Giliran", "Bukan Giliran")
                player_O = player_O.replace("Bukan Giliran", "Giliran")
        elif jawaban == "5":
            if not five == "5️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                five = five.replace("5️⃣", "❌")
                player_X = player_X.replace("Giliran", "Bukan Giliran")
                player_O = player_O.replace("Bukan Giliran", "Giliran")
        elif jawaban == "6":
            if not six == "6️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                six = six.replace("6️⃣", "❌")
                player_X = player_X.replace("Giliran", "Bukan Giliran")
                player_O = player_O.replace("Bukan Giliran", "Giliran")
        elif jawaban == "7":
            if not seven == "7️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                seven = seven.replace("7️⃣", "❌")
                player_X = player_X.replace("Giliran", "Bukan Giliran")
                player_O = player_O.replace("Bukan Giliran", "Giliran")
        elif jawaban == "8":
            if not eight == "8️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                eight = eight.replace("8️⃣", "❌")
                player_X = player_X.replace("Giliran", "Bukan Giliran")
                player_O = player_O.replace("Bukan Giliran", "Giliran")
        elif jawaban == "9":
            if not nine == "9️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                nine = nine.replace("9️⃣", "❌")
                player_X = player_X.replace("Giliran", "Bukan Giliran")
                player_O = player_O.replace("Bukan Giliran", "Giliran")
        else:
            print("Masukkan Angka Yang Benar! (1-9)")
            s(0.5)

    elif player_O == "Giliran":
        clear()
        print(xxx)
        print(f"Nama P1 : {nama_player1}\nNama P2 : {nama_player2}\n")
        jawaban = input(giliran_player2)
        if jawaban == "1":
            if not one == "1️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                one = one.replace("1️⃣", "⭕")
                player_O = player_O.replace("Giliran", "Bukan Giliran")
                player_X = player_X.replace("Bukan Giliran", "Giliran")
        elif jawaban == "2":
            if not two == "2️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                two = two.replace("2️⃣", "⭕")
                player_O = player_O.replace("Giliran", "Bukan Giliran")
                player_X = player_X.replace("Bukan Giliran", "Giliran")
        elif jawaban == "3":
            if not three == "3️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                three = three.replace("3️⃣", "⭕")
                player_O = player_O.replace("Giliran", "Bukan Giliran")
                player_X = player_X.replace("Bukan Giliran", "Giliran")
        elif jawaban == "4":
            if not four == "4️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                four = four.replace("4️⃣", "⭕")
                player_O = player_O.replace("Giliran", "Bukan Giliran")
                player_X = player_X.replace("Bukan Giliran", "Giliran")
        elif jawaban == "5":
            if not five == "5️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                five = five.replace("5️⃣", "⭕")
                player_O = player_O.replace("Giliran", "Bukan Giliran")
                player_X = player_X.replace("Bukan Giliran", "Giliran")
        elif jawaban == "6":
            if not six == "6️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                six = six.replace("6️⃣", "⭕")
                player_O = player_O.replace("Giliran", "Bukan Giliran")
                player_X = player_X.replace("Bukan Giliran", "Giliran")
        elif jawaban == "7":
            if not seven == "7️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                seven = seven.replace("7️⃣", "⭕")
                player_O = player_O.replace("Giliran", "Bukan Giliran")
                player_X = player_X.replace("Bukan Giliran", "Giliran")
        elif jawaban == "8":
            if not eight == "8️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                eight = eight.replace("8️⃣", "⭕")
                player_O = player_O.replace("Giliran", "Bukan Giliran")
                player_X = player_X.replace("Bukan Giliran", "Giliran")
        elif jawaban == "9":
            if not nine == "9️⃣":
                print("Silahkan Masukkan Angka Lain, Angka Ini Telah Digunakan!")
                s(0.5)
            else:
                nine = nine.replace("9️⃣", "⭕")
                player_O = player_O.replace("Giliran", "Bukan Giliran")
                player_X = player_X.replace("Bukan Giliran", "Giliran")
        else:
            print("Masukkan Angka Yang Benar! (1-9)")
            s(0.5)

    else:
        None
    xxx = f"\nTicTacToe\n{one}{two}{three}\n{four}{five}{six}\n{seven}{eight}{nine}\n"       
    if one == x and two == x and three == x:
        menang = menang.replace("Tidak", "Menang")
        player_X = player_X.replace("Bukan Giliran", "Menang")
    elif four == x and five == x and six == x:
        menang = menang.replace("Tidak", "Menang")
        player_X = player_X.replace("Bukan Giliran", "Menang")
    elif seven == x and eight == x and nine == x:
        menang = menang.replace("Tidak", "Menang")
        player_X = player_X.replace("Bukan Giliran", "Menang")
    elif one == x and four == x and seven == x:
        menang = menang.replace("Tidak", "Menang")
        player_X = player_X.replace("Bukan Giliran", "Menang")
    elif two == x and five == x and eight == x:
        menang = menang.replace("Tidak", "Menang")
        player_X = player_X.replace("Bukan Giliran", "Menang")
    elif three == x and six == x and nine == x:
        menang = menang.replace("Tidak", "Menang")
        player_X = player_X.replace("Bukan Giliran", "Menang")
    elif one == x and five == x and nine == x:
        menang = menang.replace("Tidak", "Menang")
        player_X = player_X.replace("Bukan Giliran", "Menang")
    elif three == x and five == x and seven == x:
        menang = menang.replace("Tidak", "Menang")
        player_X = player_X.replace("Bukan Giliran", "Menang")
    else:
        None
    if one == o and two == o and three == o:
        menang = menang.replace("Tidak", "Menang")
        player_O = player_O.replace("Bukan Giliran", "Menang")
    elif four == o and five == o and six == o:
        menang = menang.replace("Tidak", "Menang")
        player_O = player_O.replace("Bukan Giliran", "Menang")
    elif seven == o and eight == o and nine == o:
        menang = menang.replace("Tidak", "Menang")
        player_O = player_O.replace("Bukan Giliran", "Menang")
    elif one == o and four == o and seven == o:
        menang = menang.replace("Tidak", "Menang")
        player_O = player_O.replace("Bukan Giliran", "Menang")
    elif two == o and five == o and eight == o:
        menang = menang.replace("Tidak", "Menang")
        player_O = player_O.replace("Bukan Giliran", "Menang")
    elif three == o and six == o and nine == o:
        menang = menang.replace("Tidak", "Menang")
        player_O = player_O.replace("Bukan Giliran", "Menang")
    elif one == o and five == o and nine == o:
        menang = menang.replace("Tidak", "Menang")
        player_O = player_O.replace("Bukan Giliran", "Menang")
    elif three == o and five == o and seven == o:
        menang = menang.replace("Tidak", "Menang")
        player_O = player_O.replace("Bukan Giliran", "Menang")
    else:
        None

    if not ((one == "1️⃣" or two == "2️⃣" or three == "3️⃣" or four == "4️⃣" or five == "5️⃣" or six == "6️⃣" or seven == "7️⃣" or eight == "8️⃣" or nine == "9️⃣" ) and not menang == "Menang"):
      seri = True
    else:
      seri = False

    xxx = f"\nTicTacToe\n{one}{two}{three}\n{four}{five}{six}\n{seven}{eight}{nine}\n"  

    if menang == "Menang":
        clear()
        print(xxx)
        print(f"Nama P1 : {nama_player1}\nNama P2 : {nama_player2}\n")
        if player_X == "Menang":
            print(f"\nSelamat {nama_player1} Kamu Menang!")
        if player_O == "Menang":
            print(f"\nSelamat {nama_player2} Kamu Menang!")
        break

    if seri:
      clear()
      print(xxx)
      print(f"Nama P1 : {nama_player1}\nNama P2 : {nama_player2}\n")
      print("Seri!")
      break

print("Terima Kasih Bermain TicTacToe Python Milik Saya :>")
print("Jika Ingin Main Lagi, Silahkan Jalankan Script Ini Lagi ")
print("Script by Denta FT")

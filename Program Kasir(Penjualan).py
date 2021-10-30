# Program Kasir Sederhana
def menu():
    print('''
    =========================================
         Selamat datang di Korean Cafe
    =========================================
      Silahkan pilih Menu yang Anda inginkan
    -----------------------------------------
      Daftar Menu Makanan:
      [1] Tteokbokki       - Rp 15.000
      [2] Kimbap           - Rp 30.000
      [3] Bibimbap         - Rp 55.000
      [4] Jajangmyeon      - Rp 35.000
      [5] Bulgogi          - Rp 150.000
    =========================================
      Daftar Menu Minuman :
      [6] Banana Milk      - Rp 15.000
      [7] Yuja Cha         - Rp 10.000
      [8] Ice Americano    - Rp 25.000
      [9] Daechu Tea       - Rp 10.000
      [10] Soju             - Rp 95.000
    =========================================
    ''')
Hari = []
Pesanan = []
Total = []

def Tteokbokki():
  Nama_pesanan1 = 'Tteokbokki'
  Pesanan.append(Nama_pesanan1)
  a = int(input('Jumlah porsi yang ingin Anda pesan: '))
  Harga_Tteokbokki = int(a * 15000)
  Total.append(Harga_Tteokbokki)

def Kimbap():
  Nama_pesanan2 = 'Kimbap'
  Pesanan.append(Nama_pesanan2)
  b = int(input('Jumlah porsi yang ingin Anda pesan: '))
  Harga_Kimbap = int(b * 30000)
  Total.append(Harga_Kimbap)
def Bibimbap():
  Nama_pesanan3 = 'Bibimbap'
  Pesanan.append(Nama_pesanan3)
  c = int(input('Jumlah porsi yang ingin Anda pesan: '))
  Harga_Bibimbap = int(c * 55000)
  Total.append(Harga_Bibimbap)
def Jajangmyeon():
  Nama_pesanan4 = 'Jajangmyeon'
  Pesanan.append(Nama_pesanan4)
  d = int(input('Jumlah porsi yang ingin yang Anda pesan: '))
  Harga_Jajangmyeon = int(d * 35000)
  Total.append(Harga_Jajangmyeon)

def Bulgogi():
  Nama_pesanan5 = 'Bulgogi'
  Pesanan.append(Nama_pesanan5)
  e = int(input('Jumlah porsi yang ingin Anda pesan: '))
  Harga_Bulgogi = int(e * 150000)
  Total.append(Harga_Bulgogi)

def Banana_Milk():
  Nama_pesanan6 = 'Banana Milk'
  Pesanan.append(Nama_pesanan6)
  a = int(input('Jumlah gelas yang ingin Anda pesan: '))
  Harga_BananaMilk = int(a*15000)
  Total.append(Harga_BananaMilk)

def Yuja_Cha():
  Nama_pesanan7 = 'Yuja Cha'
  Pesanan.append(Nama_pesanan7)
  b = int(input('Jumlah gelas yang ingin Anda pesan: '))
  Harga_YujaCha = int(b*10000)
  Total.append(Harga_YujaCha)

def Ice_Americano():
  Nama_pesanan8 = 'Ice Americano'
  Pesanan.append(Nama_pesanan8)
  c = int(input('Jumlah gelas yang ingin Anda pesan: '))
  Harga_IceAmericano = int(c*25000)
  Total.append(Harga_IceAmericano)

def Daechu_Tea():
  Nama_pesanan9 = 'Daechu Tea'
  Pesanan.append(Nama_pesanan9)
  d = int(input('Jumlah gelas yang ingin Anda pesan: '))
  Harga_DaechuTea = int(d*10000)
  Total.append(Harga_DaechuTea)

def Soju():
  Nama_pesanan10 = 'Soju'
  Pesanan.append(Nama_pesanan10)
  e = int(input('Jumlah botol yang ingin Anda pesan: '))
  Harga_Soju = int(e*95000)
  Total.append(Harga_Soju)

def tanya():
  print("\n=========================================")
  tanya = input("Ingin menambah menu lagi? [Y/T] : ")
  print("=========================================")
  if tanya == "Y":
    menu()
    Pilihan()
  elif tanya == "T":
    akhir()
  else:
    print("Pilihan yang anda masukan salah!")
    tanya()

def akhir():
  for harga in Total:
    print("=========================================")
    print("             Korean Cafe                 ")
    print("=========================================")
    print(" Menu Pesanan     : ", str(Pesanan))
    print(" SubTotal         : Rp. ", sum(Total))
    diskon = 0
    a = int(sum(Total))
    if a > 50000:
      diskon = int(a * 10/100)
    elif a > 100000:
        diskon = int(a * 25/100)
    else:
      print('Nama Hari Yang Anda Masukkan Tidak Valid')
      diskon = 0
      akhir()
    print(" Potongan Harga   : Rp. ", diskon )
    totalakhir = int((sum(Total))- diskon)
    print(" Total Pembayaran : Rp. ", totalakhir)
    print("-----------------------------------------")
    bayar = int(input("Bayar            : Rp. "))
    kembalian = bayar - totalakhir
    print(" Kembalian        : Rp. ", kembalian)
    print("=========================================")
    print("             Terima Kasih                ")
    print("=========================================")

#program utama
def Pilihan():
  loop = 1
  while loop == 1:
    Pilihan = int(input('Masukkan nomor menu pilihan Anda: '))
    if Pilihan == 1:
      Tteokbokki()
      tanya()
    elif Pilihan == 2:
      Kimbap()
      tanya()
    elif Pilihan == 3:
      Bibimbap()
      tanya()
    elif Pilihan == 4:
      Jajangmyeon()
      tanya()
    elif Pilihan == 5:
      Bulgogi()
      tanya()
    elif Pilihan == 6:
      Banana_Milk()
      tanya()
    elif Pilihan == 7:
      Yuja_Cha()
      tanya() 
    elif Pilihan == 8:
      Ice_Americano()
      tanya()
    elif Pilihan == 9:
      Daechu_Tea()
      tanya()
    elif Pilihan == 10:
      Soju()
      tanya()
      loop = 0
    else: 
      print('Nomor menu yang Anda masukkan tidak valid')

menu()
Pilihan()
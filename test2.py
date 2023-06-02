#data program
data={
    "wisata":{
    "Pantai Kuta": 0,
    "Pantai Pandawa": 8000,
    "Sangeh Monkey Forest": 15000,
    "Danau Batur": 15000,
    "Desa Penglipuran": 25000,
    "Pura Luhur Uluwatu": 30000,
    "Garuda Wisnu Kencana": 125000
    },
    "hotel_harga":{
    "hotel_murah":{
    "hotel Segara Sadhu Inn Kuta":130000,
    "hotel The Hill Ungasan Bukit Jimbaran": 220000,
    "hotel PAndawa Beach Homestay": 350000
    },
    "hotel_menengah":{
    "hotel Kintamani Gold View": 475000,
    "hotel Pandawa Hill Resort": 500000,
    "hotel Uma Mani Villa": 580000,
    "hotel Yollow Kuta Beacwalk Bali": 650000
    },
    "hotel_mahal":{
    "hotel  Four Points by Sheraton Ungasan": 1100000,
    "Hotel Kuta Seaview Boutique Resort": 1200000,
    "hotel The Ayu Kintamani Villa": 2900000,
    "Hotel Jumana Bali Ungasan resort": 5000000
    }}}
    

#program sign up dan login
# Dictionary untuk menyimpan data pengguna
users = {}  

def sign_up():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in users:
        print("Username sudah digunakan. Silakan coba lagi.")
    else:
        users[username] = password
        print("Pendaftaran berhasil!")

def login():
    while True: 
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if  username in users and users[username] == password:
            print("Login berhasil!")
 # Panggil fungsi atau program selanjutnya setelah login berhasil
            break
        else:
            print("Username atau password salah.")

# Program Utama
print("Selamat datang!")
while True:
    print('''Pilih opsi:
    1. Sign up
    2. Login''')
    pilih = input("Masukkan pilihan (1/2): ")
    if pilih == "1":
        sign_up()
    elif pilih == "2":
        login()
        # Jika login berhasil, keluar dari loop dan lanjutkan ke program selanjutnya
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

#memilih kategori wisata
print(''' Pilih opsi:
1. Budget
2. Rating''')
kategori=input("Silakan memilih kategori wisata (1/2): ")
hari=input("silakan memilih berapa lama waktu berwisata (2 hari sampai dengan 4 hari): ")

# jika user memilih kategori budget
if kategori == "1":
# jika user memilih 2 hari untuk berlibur
    if hari == "2":
        uang=int(input("masukkan jumlah nomimal budget anda: "))
        if uang<=400000:
            print("berikut tempat wisata yang dapat anda pilih" )
            print(data["wisata"])
            print()
            print("berikut tempat penginapan yang dapat anda pilih")
            print(data["hotel_harga"]["hotel_murah"])
            murah2wisata=input("silahkan memilih tempat wisata: ")
            murah2hotel=input("silahkan memilih tepat penginapan: ")
        elif uang<=600000:
            print("berikut tempat wisata yang dapat anda pilih" )
            print(data["wisata"])
            print()
            print("berikut tempat penginapan yang dapat anda pilih")
            print(data["hotel_harga"]["hotel_menengah"])
            menengah2wisata=input("silahkan memilih tempat wisata: ")
            menengah2hotel=input("silahkan memilih tepat penginapan: ")
    # jika user memilih 3 hari untuk berlibur
    elif hari == "3":
        uang=int(input("masukkan jumlah nomimal: "))
        if uang<=600000:
            print("berikut tempat wisata yang dapat anda pilih" )
            print(data["wisata"])
            print()
            print("berikut tempat penginapan yang dapat anda pilih")
            print(data["hotel_harga"]["hotel_murah"])
            murah3wisata=input("silahkan memilih tempat wisata: ")
            murah3hotel=input("silahkan memilih tepat penginapan: ")
        elif uang<=800000:
            print("berikut tempat wisata yang dapat anda pilih" )
            print(data["wisata"])
            print()
            print("berikut tempat penginapan yang dapat anda pilih")
            print(data["hotel_harga"]["hotel_menengah"])
            menengah2wisata=input("silahkan memilih tempat wisata: ")
            menengah2hotel=input("silahkan memilih tepat penginapan: ")
        else:
            print("berikut tempat wisata yang dapat anda pilih" )
            print(data["wisata"])
            print()
            print("berikut tempat penginapan yang dapat anda pilih")
            print(data["hotel_harga"]["hotel_mahal"])
            mahal2wisata=input("silahkan memilih tempat wisata: ")
            mahal2hotel=input("silahkan memilih tepat penginapan: ")
    # jika user memilih 4 hai untuk berlibur
    elif hari =="4":
        uang=int(input("masukkan jumlah nomimal: "))
        if uang<=700000:
            murah4=input("silahkan memilih tempat wisata: ")
        elif uang<=900000:
            menengah4=input("silahkan memilih tempat wisata: ")
        else:
            mahal4=input("silahkan memilih tempat wisata: ")

# jika user memilih kategori berdasarkan rating
elif kategori == "2":
    rating=input("masukkan rating yang anda inginkan (4/5): ")
    if rating == "4":
        if hari == "2":
           print("berikut tempat wisata yang dapat anda pilih" ) 
        elif hari == "3":
            print("berikut tempat wisata yang dapat anda pilih" ) 
        elif hari == "4":
            print("berikut tempat wisata yang dapat anda pilih" ) 
    elif rating == "5":
        if hari == "2":
            print("berikut tempat wisata yang dapat anda pilih" ) 
        elif hari == "3":
            print("berikut tempat wisata yang dapat anda pilih" )
        elif hari == "4":
            print("berikut tempat wisata yang dapat anda pilih" )  
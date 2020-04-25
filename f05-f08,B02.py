import csv
from csv import writer

def cariPemain():
    findPlayer = input("Masukkan username: ")
    found = False
    i = 1
    with open('user.csv', 'r') as readfile:
        d = csv.reader(readfile)
        playerData = list(d)
        count = len(playerData)
        while (not found and i < count) :
            if (findPlayer == playerData[i][3]):
                found = True
            else:
                i = i + 1

        if found:
            print("Nama Pemain:", playerData[i][0])
            print("Tinggi Pemain:", playerData[i][2])
            print("Tanggal Lahir Pemain:", playerData[i][1])
        else:
            print("Pemain tidak ditemukan.")
            
def cariWahana():
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print(" ")
    print("Jenis batasan tinggi:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print(" ")

    # Input batas umur
    batasUmur = int(input("Batasan umur pemain: "))
    while (batasUmur < 1 or batasUmur > 3):
        print("Batasan umur tidak valid!")
        batasUmur = int(input("Batasan umur pemain: "))

    # Input batas tinggi
    batasTinggi = int(input("Batasan tinggi pemain: "))
    while (batasTinggi < 1 or batasTinggi > 2):
        print("Batasan tinggi badan tidak valid!")
        batasUmur = int(input("Batasan tinggi pemain: "))

    print(" ")

    umur = 17
    tinggi = 170

    found = False
    i = 1

    with open('wahana.csv', 'r') as userfile:
        venueData = list(csv.reader(userfile))
        count = len(venueData)

        while (i < count):
            if (batasTinggi == 1):
                if (batasUmur == 1):
                    if (umur < int(venueData[i][4]) and tinggi > int(venueData[i][5])):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                elif (batasUmur == 2):
                    if (umur >= int(venueData[i][4]) and tinggi > int(venueData[i][5])):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                else:
                    if (tinggi > int(venueData[i][5])):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
            else:
                if (batasUmur == 1):
                    if (umur < int(venueData[i][4])):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                elif (batasUmur == 2):
                    if (umur >= int(venueData[i][4])):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                else:
                    print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                    found = True
                    i = i + 1

        if not found:
            print("Tidak ada wahana yang sesuai dengan pencarian Anda.")
               
def beliTiket(username):
    wahanaID = input("Masukkan ID wahana: ")
    today = input("Masukkan tanggal hari ini: ") # Untuk cek umur pemain
    qty = int(input("Jumlah tiket yang dibeli: "))

    # Array tanggal hari ini
    curr = [int(today[:2]), int(today[3:5]), int(today[6:])]

    with open('user.csv', 'r') as userfile:
        userData = list(csv.reader(userfile))
        found = False
        i = 1

        # Cari index user
        while (not found and i < len(userData)):
            if (username == userData[i][3]):
                found = True
            else:
                i = i + 1

        # Array date of birth user
        birthYr = int(userData[i][1][6:])
        birthMth = int(userData[i][1][3:5])
        birthDay = int(userData[i][1][:2])
        dob = [birthDay, birthMth, birthYr]

        # Menyimpan saldo user
        saldo = userData[i][6]
        
    with open('wahana.csv', 'r') as userfile:
        venueData = list(csv.reader(userfile))
        count = len(venueData)

        j = 1
        found = False

        # Cari index wahana
        while (not found and i < count):
            if (wahanaID == venueData[j][0]):
                found = True
            else:
                j = j + 1
        
        # Menyimpan harga tiket
        if userData[i][7]: # Memeriksa apakah akun gold
            price = int(venueData[j][2]) * 0.5
        else:
            price = int(venueData[j][2])

        # Memeriksa umur user
        old = False
        
        if (curr[2] - dob[2] > int(venueData[j][3])):
            if (curr[1] - dob[1] == 0):
                if (curr[0] - dob[0] < 0):
                    print("Anda tidak cukup umur untuk menaiki wahana ini.")
                else:
                    old = True
            else:
                old = True
        else:
            print("Anda tidak cukup umur untuk menaiki wahana ini.")

        # Memeriksa saldo user
        if old:
            enough = False
            if (saldo > price*qty):
                enough = True
                userData[i][6] = saldo - price*qty
            else:
                print("Saldo Anda tidak cukup.")
    
    if enough:
        print("")
        print("Selamat bersenang-senang di", venueData[j][1])
        print(" ")
        tiket = [username, wahanaID, qty]
        
        with open('tiket.csv', 'a+', newline='') as write:
            a = writer(write)
            a.writerow(tiket)  

        with open('user.csv', 'w', newline='') as write:
            b = writer(write)
            b.writerows(userData)       

def pakaiTiket(username):
    wahanaID = input("Masukkan ID wahana: ")
    date = input("Masukkan tanggal hari ini: ")
    use = int(input("Jumlah tiket yang digunakan: "))

    with open('tiket.csv', 'r', newline='') as userfile:
        d = csv.reader(userfile)
        tiket = list(d)
        count = len(tiket)
        
        valid = False
        found = False
        i = 1

        while not found and i < count:
            if (wahanaID == tiket[i][1] and username == tiket[i][0]):
                found = True
            else:
                i = i + 1
        
        if found:
            if (use <= int(tiket[i][2])):
                valid = True
                if valid:
                    newQty = int(tiket[i][2]) - use
                    if newQty == 0 :
                        tiket.pop(i)
                    else:
                        tiket[i][2] = str(newQty)
                else:
                    print("Tiket Anda tidak valid dalam sistem kami.")
                
        else:
            print("Tiket Anda tidak valid dalam sistem kami.")

    with open('wahana.csv', 'r') as userfile:
        venueData = list(csv.reader(userfile))
        print("")
        print("Selamat bersenang-senang di", venueData[i][1])

    with open('tiket.csv', 'w', newline='') as userfile:
        f = csv.writer(userfile)
        f.writerows(tiket)

def goldAccount(username):
    with open('user.csv', 'r') as userfile:
        userData = list(csv.reader(userfile))
        upgrade = False

        # Mencari index username pemain
        count = len(userData)
        i = 1
        found = False

        while (not found and i < count) :
            if (username == userData[i][3]):
                found = True
            else:
                i = i + 1

        if (userData[i][5] == "admin"):
            print("Harga akun premium adalah Rp50.000,00")
            upgrUser = input("Masukkan username user yang ingin di-upgrade:")
            price = 50000

            with open('user.csv', 'r') as userfile:
                userData = list(csv.reader(userfile))
                found = False
                i = 1

                # Cari index user
                while not found and i < len(userData) :
                    if (upgrUser == userData[i][3]):
                        found = True
                    else:
                        i = i + 1
                
                # Upgrade account
                if found:
                    if not userData[i][7]:
                        print("Akun sudah terdaftar sebagai Golden.")
                    else:
                        if (int(userData[i][6]) > price):
                            userData[i][7] = True
                            userData[i][6] = int(userData[i][6]) - price
                            upgrade = True
                            print("Akun Anda telah diupgrade.")
            if upgrade:
                with open('user.csv', 'w', newline='') as write:
                    w = writer(write)
                    w.writerows(userData) 

        else:
            print("Anda tidak dapat mengakses menu ini.")


##### UNTUK KEPERLUAN TESTING #####

###username = input("Insert username: ")
###print(" ")
###print("Pilih menu:")
###print("1. Cari pemain")
###print("2. Cari wahana")
###print("3. Beli tiket")
###print("4. Pakai tiket")
###print("5. Upgrade account")
###choice = int(input())

###if choice == 1 :
###    cariPemain()
###elif choice == 2 :
###    cariWahana()
###elif choice == 3 :
###    beliTiket(username)
###elif choice == 4 :
###    pakaiTiket(username)
###else:
###    goldAccount(username)
def load():
    fileUser=input("Masukkan nama File User : ")
    fileWahana=input("Masukkan nama File Daftar Wahana : ")
    filePembelian=input("Masukkan nama File Pembelian Tiket : ")
    filePenggunaan=input("Masukkan nama File Penggunaan Tiket : ")
    fileTiket=input("Masukkan nama File Kepemilikan Tiket : ")
    fileRefund=input("Masukkan nama File Refund Tiket : ")
    fileKritiksaran=input("Masukkan nama File Kritik dan Saran : ")

    #yang diload merupakan file temporary
    loadFile(fileUser)
    loadFile(fileWahana)
    loadFile(filePembelian)
    loadFile(filePenggunaan)
    loadFile(fileTiket)
    loadFile(fileRefund)
    loadFile(fileKritiksaran)

    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")
    

def save():
    #disave ke file asli
    fileUser=input("Masukkan nama File User : ")
    fileWahana=input("Masukkan nama File Daftar Wahana : ")
    filePembelian=input("Masukkan nama File Pembelian Tiket : ")
    filePenggunaan=input("Masukkan nama File Penggunaan Tiket : ")
    fileTiket=input("Masukkan nama File Kepemilikan Tiket : ")
    fileRefund=input("Masukkan nama File Refund Tiket : ")
    fileKritiksaran=input("Masukkan nama File Kritik dan Saran : ")


    saveFile("userTemp.csv", fileUser)
    saveFile("wahanaTemp.csv",fileWahana)
    saveFile("pembelianTemp.csv",filePembelian)
    saveFile("penggunaanTemp.csv",filePenggunaan)
    saveFile("tiketTemp.csv",fileTiket)
    saveFile("kritiksaranTemp.csv",fileKritiksaran)
    print("Data berhasil disimpan!")

def signup():
    Nama=input("Masukkan nama pemain : ")
    Tanggal_Lahir=input("Masukkan tanggal lahir pemain (DD/MM/YYYY) : ")
    Tinggi_Badan=int(input("Masukkan tinggi badan pemain (cm) : "))
    Username=input("Masukkan username pemain : ")
    Password = getpass.getpass("Masukkan password pemain : ")
    Role=input("Masukkan Role : ")
    Saldo=int(input("Masukkan Saldo : "))

    tambahUser(Nama,Tanggal_Lahir,str(Tinggi_Badan),Username,Password,Role,str(Saldo))
#signup kurang lengkap, kalau ada username sama (?)

def login(Username,Password):# return temp(0 username ngga ada, 1 username ada password salah, 2 username ada password benar)
    global temp
    ifile = open("user.csv")
    reader = csv.reader(ifile)
    temp = '0' #0 username ngga ada, 1 username ada password salah, 2 username ada password benar, 3 admin

    for row in reader:
        if (row[3] == Username):
            temp = 1
            if (cipher.decrypt(row[4].encode()).decode() == Password):
                temp = 2
                if (row[5] == 'admin'):
                    temp = 3
#kurang admin login

def cariPemain():
    findPlayer = input("Masukkan username: ")
    found = False
    i = 1
    with open('user.csv', 'r') as readfile:
        d = csv.reader(readfile)
        playerData = list(d)
        count = sebutSajaLen(playerData)
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
                        #venueData.append(venueData[i])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                elif (batasUmur == 2):
                    if (umur >= int(venueData[i][4]) and tinggi > int(venueData[i][5])):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        #venueData.append(venueData[i])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                else:
                    if (tinggi > int(venueData[i][5])):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        #venueData.append(venueData[i])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
            else:
                if (batasUmur == 1):
                    if (umur < int(venueData[i][4])):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        #venueData.append(venueData[i])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                elif (batasUmur == 2):
                    if (umur >= int(venueData[i][4])):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        #venueData.append(venueData[i])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                else:
                    print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                    #venueData.append(venueData[i])
                    found = True
                    i = i + 1

        if not found:
            print("Tidak ada wahana yang sesuai dengan pencarian Anda.")

def beliTiket():
    # Catatan (1): Harusnya nanti username ikut diwrite ke file csv tapi ini tanpa login jd belum
    # Catatan (2): Kalau mau beli tiket lebih dari 1 wahana sebaiknya satu2 aja jangan langsung banyak
    # Catatan (3): Masih tanpa login, saldo dan umur pemain belum dicek

    wahanaID = input("Masukkan ID wahana: ")
    today = input("Masukkan tanggal hari ini: ") # Untuk cek umur pemain
    qty = input("Jumlah tiket yang dibeli: ")

    ticket = [wahanaID, qty] # Nanti pas udah dgn login index pertamanya itu username

    with open('wahana.csv', 'r') as userfile:
        venueData = list(csv.reader(userfile))
        count = len(venueData)

        i = 1
        found = False

        while (not found and i < count):
            if (wahanaID == venueData[i][0]):
                found = True
            else:
                i = i + 1
        
        print("")
        print("Selamat bersenang-senang di", venueData[i][1])

    with open('tiket.csv', 'a+', newline='') as write:
        w = writer(write)
        w.writerow(ticket)    

def pakaiTiket():
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
            if (wahanaID == tiket[i][1]):
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
        
    with open('tiket.csv', 'w', newline='') as userfile:
        f = csv.writer(userfile)
        f.writerows(tiket)

def refund():
    tanggal = date.today()
    Id_Wahana=input("Masukan ID wahana : ")
    Jumlah_refund=int(input('Jumlah tiket yang di-refund :'))
    
    with open('pembelian.csv','r') as csv:
        reader1= csv.DictReader(csv)
        for row in reader1:
            if (row['ID_Wahana']) == Id_Wahana:
                cek_jumlah = int(row['Jumlah_Tiket'])
				#cek_Username=(row['Username']) masih bingung gimana ngecek username nya 
                cek_id_wahana=(row['ID_Wahana'])	
		
        with open('refund.csv', 'r+') as csvfile:
            fieldnames=['Username','Tanggal_Refund','ID_Wahana','Jumlah_Tiket']
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            reader= csv.DictReader(csvfile)
            
            for row in reader:
                if (row['ID_Wahana']) == Id_Wahana:
                    if cek_jumlah >= Jumlah_refund:
                        pengurangan_tiket = cek_jumlah - Jumlah_refund
                        writer.writerow({'Tanggal_Refund': tanggal,'ID_Wahana':Id_Wahana, 'Jumlah_Tiket': pengurangan_tiket})
                        print('Uang refund sudah kami berikan pada akun Anda.')
                    else:
                        print("Anda tidak memiliki tiket terkait.")
                else:
                    print("Anda tidak memiliki tiket terkait.")

def kritikSaran():
    Id_Wahana=input("Masukan ID wahana : ")
    tanggal = input('Tanggal pelaporan :')
    kritik_saran=input('Kritik/saran anda :')

    with open ('kritiksaran.csv','r+') as csv:
        writer= csv.DictWriter(csv)
        #ngisi usernamenya gatau gimana..
        writer.writerow({'Tanggal_Kritik': tanggal,'ID_Wahana':Id_Wahana, 'Isi_Kritik': kritik_saran})

def tambahWahana():
    print('Masukan Informasi Wahana yang ditambahkan :')
    ID_Wahana = input('Masukan ID Wahana : ')
    Nama_Wahana = input('Masukan Nama Wahana : ')
    Harga_Tiket = input('Masukan Harga Tiket : ')
    Batasan_umur = input('Batasan umur : ')
    Batasan_tinggi = input('Batasan Tinggi Badan : ')

    with open ('wahana.csv', 'r+') as csv:
        writer=csv.writer(csv)
        writer.writerow([ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_umur,Batasan_tinggi])

def topUp():
    with open('user.csv') as inf:
        reader = csv.reader(inf.readlines())

    with open('user.csv', 'w') as outf:
        username=input("Masukkan username : ")
        jumlahTopUp=int(input("Masukkan saldo : "))
        writer = csv.writer(outf)
        for line in reader:
            if username==line[3]:
                saldoAwal=int(line[6])
                saldoAkhir=saldoAwal+jumlahTopUp
                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5], str(saldoAkhir)])
            else:
                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5], line[6]])

def riwayat():
    ulang=0
    arrayJumlahTiket=[]
    arrayUser=[]
    arrayTanggal=[]
    with open('penggunaan.csv') as tiketfile:
        readTiket = csv.reader(tiketfile)
        next(tiketfile)
        cariID=input("Masukkan ID wahana : ")
        for baris in readTiket:
            if cariID==baris[2]:
                ulang=ulang+1
                arrayTanggal=arrayTanggal+[baris[1]]
                arrayJumlahTiket=arrayJumlahTiket+[baris[3]]
                arrayUser=arrayUser+[baris[0]]
                
    print("Riwayat : ")
    for i in range (ulang):
        print(f"{arrayTanggal[i]} | {arrayUser[i]} | {arrayJumlahTiket[i]}")

def jumlahPemain():
    #membaca kolom tiket dan jumlah, kemudian menggubahnya ke bentuk array
    with open('tiket.csv') as tiketfile:
        readTiket = csv.reader(tiketfile)
        next(tiketfile)
        cari=input("masukkan pencarian : ")
    	#cari='ariya'
        for kolom in readTiket:
            if cari==kolom[0]:
                arrayID=(kolom[1])
                arrayJumlah=(kolom[2])

        arrayKode=(sebutsajaApend(arrayID))
        print(f"arraykode = {arrayKode}")

#mulai dari sini
    arrayBanyak=[]
    hitung=0
    jumlah=0
#membuat array untuk jumlah tiket
    for i in arrayJumlah:
        if i==',':
            hitung=hitung+1
        elif i==' ':
            hitung=hitung+0
        else:
            arrayBanyak=arrayBanyak+[f'{i}']
            jumlah=jumlah+1

#menampilkan wahana dan banyak tiket
    index=hitung+1
    print("ID Wahana | Banyak Tiket ")
    for i in range (index):
        print(f"{arrayKode[i]}    | {arrayBanyak[i]}")
    

def exitProgram():
    global stmt
    close=input("\nApakah Anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")
    if close=='Y' or close=='y':
        save()
        stmt=False
    elif close=='N' or close=='n':
        print("Terima kasih telah menggunakan program ini")
        stmt=False
    else:
        print("Input tidak valid, harap ulangi!")


#============================================================================================================================
#Fungsi buatan sendiri

def loadFile(fileName):
    ifile = open(fileName)
    reader = csv.reader(ifile)

    lebar = 0
    panjang = 0
    for row in reader:
        lebar += 1
        #print(row)
        panjang = 0
        for col in row :
            panjang += 1
    #print(lebar)
    #print(panjang)

    arr = ["0" for j in range(lebar)]

    ifile = open(fileName)
    reader = csv.reader(ifile)
    i = 0
    for row in reader:
       arr [i] = row
       i += 1
    ifile.close()
    return(arr)

def saveFile(fileName,array):
    
    ifile = open(fileName,'w')
    #print(array[0])
    #writer = csv.DictWriter(ifile, fieldnames=array[0])
    for row in array:
        #print(row)
        temp=''
        for col in row:
            temp += str(col) + ','
        temp = temp[0:-1]
        ifile.write(temp + '\n')


def tambahUser(Nama,Tanggal_Lahir,Tinggi_Badan,Username,Password,Role,Saldo): #pasti ke file user
    ifile = open("user.csv",'a')
    ifile.write(Nama + ',' + Tanggal_Lahir+ ','  + Tinggi_Badan+ ','  + Username+ ','  + cipher.encrypt(Password.encode()) + ','  + Role + ','  + Saldo)
    ifile.write('\n')

def sebutSajaLen(b):
    count = 0
    for i in b:
        count = count + 1
    return(count)

def sebutsajaApend(a):
    array = []
    newarray = []
    hitung=0
    batas=0
    jumlahhuruf = (sebutSajaLen(a))
    for i in a:
        if i==',' or i==' ':
            hitung=(hitung+1)
            batas=batas+0
        else:
            array=array+[i]
            batas=batas+1
    for i in range (jumlahhuruf)[:batas:6]:
        newarray=newarray+[(array[i]+array[i+1]+array[i+2]+array[i+3]+array[i+4]+array[i+5])]
    return(newarray)


def loggedmenu():
    print("\nBeberapa pilihan menu: ")
    print("1. Pencarian Wahana")
    print("2. Pembelian Tiket")
    print("3. Gunakan Tiket")
    print("4. Refund")
    print("5. Kritik dan Saran")
    print("6. Exit")
    pilihan=int(input("Masukkan pilihan : "))

    if pilihan==1:
        cariWahana()
    elif pilihan==2:
        beliTiket()
    elif pilihan==3:
        pakaiTiket()
    elif pilihan==4:
        refund()
    elif pilihan==5:
        kritikSaran()
    elif pilihan==6:
        exitProgram()

def adminmenu():
    print("\nADMIN AREA")
    print("1. Sign Up")
    print("2. Pencarian Pemain")
    print("3. Tambah Wahana Baru")
    print("4. Top Up Saldo")
    print("5. Riwayat Penggunaan Wahana")
    print("6. Jumlah Tiket Pemain")
    print("7. Exit")
    pilihan=int(input("Masukkan pilihan : "))

    if pilihan==1:
        signup()
    elif pilihan==2:
        cariPemain()
    elif pilihan==3:
        tambahWahana()
    elif pilihan==4:
        topUp()
    elif pilihan==5:
        riwayat()
    elif pilihan==6:
        jumlahPemain()
    elif pilihan==7:
        exitProgram()

#Kondisi awal
import csv
import getpass
from datetime import date
from cryptography.fernet import Fernet

stmt=True
permAdmin = False

key = b'EXiOWY1qNCF39AfV4j8GKMZBUvnlMufhwPwm4bfjMPU='
cipher = Fernet(key)

print("\nSelamat Datang di Wahana Wangky")
print("Silahkan Login untuk menggunakan fasilitas ini")
while stmt==True:
    username=input("\nMasukkan Username : ")
    password=getpass.getpass("Masukkan Password : ")
    login(username,password)
    if temp == 3 :
        permAdmin = True
    if (temp==2 or temp == 3):
        adminmenu()
    else:
        print("\n Login gagal, silahkan ulangi!")
    



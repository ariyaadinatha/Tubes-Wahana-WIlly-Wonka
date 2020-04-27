def load():
    '''
    fileUser=input("Masukkan nama File User : ")
    fileWahana=input("Masukkan nama File Daftar Wahana : ")
    filePembelian=input("Masukkan nama File Pembelian Tiket : ")
    filePenggunaan=input("Masukkan nama File Penggunaan Tiket : ")
    fileTiket=input("Masukkan nama File Kepemilikan Tiket : ")
    fileRefund=input("Masukkan nama File Refund Tiket : ")
    fileKritiksaran=input("Masukkan nama File Kritik dan Saran : ")
    '''
    fileUser='user.csv'
    fileWahana='wahana.csv'
    filePembelian='pembelian.csv'
    filePenggunaan='penggunaan.csv'
    fileTiket='tiket.csv'
    fileRefund='refund.csv'
    fileKritiksaran='kritiksaran.csv'

    #yang diload merupakan file temporary
    global ArrUser
    global ArrWahana
    global ArrPembelian
    global ArrPenggunaan
    global ArrTiket
    global ArrRefund
    global ArrKritiksaran
    
    ArrUser = loadFile(fileUser)
    ArrWahana = loadFile(fileWahana)
    ArrPembelian = loadFile(filePembelian)
    ArrPenggunaan = loadFile(filePenggunaan)
    ArrTiket =  loadFile(fileTiket)
    ArrRefund = loadFile(fileRefund)
    ArrKritiksaran = loadFile(fileKritiksaran)

    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")
    

def save():
    #disave ke file asli
    '''
    fileUser=input("Masukkan nama File User : ")
    fileWahana=input("Masukkan nama File Daftar Wahana : ")
    filePembelian=input("Masukkan nama File Pembelian Tiket : ")
    filePenggunaan=input("Masukkan nama File Penggunaan Tiket : ")
    fileTiket=input("Masukkan nama File Kepemilikan Tiket : ")
    fileRefund=input("Masukkan nama File Refund Tiket : ")
    fileKritiksaran=input("Masukkan nama File Kritik dan Saran : ")
    '''
    saveFile("user.csv", ArrUser)
    saveFile("wahana.csv",ArrWahana)
    saveFile("pembelian.csv",ArrPembelian)
    saveFile("penggunaan.csv",ArrPenggunaan)
    saveFile("tiket.csv",ArrTiket)
    saveFile('refund.csv',ArrRefund)
    saveFile("kritiksaran.csv",ArrKritiksaran)
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

# Fungsi F05-F08 + B02 #
def cariPemain():
    findPlayer = input("Masukkan username: ")
    found = False
    i = 1
    with open('user.csv', 'r') as readfile:
        d = csv.reader(readfile)
        playerData = list(d)
        count = sebutsajaLen(playerData)
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
        batasTinggi = int(input("Batasan tinggi pemain: "))

    print(" ")

    umur = 17
    tinggi = 170

    found = False
    i = 1

    with open('wahana.csv', 'r') as userfile:
        venueData = list(csv.reader(userfile))
        count = sebutSajaLen(venueData)

        while (i < count):
            if (batasTinggi == 1):
                if (batasUmur == 1):
                    if int(venueData[i][3]) < umur and int(venueData[i][4]) > tinggi:
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                elif (batasUmur == 2):
                    if int(venueData[i][3]) >= umur and int(venueData[i][4]) > tinggi:
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                else:
                    if int(venueData[i][4]) > tinggi:
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
            else:
                if (batasUmur == 1):
                    if (int(venueData[i][3]) < umur):
                        print(venueData[i][0],"|",venueData[i][1],"|",venueData[i][2])
                        found = True
                        i = i + 1
                    else:
                        i = i + 1
                elif (batasUmur == 2):
                    if int(venueData[i][4]) >= umur:
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
        while (not found and i < length(userData)):
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
        saldo = float(userData[i][6])
        
    with open('wahana.csv', 'r') as userfile:
        venueData = list(csv.reader(userfile))
        count = sebutSajaLen(venueData)

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
            old = True
        elif (curr[2] - dob[2] == int(venueData[j][3])):
            if (curr[1] - dob[1] == 0):
                if (curr[0] - dob[0] < 0):
                    print("Anda tidak cukup umur untuk menaiki wahana ini.")
                else:
                    old = True
            elif (curr[1] - dob[1] < 0):
                    print("Anda tidak cukup umur untuk menaiki wahana ini.")
            else:
                old = True
        else:
            print("Anda tidak cukup umur untuk menaiki wahana ini.")

        # Memeriksa saldo user
        enough = False
        if old:
            if (saldo >= price*qty):
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
            a = csv.writer(write)
            a.writerow(tiket)  

        with open('user.csv', 'w', newline='') as write:
            b = csv.writer(write)
            b.writerows(userData)       

def pakaiTiket(username):
    wahanaID = input("Masukkan ID wahana: ")
    date = input("Masukkan tanggal hari ini: ")
    use = int(input("Jumlah tiket yang digunakan: "))

    with open('tiket.csv', 'r', newline='') as userfile:
        tiket = list(csv.reader(userfile))
        count = sebutSajaLen(tiket)
        
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
        count = sebutSajaLen(venueData)
        found = False
        j = 1

        while not found and j < count:
            if venueData[j][0] == wahanaID:
                found = True
            else:
                j = j + 1
        if valid:
            print("")
            print("Selamat bersenang-senang di", venueData[j][1])

    with open('tiket.csv', 'w', newline='') as userfile:
        f = csv.writer(userfile)
        f.writerows(tiket)

def goldAccount(username):
    with open('user.csv', 'r') as userfile:
        userData = list(csv.reader(userfile))
        upgrade = False

        # Mencari index username pemain
        count = length(userData)
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

            upgrade = False
            found = False
            i = 1

            # Cari index user
            while not found and i < length(userData) :
                if (upgrUser == userData[i][3]):
                    found = True
                else:
                    i = i + 1
                
            # Upgrade account
            if found:
                if (userData[i][7] == "True"):
                    print("Akun sudah terdaftar sebagai Golden.")
                else:
                    if (float(userData[i][6]) > price):
                        userData[i][7] = True
                        userData[i][6] = float(userData[i][6]) - price
                        upgrade = True
                        print("Akun Anda telah diupgrade.")
                    else:
                        print("Saldo pengguna tidak cukup untuk melakukan upgrade.")
            else:
                print("Pengguna tidak ditemukan.")
            if upgrade:
                with open('user.csv', 'w', newline='') as write:
                    w = writer(write)
                    w.writerows(userData) 
        else:
            print("Anda tidak dapat mengakses menu ini.")


def refund(username):

    import csv
    from datetime import date
    tanggal = date.today()
    ID_Wahana=input("Masukan ID wahana : ")
    Jumlah_refund=int(input('Jumlah tiket yang di-refund :'))
    a=username
    array=[0 for i in range(100)]
    arrayuser=[0 for i in range(100)]
    n=0
    neff=0
    cek=0

#membuka file tiket.csv dan refund.csv
    with open('tiket.csv','r') as csvfile:
        with open('refund.csv','a',newline='') as csvfile1:
            fieldnames=['Username','ID_Wahana','Jumlah_Tiket']
            writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
            reader= csv.DictReader(csvfile)
            writer1=csv.writer(csvfile1)
            reader1= csv.reader(csvfile1)

            for row in reader:
                username_simpan=row['Username']
                ID_Wahana_simpan=row['ID_Wahana']
                jumlah_tiket_simpan=row['Jumlah_Tiket']
                array[neff]=(username_simpan,ID_Wahana_simpan,jumlah_tiket_simpan)#memasukan isi file tiket.csv kedalam array 
                neff+=1            
            for i in range (0,neff):
                if array[i][0] == a and array[i][1]==ID_Wahana:
                    cek=int(array[i][2])
            
            arraybaru=[0 for i in range(neff)]
            
            if cek>=Jumlah_refund:
                tiketakhir=str(cek-Jumlah_refund)
                for i in range (0,neff):
                    if array[i][0] == a and array[i][1]==ID_Wahana:
                        array[i]=(a,ID_Wahana,tiketakhir)#memasukan tiket terakhir yang sudah di update kedalam array
                        writer1.writerow([a,tanggal,ID_Wahana,cek])

                print('Uang refund sudah kami berikan pada akun Anda.')

                for i in range (0,neff):
                    data1=array[i][0]
                    data2=array[i][1]
                    data3=array[i][2]
                    arraybaru[i]=(data1,data2,data3)#memasukan data kedalam array baru
                

                with open ('user.csv','r') as liatuser:#membaca isi file user.csv
                    reader2=csv.DictReader(liatuser)
                    for row in reader2:
                        nama_simpan=row['Nama']
                        tanggalL_simpan=row['Tanggal_Lahir']
                        Tinggi_simpan=row['Tinggi_Badan']
                        user_simpan=row['Username']
                        pass_simpan=row['Password']
                        role_simpan=row['Role']
                        saldo_simpan=row['Saldo']
                        gold=row['Gold']
                        arrayuser[n]=(nama_simpan,tanggalL_simpan,Tinggi_simpan,user_simpan,pass_simpan,role_simpan,saldo_simpan,gold)#menulis isi file kedalam array
                        n+=1

                    for i in range (0,n):
                        if (arrayuser[i][3]) == a:
                            saldoawal=(arrayuser[i][6])
                            saldoakhir=int(float(saldoawal)+(500*float(cek)))#mengisi arrayuser dengan saldo akhir
                            arrayuser[i]=(arrayuser[i][0],arrayuser[i][1],arrayuser[i][2],arrayuser[i][3],arrayuser[i][4],arrayuser[i][5],str(saldoakhir),arrayuser[i][7])
                    

                with open ('user.csv','w') as csvfile:
                    fieldnames=['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password','Role','Saldo','Gold']
                    writer= csv.DictWriter(csvfile,fieldnames=fieldnames)

                    writer.writeheader()
                    for i in range (0,n):#menulis kembali isi user.csv dengan saldo akhir yang baru
                        writer.writerow({'Nama':arrayuser[i][0],'Tanggal_Lahir':arrayuser[i][1],'Tinggi_Badan':arrayuser[i][2],'Username':arrayuser[i][3],'Password':arrayuser[i][4],'Role':arrayuser[i][5],'Saldo':arrayuser[i][6],'Gold':arrayuser[i][7]})


            

                with open ('tiket.csv','w') as csvfile:
                    fieldnames=['Username','ID_Wahana','Jumlah_Tiket']
                    writer= csv.DictWriter(csvfile,fieldnames=fieldnames)

                    writer.writeheader()
                    for i in range (0,neff):#menulis file dengan jumlah tiket yang  baru
                        writer.writerow({'Username':arraybaru[i][0],'ID_Wahana':arraybaru[i][1],'Jumlah_Tiket':(arraybaru[i][2])})
            else:
                print("Anda tidak memiliki tiket terkait.")

def kritikSaran(username):
    import csv
    a=(username)
    Id_Wahana=(input("Masukan ID wahana : "))
    tanggal =(input('Tanggal pelaporan :'))
    kritik_saran=(input('Kritik/saran anda :'))

    with open ('kritiksaran.csv','a',newline='') as csv_file:#menambahkan input kedalam file kritiksara.csv
        writer = csv.writer(csv_file)
        writer.writerow([a,tanggal,Id_Wahana,kritik_saran])
    print("Kritik dan saran Anda kami terima.")

def adminKritikSaran():
    import csv
    array=[0 for i in range (100)]
    neff=0
    with open ('kritiksaran.csv','r') as csv_file:#membaca isi file kritiksaran.csv
        reader=csv.DictReader(csv_file)

        for row in reader:
            Username = row['Username']
            Tanggal_Kritik = row['Tanggal_Kritik']
            ID_Wahana = row['ID_Wahana']
            Isi_Kritik = row['Isi_Kritik']
            array[neff]=(ID_Wahana,Tanggal_Kritik,Username,Isi_Kritik)#menulis kedalam array
            neff+=1
        print('Kritik dan saran : ')
        for i in range (0,neff):
            print(array[i][0],'|',array[i][1],'|',array[i][2],'|',array[i][3],'|')#output

def tambahWahana():
    import csv
    print('Masukan Informasi Wahana yang ditambahkan :')
    ID_Wahana = input('Masukan ID Wahana : ')
    Nama_Wahana = input('Masukan Nama Wahana : ')
    Harga_Tiket = input('Masukan Harga Tiket : ')
    Batasan_umur = input('Batasan umur : ')
    Batasan_tinggi = input('Batasan Tinggi Badan : ')

    with open ('wahana.csv','a',newline='') as csv_file:#membuka isi file
        writer=csv.writer(csv_file)

        writer.writerow([ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_umur,Batasan_tinggi])#menambahkan isi file dari hasil input
    print("Info wahana telah ditambahkan!")


def bestwahana():
    import csv
    array=[0 for i in range(100)]
    a=0
    neff=0
    with open ("wahana.csv","r") as csv1:#membaca isi file wahana.csv
        with open ("pembelian.csv",'r') as csv2:#membaca isi file pembelian.csv
            reader1=csv.DictReader(csv1)
            reader2=csv.DictReader(csv2)

            for row in reader2:
                ID_Wahana=row["ID_Wahana"]
                Jumlah=row["Jumlah_Tiket"]
                array[neff]=(Jumlah,ID_Wahana)#menyimpan didalam array
                neff+=1
            arraybaru=[0 for i in range((neff))]
            for row in reader1:
                for i in range (0,neff):
                    if row["ID_Wahana"] == array[i][1]:
                        nama=row["Nama_Wahana"]
                        data1=array[i][0]
                        data2=array[i][1]
                        data3=nama
                        arraybaru[i]=(data3,data2,data1)#menyimpan didalam array
            t=arraybaru
            sums = {}
            for i in t:#membuat data yang duplikat menjadi satu dan menjumlahkan valuenya
                sums[tuple(i[:-1])] = int(sums.get(tuple(i[:-1]),0)) + int(i[-1])
            arraybaru = [[a,b,sums[(a,b)]] for a,b in sums]

            for i in range(sebutSajaLen(arraybaru)):
                data1=arraybaru[i][0]
                data2=arraybaru[i][1]
                data3=arraybaru[i][2]
                arraybaru[i]=(data3,data2,data1)#menyimpan didalam array

            for i in range (1,sebutSajaLen(arraybaru)):#membuat insertion sort
                temp=int(arraybaru[i][0])
                tempgeser= arraybaru[i]
                j=i-1
                while j >= 0 and temp<int(arraybaru[j][0]):
                    arraybaru[j+1]= arraybaru[j]
                    j-=1
                arraybaru[j+1]=tempgeser
            arraybaru=(arraybaru[::-1])#membuat data dalam array diurutkan dari yang terbesar

            print("Best Wahana berdasarkan pembelian tiket :")
            for i in range (0,3):
                print(i+1,"|",arraybaru[i][1],"|",arraybaru[i][2],"|",arraybaru[i][0])


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
    ifile.write(Nama + ',' + Tanggal_Lahir+ ','  + Tinggi_Badan+ ','  + Username+ ','  + cipher.encrypt(Password.encode()).decode() + ','  + Role + ','  + Saldo)
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
        refund(username)
    elif pilihan==5:
        kritikSaran(username)
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
    print("7. Melihat Kritik dan Saran")
    print("8. Best Wahana")
    print("9. Exit")
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
        adminKritikSaran()
    elif pilihan==8:
        bestwahana()
    elif pilihan==9:
        exitProgram()

#Kondisi awal
import csv
import getpass
from csv import writer
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
    load()
    if temp == 3 :
        permAdmin = True
    if (temp==2 or temp == 3):
        adminmenu()
    else:
        print("\n Login gagal, silahkan ulangi!")
    



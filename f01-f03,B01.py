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
        value =''
        for col in row:
            value += str(col) + ','
        value = value[0:-1]
        ifile.write(value + '\n')


def tambahUser(Nama,Tanggal_Lahir,Tinggi_Badan,Username,Password,Role,Saldo): #pasti ke file user
    ifile = open("user.csv",'a')
    ifile.write(Nama + ',' + Tanggal_Lahir+ ','  + Tinggi_Badan+ ','  + Username+ ','  + cipher.encrypt(Password.encode()).decode() + ','  + Role + ','  + Saldo)
    ifile.write('\n')
    
import csv    
from cryptography.fernet import Fernet
key = b'EXiOWY1qNCF39AfV4j8GKMZBUvnlMufhwPwm4bfjMPU='
cipher = Fernet(key)
import csv
def topUp():
    with open('user.csv') as topupfile:
        reader = csv.reader(topupfile.readlines())

    with open('user.csv', 'w') as wtopupfile:
        username=input("\nMasukkan username : ")
        jumlahTopUp=int(input("Masukkan saldo : "))
        writer = csv.writer(wtopupfile)
        found=0 #memastikan bahwa data ditemukan
        for line in reader:
            #mencari username
            if username==line[3]:
                namaPemain=(line[0])
                saldoAwal=int(line[6])
                saldoAkhir=saldoAwal+jumlahTopUp
                found=found+1
                #mengubah data csv
                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5], str(saldoAkhir)])
            else:
                writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5], line[6]])
    if found==0:
        print("\nUser tidak ditemukan")
    else:
        print(f"\nTop up berhasil! Saldo {namaPemain} sekarang menjadi {saldoAkhir}")

def riwayat():
    index=0
    arrayJumlahTiket=[]
    arrayUser=[]
    arrayTanggal=[]
    with open('penggunaan.csv') as tiketfile:
        readTiket = csv.reader(tiketfile)
        next(tiketfile)
        cariID=input("\nMasukkan ID wahana : ")
        for baris in readTiket:
            if cariID==baris[2]:
                #menentukan index, agar tidak out of range
                index=index+1
                arrayTanggal=arrayTanggal+[baris[1]]
                arrayJumlahTiket=arrayJumlahTiket+[baris[3]]
                arrayUser=arrayUser+[baris[0]]
    if index==0:
        print("Riwayat tidak ditemukan")
    else:
        print("Riwayat : ")
        for i in range (index):
            print(f"{arrayTanggal[i]} | {arrayUser[i]} | {arrayJumlahTiket[i]}")

def jumlahTiket():
	#membuat array
    arrayID=[]
    arrayJumlah=[]
    arrayNama=[]
    kamusID=[]
    kamusNama=[]
    banyaKamus=0
    catatIndex=[]
    index=0
    with open('tiket.csv') as tiketfile:
        readTiket = csv.reader(tiketfile)
        next(tiketfile)
        cari=input("\nmasukkan username : ")
        for kolom in readTiket:
            #mencari username
            if cari==kolom[0]:
                #mengisi array
                arrayID=arrayID+[kolom[1]]
                arrayJumlah=arrayJumlah+[kolom[2]]
                index=index+1

    #untuk mencari nama wahana dari ID
    with open('wahana.csv') as wahanafile:
        readWahana = csv.reader(wahanafile)
        next(wahanafile)
        for kolom in readWahana:
            kamusID=kamusID+[kolom[0]]
            kamusNama=kamusNama+[kolom[1]]
            banyaKamus=banyaKamus+1
        matrixKamus=[kamusID,kamusNama]
    #menetapkan index wahana
    for i in range (index):
        for j in range (banyaKamus):
            if matrixKamus[0][j]==arrayID[i]:
                catatIndex=catatIndex+[j]

#menampilkan wahana dan banyak tiket
    if index==0:
        print("User tidak ditemukan")
    else:
        print("ID Wahana | Nama Wahana | Banyak Tiket ")
        for i in range (index):
            print(f"{arrayID[i]} | {kamusNama[catatIndex[i]]} | {arrayJumlah[i]}")

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

def tiketHilang():
    #bonus B04
    with open('tiketHilang.csv') as hilangfile:
        reader = csv.reader(hilangfile.readlines())

    #menulis kehilangan di file tiketHilang
    with open('tiketHilang.csv', 'w') as whilangfile:
        username=input("\nMasukkan username : ")
        tanggalHilang=input("Tanggal kehilangan tiket : DD/MM/YYYY ")
        idWahana=input("Masukkan ID wahana : ")
        jumlahHilang=int(input("Jumlah tiket yang dihilangkan : "))
        writer = csv.writer(whilangfile)
        
        for line in reader:
            writer.writerow([line[0],line[1],line[2],line[3]])
        writer.writerow([username,tanggalHilang,idWahana,jumlahHilang])
        print("Laporan kehilangan berhasil disubmit")
    
    with open('tiket.csv') as tiketfile:
        reader = csv.reader(tiketfile.readlines())

    #mengurangi tiket di file tiket.csv
    with open('tiket.csv', 'w') as wtiketfile:
        writer = csv.writer(wtiketfile)
        found=0
        for line in reader:
            if username==line[0] and idWahana==line[1]:
                found=found+1
                tiketAwal=int(line[2])
                tiketAkhir=tiketAwal-jumlahHilang
                if tiketAkhir<=0:
                    print("Tiket habis, data dihapus")
                else:
                    writer.writerow([line[0],line[1],str(tiketAkhir)])
            else:
                writer.writerow([line[0],line[1],line[2]])
    if found==0:
        print("Data tiket tidak ditemukan")
    else:
        print("File tiket berhasil diubah")

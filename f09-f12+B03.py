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



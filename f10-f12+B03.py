def kritikSaran(username):
    import csv
    a=(username)
    Id_Wahana=(input("Masukan ID wahana : "))
    tanggal =(input('Tanggal pelaporan :'))
    kritik_saran=(input('Kritik/saran anda :'))

    with open ('kritiksaran.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([a,tanggal,Id_Wahana,kritik_saran])
    print("Kritik dan saran Anda kami terima.")
#username=input()   
#kritikSaran(username)

def adminKritikSaran():
    import csv
    array=[0 for i in range (100)]
    neff=0
    with open ('kritiksaran.csv','r') as csv_file:
        reader=csv.DictReader(csv_file)

        for row in reader:
            Username = row['Username']
            Tanggal_Kritik = row['Tanggal_Kritik']
            ID_Wahana = row['ID_Wahana']
            Isi_Kritik = row['Isi_Kritik']
            array[neff]=(ID_Wahana,Tanggal_Kritik,Username,Isi_Kritik)
            neff+=1
        print('Kritik dan saran : ')
        for i in range (0,neff):
            print(array[i][0],'|',array[i][1],'|',array[i][2],'|',array[i][3],'|')
#adminKritikSaran()

def tambahWahana():
    import csv
    print('Masukan Informasi Wahana yang ditambahkan :')
    ID_Wahana = input('Masukan ID Wahana : ')
    Nama_Wahana = input('Masukan Nama Wahana : ')
    Harga_Tiket = input('Masukan Harga Tiket : ')
    Batasan_umur = input('Batasan umur : ')
    Batasan_tinggi = input('Batasan Tinggi Badan : ')

    with open ('wahana.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)

        writer.writerow([ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_umur,Batasan_tinggi])
    print("Info wahana telah ditambahkan!")
#tambahWahana()

def bestwahana():
    import csv
    array=[0 for i in range(100)]
    a=0
    neff=0
    with open ("wahana.csv","r") as csv1:
        with open ("pembelian.csv",'r') as csv2:
            reader1=csv.DictReader(csv1)
            reader2=csv.DictReader(csv2)

            for row in reader2:
                ID_Wahana=row["ID_Wahana"]
                Jumlah=row["Jumlah_Tiket"]
                array[neff]=(Jumlah,ID_Wahana)
                neff+=1
            arraybaru=[0 for i in range((neff))]
            for row in reader1:
                for i in range (0,neff):
                    if row["ID_Wahana"] == array[i][1]:
                        nama=row["Nama_Wahana"]
                        data1=array[i][0]
                        data2=array[i][1]
                        data3=nama
                        arraybaru[i]=(data3,data2,data1)
            t=arraybaru
            sums = {}
            for i in t:
                sums[tuple(i[:-1])] = int(sums.get(tuple(i[:-1]),0)) + int(i[-1])
            arraybaru = [[a,b,sums[(a,b)]] for a,b in sums]

            for i in range(sebutSajaLen(arraybaru)):
                data1=arraybaru[i][0]
                data2=arraybaru[i][1]
                data3=arraybaru[i][2]
                arraybaru[i]=(data3,data2,data1)

            for i in range (1,sebutSajaLen(arraybaru)):
                temp=int(arraybaru[i][0])
                tempgeser= arraybaru[i]
                j=i-1
                while j >= 0 and temp<int(arraybaru[j][0]):
                    arraybaru[j+1]= arraybaru[j]
                    j-=1
                arraybaru[j+1]=tempgeser
            arraybaru=(arraybaru[::-1])


            for i in range (0,3):
                print(i+1,"|",arraybaru[i][1],"|",arraybaru[i][2],"|",arraybaru[i][0])


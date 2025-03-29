import os
import math

# Header

# Luas Persegi Panjang
def luas_persegi(p,l):
    luas = p * l
    return luas

def keliling(p,l):
    k = 2 * (p+l)
    return k

def keliling_segitiga(a,b,c):
    k = a + b + c
    return k
def luas_segitiga(alas,tinggi):
    L = ( 1 / 2) * alas * tinggi
    return L

def keliling_lingkaran(r):
    phi = math.pi
    K = 2 * phi * r
    return K

def luas_lingkaran(r):
    pi = math.pi
    L = pi * r**2
    return L

def persegi(sisi):
    K = 4 * sisi
    return K
def persegi_luas(s,sisi):
    L = s * sisi
    return L


while True:
    os.system('cls')
    print(f'{'CALCULATE':^40}')
    print(f'{'-'*40:^40}')

    # User input
    try:
        print('''
1. Persegi Panjang
2. Segitiga
3. Lingkaran
4. Persegi
''')
        user_input = str(input('pilih opsi: ')).strip()

        if user_input == '1' or user_input.lower() == 'persegi panjang':
            print('''
1. Keliling Persegi Panjang
2. Luas Persegi Panjang
''')        
            user_input1 = str(input('pilih opsi(lagi): ')).strip()

            if user_input1 == '1' or user_input1.lower() == 'keliling' or user_input1.lower() == 'keliling persegi panjang':
                panjang = int(input('input nilai panjang: '))
                lebar = int(input('input nilai lebar: '))
                print(f'hasil perhitungan dari keliling persegi panjang: {keliling(panjang,lebar)}cm')
            elif user_input1 == '2' or user_input1.lower() == 'luas' or user_input1.lower() == 'luas persegi panjang':
                panjang = int(input('input nilai panjang: '))
                lebar = int(input('input nilai lebar: '))
                print(f'hasil perhitungan dari luas persegi panjang: {luas_persegi(panjang,lebar)}')
            else:
                print('dimohon untuk memilih opsi dengan benar')

        elif user_input == '2' or user_input.lower() == 'segitiga':
            print('''
1. Keliling Segitiga
2. Luas Segitiga
''')
            user_input1 = str(input('pilih opsi(lagi): ')).strip()

            if user_input1 == '1' or user_input1.lower() == 'keliling' or user_input1.lower() == 'keliling segitiga':
                sisi1 = int(input('input nilai sisi pertama: '))
                sisi2 = int(input('input nilai sisi kedua: '))
                sisi3 = int(input('input nilai sisi ketiga: '))
                print(f'Hasil dari perhitungan keliling segitiga: {keliling_segitiga(sisi1,sisi2,sisi3)}cm')
            elif user_input1 == '2' or user_input1.lower() == 'luas' or user_input1.lower() == 'luas segitiga ':
                alas = int(input('input nilai alas: '))
                tinggi = int(input('input nilai tinggi: '))
                print(f'Hasil dari perhitungan luas segitiga: {luas_segitiga(alas,tinggi)}')
            else:
                print('dimohon untuk memilih opsi dengan benar')

        elif user_input == '3' or user_input.lower() == 'lingkaran':
            print('''
1. Keliling Lingkaran
2. Luas Lingkaran
''')
            user_input2 = str(input('pilih opsi(lagi): ')).strip()

            if user_input2 == '1' or user_input2.lower() == 'keliling' or user_input2.lower() == 'keliling lingkaran':
                jari_jari = int(input('input nilai jari-jari unuk mengertahui keliling lingkaran: '))
                print(f'keliling lingkaran dari jari-jari {jari_jari} adalah: {round(keliling_lingkaran(jari_jari))}cm')
            elif user_input2 == '2' or user_input2.lower() == 'luas' or user_input2.lower() == 'luas lingkaran':
                jari_jari = int(input('input nilai jari-jari unuk mengertahui luas lingkaran: '))
                print(f'luas lingkaran dari jari-jari {jari_jari} adalah: {round(luas_lingkaran(jari_jari))}cm')
            else:
                print('dimohon untuk memilih opsi dengan benar')

        elif user_input == '4' or user_input.lower() == 'persegi':
            print('''
1. Keliling Persegi
2. Luas Persegi
''')    
            user_input3 = str(input('pilih opsi(lagi): ')).strip()
            if user_input3 == '1' or user_input3.lower() == 'Keliling' or user_input3.lower() == 'Keliling Persegi':
                sisi = int(input('masukan nilai S untuk sisi: '))
                print(f'nilai keliling persegi dari sisi {sisi} adalah: {persegi(sisi)}')
            elif user_input3 == '2' or user_input3.lower() == 'luas' or user_input3.lower() == 'luas Persegi':
                sisi_pertama = int(input('input nilai sisi pertama: '))
                sisi_kedua = int(input('input nilai sisi kedua: '))
                print(f'Luas dari perhitungan kedua sisi adalah: {persegi_luas(sisi_pertama,sisi_kedua)}cm')

        else:
            print('Tolong pilih opsi dengan benar')

        user = str(input('apakah ingin lanjut(y/n): '))
        if user != 'y':
            print('program ended')
            break
    except ValueError:
        print('input dengan benar,terimakasih')
        

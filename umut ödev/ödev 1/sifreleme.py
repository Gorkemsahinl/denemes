
sifre = input("Şifre gir: ")
print("Önce: " + sifre)
 
kayma = 8
dizi = ['=', '!', '^', '^^', '+', '&', '/', '<', '>', '-']
kilitsifre = ""
for karakter in sifre:
    if karakter.isalpha():  
        boyutbulma = ord('a') if karakter.islower() else ord('A')
        sifreli = chr((ord(karakter) - boyutbulma + kayma) % 26 + boyutbulma)
        kilitsifre += sifreli
     
    elif karakter.isdigit():
        i = int(karakter)
        kilitsifre += dizi[i] 
     



veri = 'veri.txt'
try:
    with open(veri, 'a') as file:
        file.write(kilitsifre + '\n')
finally:
    


 veri = 'veri.txt'

def sifreleriokuma(veri):
    try:
        with open(veri, 'r') as file:
            sonhali = file.readlines()
            if sonhali:
                print("Kaydedilmiş şifreler:")
                for okut in sonhali:
                    print(okut.strip())
    except IOError:
        print("Dosya okuma hatası.")

try:
    while True:
        okut = input("Şifre gir veya 'q' tuşuna basarak çık: ")

        if okut.lower() == 'q':
            sifreleriokuma(veri)
            break
finally:
    print("\n \n ")
    print("CONG")

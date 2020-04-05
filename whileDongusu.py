"""""
x=0
while x<5:
    ad=input("adınızı giriniz: ")
    x+=1
"""

""""
sayac=0
while sayac<5:
    sayi=int(input("sayı giriniz: "))
    sayac+=1
    print("Sayaç: ",sayac)
"""
""""
sayac=0
toplam=0
while sayac<5:
    sayi=int(input("sayı giriniz: "))
    sayac+=1
    toplam=toplam+sayi
print("Toplam: ",toplam)
"""
""""
sayac=0
toplam=0
while sayac<5:
    sayi=int(input("sayı giriniz: "))
    if sayi>0:
        sayac+=1
        toplam=toplam+sayi
print("Toplam değer: ",toplam)

"""
""""
sayi=0
toplam=0
while sayi>=0:
    sayi=int(input("pozitif sayı giriniz,negatif sayı işlemi sonlandırır. "))
    toplam=toplam+sayi
print("Toplam: ",toplam)
"""
""""
while True:
    a=input("değer giriniz")
    print(a)
"""
"""""
while True:
    a=int(input("Sayı giriniz: "))
    if a<0:
        break;
"""
""""
hak=0
while hak<3:
    soru=input("Sakarya'nın plaka kodu kaçtır? ")
    if soru!='54':
        hak=hak+1
        print("Bilemediniz Malesef",3-hak, "Hakkınız Kaldı")
        if hak==3:
            print("OYUN BİTTİ")
    else:
        print("Tebrikler",hak+1,". Hakkınızda Bildiniz")
        break;
"""
"""
toplam=0
while True:
    deger=int(input("Pozitif Değer Giriniz.(Çıkış İçin : 999)"))
    if deger<0:
        print("Malesef negatif sayı girdiniz.",deger,"Değeri İşleme Alınmadı.")
        continue
    if deger!=999:
        print("Eklenen Değer: ",deger)
        toplam=toplam+deger
    else:
        print("Döngü Sona Erdi")
        break;
print("Eklenen Değerlerin Toplamı: ",toplam)


cevap=0
dogru=0
while cevap<11:
    soru=input("Marmara Bölgesinin İllerini Yazınız")
    if soru=='Sakarya' or soru=='İstanbul' or soru=='Kocaeli' or soru=='Yalova' or soru=='Bursa' or soru=='Balıkesir'\
        or soru=='Çanakkale' or soru=='Edirne' or soru=='Tekirdağ' or soru=='Kırklareli' or soru=='Bilecik':
        dogru=dogru+1
    cevap=cevap+1
print(dogru,"Tane Doğrunuz Var")

"""
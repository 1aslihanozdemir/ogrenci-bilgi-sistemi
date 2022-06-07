def Basari(ortalama):

    if ortalama>=87 and ortalama<=100:
        harf_notu='AA'
        basari = "BAŞARILI"
    elif ortalama>=81 and ortalama<87:
        harf_notu='BA'
        basari = "BAŞARILI"
    elif ortalama>=74 and ortalama<81:
        harf_notu='BB'
        basari = "BAŞARILI"
    elif ortalama>=67 and ortalama<74:
        harf_notu='CB'
        basari = "BAŞARILI"
    elif ortalama>=60 and ortalama<67:
        harf_notu='CC'
        basari = "BAŞARILI"
    elif ortalama>=53 and ortalama<60:
        harf_notu='DC'
        basari = "KOŞULLU"
    elif ortalama>=46 and ortalama<53:
        harf_notu='DD'
        basari = "BAŞARISIZ"
    elif ortalama>=39 and ortalama<45:
        harf_notu='FD'
        basari = "BAŞARISIZ"
    else:
        harf_notu="FF"
        basari = "BAŞARISIZ"
    return harf_notu,basari

ogrenci_bilgileri={}
def Not_Gir():
    ad_soyad = input("Öğrenci adı-soyadı:")
    no = input("Öğrenci numarası:")
    not1 = input("Not1 :")
    not2 = input("Not2 :")
    not3 = input("Not3 :") 

    ortalama = (int(not1)+int(not2)+int(not3))/3
    t = Basari(ortalama)
    harf_notu=t[0]
    basari = t[1]

    with open("sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write("ÖĞRENCİ NUMARASI: "+no+" ÖĞRENCİ ADI SOYADI: "+ ad_soyad +" NOTLARI: "+str(not1)+" "+str(not2)+" "+str(not3)+" ORTALAMASI: "+str(ortalama)+" HARF NOTU: "+harf_notu+" BAŞARI DURUMU: "+basari+'\n')



def Not_Oku():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file:
        for i in file:
            print(i)


while True:
    islem = input("Yapmak İstediğiniz İşlemi Tuşlayınız.\n1-Not Gir\n2-Not Oku\n3-Çıkış")
    if islem == '1':
        Not_Gir()
    elif islem =='2':
        Not_Oku()
    else:
        break
# FONKSİYONLAR
"""
def selamlama(isim):  # fonksiyon tanımlama ve parametre atama
    print("Otelimize hoşgeldiniz Sayın", isim)


musteri = input("İsminiz : ")
selamlama(musteri)


def karsilama(ad="Baki"):  # fonksiyona default olarak bir isim tanımladık
    print("\n")
    print("Evinize hoşgeldiniz Sayın", ad)


karsilama()  # herhangi bir değer girmeden çalıştığında default olarak tanımlı değeri yazdırır

karsilama("Açelya")  # değer girildiğinde ise o değeri ad parametresi olarak algılayıp yazdırır

misafir = input("İsminiz : ")  # burda ise fonksiyona klavyeden alınan değişkeni parametre olarak gönderdik
karsilama(misafir)  # fonksiyon ad yerine misafir değişkenini yazdırır


def alan(a, b):
    A = a*b
    return A


def cevre(a, b):
    C = (a+b)*2
    return C


a = int(input("İlk kenar uzunluğunu giriniz: "))
b = int(input("İkinci kenar uzunluğunu giriniz: "))
print("Dikdörtgenin Alanı = ", alan(a, b))
print("Dikdörtgenin Çevresi =", cevre(a, b))


# yerel ve global değişken tanımı
def topla():
    x = int(input("Sayı1: "))
    y = int(input("Sayı2: "))
    return x+y


print(topla())
print(x)  # burada hata veriyor çünkü x değişkeni sadece def topla() fonsiyonu içinde tanımlandı
print(y)  # burada hata veriyor çünkü y değişkeni sadece def topla() fonsiyonu içinde tanımlandı


x = int(input("Sayı1: "))
y = int(input("Sayı2: "))


def topla():
    return x+y


print(topla())
print(x)  # burada hata verimiyor çünkü x değişkeni def topla() fonsiyonu öncesinde tanımlandı
print(y)print(topla())
print(x)  # burada hata verimiyor çünkü x değişkeni def topla() fonsiyonu öncesinde tanımlandı
print(y)  # burada hata verimiyor çünkü y değişkeni def topla() fonsiyonu öncesinde tanımlandı

# değişkeni fonksiyon içinde tanımlarken doğrudan global olduğunu da bildirebilirdik


def topla():
    global x, y
    x = int(input("Sayı1: "))
    y = int(input("Sayı2: "))
    return x+y


def cikarma():
    pass  # programlama yaparken henüz tanımlamadığımız fakat yapısal açıdan kullanacağımız fonk için geçici boş tanım


def carpma():
    return  # henüz tanımlamadığımız fakat yapısal açıdan kullanacağımız fonk için geçici boş işlem


def bolme():
    return x/y


print("Toplama İşlemi Sonucu =", topla())
print("Toplama İşlemi Sonucu =", cikarma())
print("Çarpma İşlemi Sonucu =", carpma())
print("Bölme İşlemi Sonucu =", bolme())
print("Hesaplamada Kullanılan 1.Sayı =", x)  # hata verimiyor çünkü x değ. def topla() fonk içinde de olsa global tanım
print("Hesaplamada Kullanılan 2.Sayı =", y)  # hata verimiyor çünkü y değ. def topla() fonk içinde de olsa global tanım


def kurdonusum(lira):
    return lira/32


tl = int(input("Kaç TL'lik Dolar Alacaksınız : "))
print(f"{tl} TL karşılığında {kurdonusum(tl)} Dolar alabilirsiniz.")


kurdonusum = lambda lira: lira/32  # yukarıda iki satırda tanımlanan fonk. daha kısa tanımlaması lambda ile yapılır

tl = int(input("Kaç TL'lik Dolar Alacaksınız : "))
print(f"{tl} TL ile {kurdonusum(tl)} Dolar alabilirsin.")
"""

def usalma(x, y):
    if y == 0:
        return 1
    else:
        return x*usalma(x, y-1)  # öz yinelemeli fonk (rekürsif)

x=3
y=4
print(usalma(x, y))
# usalma(3,4) = 3*usalma(3,3)
                # usalma(3,3) = 3*usalma(3,2) ... iç içe fonk ile en son usalma(3,4)=3*3*3*3*usalma(3,0) oluyor.
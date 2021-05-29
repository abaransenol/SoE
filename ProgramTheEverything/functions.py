def toplama(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam 

def cikarma(x,y):
    return x-y

def carpma(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam *= i
    return toplam 

def bolme(x,y):
    return x/y

def kalansizBolme(x,y):
    return x // y

def kalaniAl(x, y):
    return x % y

def usAl(x,y):
    return x ** y

def kokAl(x,y):
    return x ** (1/y)

def faktoriyelAl(x):
    doncekdeger = 1
    for i in range(2,x+1):
        doncekdeger *= i
    return doncekdeger

def ortalama(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    uzunluk = len(sayilar)
    return toplam / uzunluk
	












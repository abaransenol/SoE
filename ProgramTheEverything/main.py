import time, os
from functions import *

############################################## Tanımlamalar ##############################################

def devam():
    input("Devam etmek için herhangi bir şey yazın:")

def dogalSayi_input(iString):
    try:
        intDeger = int(input(iString))
        if intDeger < 0:
            print("Lütfen doğal sayı bir değer girin.")
            time.sleep(2)
            return ValueError
    except ValueError:
        print("Lütfen doğal sayı bir değer girin.")
        time.sleep(2)
        return ValueError
    except:
        print("Bilinmeyen hata. Program kapatılıyor...")
        return ModuleNotFoundError
    return intDeger

def int_input(iString):
    try:
        intDeger = int(input(iString))
    except ValueError:
        print("Lütfen tam sayı bir değer girin.\n")
        time.sleep(1)
        return ValueError
    except:
        print("Bilinmeyen hata. Program kapatılıyor...")
        return ModuleNotFoundError
    return intDeger

def float_input(iString):
    try:
        floatDeger = float(input(iString))
    except ValueError:
        print("Lütfen bir sayı değeri girin.\n")
        time.sleep(1)
        return ValueError
    except:
        print("Bilinmeyen hata. Program kapatılıyor...")
        return ModuleNotFoundError
    return floatDeger

def ekraniTemizle():
    if os.name == "nt":
        sil = os.system("cls")
    else:
        sil = os.system("clear")

############################################## Programın Başlangıcı ##############################################

hata = False
ekraniTemizle()
print("PoE - Program of Everything v0.1...\nHerşeyin programına hoşgeldiniz :)\nProgram açılıyor...")
time.sleep(2)

while True:
    if hata == True:
        break
    ekraniTemizle()
    print("""Seçimler:
    0- Kapat
    1- Hesap Makinesi""")

    while True:
        anaSecim = int_input("Seçiminizi girin:")
        if anaSecim == ValueError:
            continue
        elif anaSecim == ModuleNotFoundError:
            hata = True
        break
    
    if anaSecim == 0:
        print("Program kapatılıyor...")
        time.sleep(1)
        print("Hoşçakalın :)")
        break

############################################## Hesap Makinesi Bölümü ##############################################

    elif anaSecim == 1:
        print("Hesap makinesi açılıyor...")
        time.sleep(1)

        while True:
            if hata == True:
                break

            ekraniTemizle()
            print("""Seçimler:
    0- Geri
    1- Toplama (+)
    2- Çıkarma (-)
    3- Çarpma (x)
    4- Bölme (:)
    5- Kalansız Bölme (//)
    6- Kalanı Alma (%)
    7- Üs Al
    8- Kök Al
    9- Faktoriyel Hesaplama
    10- Alan Hesapları
    11- Hacim Hesapları""")

            while True:
                yanSecim = int_input("Seçiminizi girin:")
                if yanSecim == ValueError:
                    continue
                elif yanSecim == ModuleNotFoundError:
                    hata = True
                break

            if yanSecim == 0:
                print("Geri dönülüyor...")
                break

############################################## Toplama ve Çarpma ##############################################

            elif yanSecim == 1 or yanSecim == 3:
                while True:
                    sayiSayisi = int_input("İşlem yapacağınız toplam sayı miktarını yazın:")
                    if sayiSayisi < 2:
                        print("Bu kadar az sayıyı toplayamazsın")
                    elif sayiSayisi == ValueError:
                        continue
                    elif sayiSayisi == ModuleNotFoundError:
                        hata = True
                    break

                print("Eğer yanlış bir değer girdiysen, çıkmak için \"0\" yazabilirsin.")
                iptal = False

                sayilar = []
                for i in range(1,sayiSayisi+1):
                    while True:
                        sayi = float_input("{}. Sayıyı Girin:".format(i))
                        if sayi == 0.0:
                            print("Hesaplama iptal ediliyor.")
                            time.sleep(1)
                            iptal = True
                            break
                        if sayi == ValueError:
                            continue
                        elif sayi == ModuleNotFoundError:
                            hata = True
                        sayilar.append(sayi)
                        break
                    if iptal == True:
                        break

                if iptal == False:
                    islemlerDict = {1:toplama(*sayilar), 3:carpma(*sayilar)}
                    isaretlerDict = {1:"+", 3:"x"}

                    for i in islemlerDict.keys():
                        if yanSecim == i:
                            for j in range(0,len(sayilar)):
                                print(sayilar[j],isaretlerDict[i],end=" ")
                            print("=",islemlerDict[i])
                            devam()
############################################## Çıkarma , Bölme ve türevleri ##############################################
            elif yanSecim > 0 and yanSecim < 7:
                while True:
                    sayi1 = float_input("1. Sayıyı Girin:")
                    if sayi1 == ValueError:
                        continue
                    elif sayi1 == ModuleNotFoundError:
                        hata = True
                    break
                
                while True:
                    sayi2 = float_input("2. Sayıyı Girin:")
                    if sayi2 == 0 and yanSecim != 2:
                        print("Bir sayı 0'a bölünemez.")
                        time.sleep(1)
                        continue
                    elif sayi2 == ValueError:
                        continue
                    elif sayi2 == ModuleNotFoundError:
                        hata = True
                    break

                islemlerDict = {2:cikarma(sayi1,sayi2),4:bolme(sayi1,sayi2), 5:kalansizBolme(sayi1,sayi2), 6:kalaniAl(sayi1,sayi2)}
                isaretlerDict = {2:"-", 4:":", 5:"//", 6:"%"}

                for i in islemlerDict.keys():
                    if yanSecim == i:
                        print(sayi1, isaretlerDict[i], sayi2, "=", islemlerDict[i])
                        devam()

############################################## Üs Alma ##############################################

            elif yanSecim == 7:
                while True:
                    sayi1 = float_input("Tabanı girin:")
                    if sayi1 == ValueError:
                        continue
                    elif sayi1 == ModuleNotFoundError:
                        hata = True
                    break
                
                while True:
                    sayi2 = float_input("Üssü girin:")
                    if sayi2 == ValueError:
                        continue
                    elif sayi2 == ModuleNotFoundError:
                        hata = True
                    break
                
                print(sayi1, "üssü", sayi2, "=", usAl(sayi1, sayi2))
                devam()

############################################## Kök Alma ##############################################

            elif yanSecim == 8:
                while True:
                    sayi1 = float_input("Sayıyı girin:")
                    if sayi1 == ValueError:
                        continue
                    elif sayi1 == ModuleNotFoundError:
                        hata = True
                    break
                
                while True:
                    sayi2 = float_input("Kökün derecesini girin:")
                    if sayi2 == ValueError:
                        continue
                    elif sayi2 == ModuleNotFoundError:
                        hata = True
                    break
                
                print("{}. dereceden kök {} = {}".format(sayi2, sayi1, kokAl(sayi1, sayi2)))
                devam()

                    

                

                    


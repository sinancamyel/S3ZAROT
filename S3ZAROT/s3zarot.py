def rot13(metin):
    deger = ""
    for char in metin:
        if char.isalpha():
            if char.isupper():
                deger += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                deger += chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            deger += char
    return deger


def sezar(metin, atlama):
    deger = ""
    for char in metin:
        if char.isalpha():
            if char.isupper():
                deger += chr((ord(char) - 65 + atlama) % 26 + 65)
            else:
                deger += chr((ord(char) - 97 + atlama) % 26 + 97)
        else:
            deger += char
    return deger


def sifrele(metin):
    return rot13(sezar(metin, 3))


def desifrele(text):
    return sezar(rot13(text), 23)


cevap = int(input("Şifreleme için 1, Deşifreleme için 0: "))

if cevap == 1:
    metin = input("Şifrelemek istediğniz metni giriniz: ")
    sifrelenmis = sifrele(metin)
    print("Şifrelenmiş metin: "+sifrelenmis)

elif cevap == 0:
    metin = input("Deşifrelemek istediğiniz metni giriniz: ")
    desifrelenmis = desifrele(metin)
    print("Deşifrelenmiş metin: "+desifrelenmis)
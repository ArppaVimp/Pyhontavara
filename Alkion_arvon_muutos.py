#alkuperäinen lista

lista = [1,2,3,4,5]

while True:
    #Tulostetaan alkuperäinen lista
    print("Alkuperäinen lista: ", lista)

    #Kysy käyttäjältä indeksi mihin uusi arvo sijoitetaan
    indeksi = int(input("Anna alkion indeksi tai -1 jos haluat lopettaa ohjelman suorituksen. "))

    #Tarkistetaan jos ohjelman suoritus halutaan lopettaa
    if indeksi == -1:
        break

    #Tarkistetaan onko indeksi OK
    if indeksi < 0 or indeksi >= len(lista):
        print("Virheellinen indeksi.")
    else:
        uusi_arvo = int(input("Anna uusi arvo listaan. "))
        lista[indeksi] = uusi_arvo

    print("Tässä uusi lista: ", lista)



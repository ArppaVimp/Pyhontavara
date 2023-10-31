def kaikki_vaarinpain(lista2):
    for merkki in lista2:
        kaannetutMerkit = merkki[::-1]
        #kaannetutMerkit.reverse()
        print(kaannetutMerkit, " ", end="")
        i = len(kaannetutMerkit) - 1
        print(kaannetutMerkit[i])
        
    
    #käännetyt_merkit = [merkki[::-1] for merkki in merkkijonolista]
    #käännetyt_merkit.reverse()  # Käännetään listan järjestys
    #return käännetyt_merkit

# Esimerkki funktion käytöstä
lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
kaikki_vaarinpain(lista)
#lista2 = kaikki_vaarinpain(lista)
#print(lista2)


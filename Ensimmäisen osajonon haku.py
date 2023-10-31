#Tee ohjelma, joka kysyy käyttäjältä merkkijonoa ja yksittäistä merkkiä. Ohjelma tulostaa merkkijonosta löytyvän ensimmäisen 
#kolmen merkin pituisen osajonon, 
#jonka alkukirjain on käyttäjän syöttämä merkki. Voit olettaa, että merkkijono on vähintään kolmen merkin pituinen.
#
#Tee edellisestä ohjelmasta laajennettu versio, joka tulostaa kaikki merkkijonon sisältämät kolmen merkin pituiset osajonot, joiden alkukirjain on käyttäjän syöttämä merkki. 
#Voit olettaa, että merkkijono on vähintään kolmen merkin pituinen.

#mjono = "saippuakauppias"
mjono = input("Sana: ")
pituus = len(mjono)


#while True:
osa = input("Merkki: ")
kohta = mjono.find(osa)
if kohta >= 0 and pituus > kohta + 3:
    #print(f"Löytyi kohdasta {kohta}")
    print(mjono[kohta:kohta+3])
#else:
    #print("Ei löytynyt")
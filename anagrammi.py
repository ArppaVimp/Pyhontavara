
def anagrammi(sana1, sana2):
    # Tarkistetaan, ovatko merkkijonot anagrammeja
    return sorted(sana1) == sorted(sana2)


sana1 = input("Anna eka sana ")
sana2 = input("Anna toka sana ")
tulos = anagrammi(sana1, sana2)
print(tulos)  

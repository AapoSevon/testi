# Tee ohjelma, joka kysyy käyttäjältä 3 lukua ja laskee niiden keskiarvon

print("Ohjelma kysyy 3 lukua ja laskee niiden keskiarvon")
luku1 = int(input("anna 1.luku\n"))
luku2 = int(input("anna 2.luku\n"))
luku3 = int(input("anna 3.luku\n"))

summa = luku1 + luku2 +luku3
keskiarvo = summa / 3

print("lukujen" ,luku1,",", luku2, "ja", luku3, "keskiarvo on","{:.2f}".format(keskiarvo), ".")
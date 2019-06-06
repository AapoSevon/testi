#Tee ohjelma joka kysyy käyttäjältä luvun ja tulostaa kympin kertotaulun

print("Tämä ohjelma kysyy luvun ja esittää sen kymmenen kertotaulun")
luku = int(input("anna luku\n"))

for i in range(0,13):
    print(i, "kertaa", luku, "on", i*luku)
    
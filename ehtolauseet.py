#Tehdään ohjelma, joka kysyy käyttäjältä luvun, ja kerrotaan, onko se positiivinen, negatiivinen vai nolla.

luku = int(input("Anna luku:\n"))

if luku > 0:
    print("luku on positiivinen")
    if luku > 10:
        print("luku on suurempi kuin kymmenen")
elif luku < 0:
    print("luku on negatiivinen")
    if luku < -10:
        print("luku on pienempi kuin miinus kymmenen")
else:
    print("luku on nolla")
print("ohjelman suoritus päättyy")
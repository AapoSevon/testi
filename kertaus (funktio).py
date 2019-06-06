#Kertausharjoitus
#Tehdään ohjelma joka kysyy käyttäjältä kaksi lukua. a: laske summa, b: laske erotus, c: laske tulo, laske osamäärä.
#Jos käyttäjä kirjoittaa stop, ohjelman suoritus päättyy.

def summa (a, b):
    return a + b

def erotus (a, b):
    return a - b
def tulo (a, b):
    return a * b
def osamäärä (a,b):
    return a / b
def main():
    
    #tulos = summa(2, 4)
    luku1 = float(input("Anna luku 1:\n"))
    luku2 = float(input("Anna luku 2:\n"))
    
    komento = input("a: summa, b: erotus, c: tulo, d: osamäärä\n")
    
    if komento == "a":
        print(summa(luku1, luku2))
    elif komento == "b":
        print(erotus(luku1, luku2))
    elif komento == "c":
        print(tulo(luku1, luku2))
    elif komento == "d":
        print (osamäärä(luku1, luku2))
    else:
        print("väärä komento")
    

main()
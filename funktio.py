# Tee ohjelma joka kysyy käyttäjän nimen
#Tämän jälkeen ohjelma kysyy kuinka monta kertaa tervehditään
# Ohjelmassa on pääohjelma main(), ja apufunktio tulosta (nimi, kertaa), jota kutsutaan main()funktiont sis

def tulosta(nimi_funktiossa, kertaa):
    for i in range(kertaa):
        print("Terve", nimi_funktiossa)
    print("Tässä tervehdykset")


def main():
    nimi = input("kerro nimesi:\n")
    lkm = int(input("kuinka monta kertaa haluat sinua tervehdittävän?\n"))
    
    tulosta(nimi, lkm)
    
    print("main-funktio suoritettu")


main() 
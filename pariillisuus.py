#Ohjelma kertoo onko käyttäjän antama luku parillinen vai pariton
#Jakojäännöksen saa %-operaattorilla
# 10 % 2 -> 0
#9 % 2 -> 1

luku = int(input("Anna luku:\n"))

if (luku % 2) == 0:
    print("luku on parillinen")
else:
    print("luku on pariton")
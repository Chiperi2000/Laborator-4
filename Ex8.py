#Ghicește numărul!
#Scrieți un program care va genera un număr aleatoriu (google it ;) ) și va cere utilizatorului să ghicească numărul! Programul se va termina când numărul va fi ghicit.
#   - contorizați numărul de încercări 
#   - adăugați mesaje ajutătoare ("prea mic" sau "prea mare")
#   - adăugați mesaj care să indice intervalul curent în care se află numărul, conform încercărilor utilizatorului

import random

x = random.randint(0,100)

y = int(input("Introduceti un numar intre 0 si 100: "))
incercari = 1

while y != x:
    print("Nu ati ghicit numarul!")
    if y < x:
        print("Numarul introdus este prea mic.")
        y = int(input("introduceti alt numar: "))
        incercari += 1
    if y > x:
        print("Numarul introdus este prea mare")
        y = int(input("Introduceti alt numar: "))
        incercari += 1
    else:
        print("Ati ghicit corect!\nNumarul este",y,end = '!\n')
        print("Ati ghicit in",incercari,"incercari")
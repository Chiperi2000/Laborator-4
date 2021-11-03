#Ghicește numărul!
#Scrieți un program care va genera un număr aleatoriu (google it ;) ) și va cere utilizatorului să ghicească numărul! Programul se va termina când numărul va fi ghicit.
#   - contorizați numărul de încercări 
#   - adăugați mesaje ajutătoare ("prea mic" sau "prea mare")
#   - adăugați mesaj care să indice intervalul curent în care se află numărul, conform încercărilor utilizatorului

import random

numar_generat = random.randint(0,100)
numar_introdus = int(input("Ghiceste un numar intre 0 si 100: "))
incercari = 0

while numar_introdus != numar_generat:
    if numar_generat > numar_introdus:
        print("Numarul introdus este prea mic!")
        numar_introdus = int(input("Incearca din nou: "))
        incercari = incercari + 1
    elif numar_generat < numar_introdus:
        print("Numarul introdus este prea mare!")
        numar_introdus = int(input("Incearca din nou: "))
        incercari = incercari + 1

print("Ai ghicit numarul!\nNumar de incercari:",incercari)
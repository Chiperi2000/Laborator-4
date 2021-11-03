#Construiesc piramida de sus in jos
#Consider fiecare etaj (de sus in jos) ca fiind construit prin adaugarea unei caramizi
#Exemplu (6 caramizi) - constructie de sus in jos:
# - primul etaj este format din o caramida: 6-1 => mai raman 5 caramizi
# - al doilea etaj este format din 2 caramizi: 5-2 => mai raman 3 caramizi
# - al treilea etaj este format din 3 caramizi: 3-3 => mai raman 0 caramizi  


caramizi = int(input("Introduceti numarul de caramizi: "))
inaltime = 0
while caramizi > inaltime:
    inaltime += 1
    caramizi -= inaltime
print("Inaltimea caramizii este: ", inaltime)
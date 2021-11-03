#Scrieți un program care va cere utilizatorului să introducă o parolă pentru a merge mai departe! 

print("Creare parola: ")
parola_1 = input("Introduceti parola: ")
parola_2 = input("Confirmati parola: ")

while parola_1 != parola_2:
    print("Confirmare esuata!")
    parola_2 = input("Reintroduceti parola: ")
    if parola_1 == parola_2:
        print("Parola a fost salvata!")

print("\nAutentificare: \n")
parola_3 = input("Introduceti parola creata:")
incercari = 1

while parola_3 != parola_1:
    incercari = incercari + 1
    if incercari < 3:
        parola_3 = input("Introduceti parola creata:")
    elif incercari == 3:
        parola_3 = input("Ultima incercare!: ")
    elif incercari > 3:
        print("Cont blocat!")
        break
    
else:
    print("Autentificare reustia!")



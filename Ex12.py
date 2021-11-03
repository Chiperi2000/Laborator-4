#Scrieți un program care va modifica toate vocalele în majuscule.

text = input("Scrieti textul: ")
for i in text:
    if i in 'aeiou':
        print(i.upper(), end='',)
    else:
        print(i,end='')
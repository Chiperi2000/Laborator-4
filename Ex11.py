#Scrieți un program care va afișa doar consoanele dintr-un text citit din consolă.

text = input("Scrieti textul: ")
for i in text:
    if i in 'aeiouAEIOU':
        print(' ', end='')
    else:
        print(i,end='')
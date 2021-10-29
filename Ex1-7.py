#Ex.1: Ce va afișa următorul program?
print("Exercitiul numarul 1:")

x = 5 
y = 10 
z = 8 

print(x > y) 
print(y > z)
print("\nExercitiul numarul 2:")

#Ex.2: Ce va afișa următorul program?
x, y, z = 5, 10, 8 

print(x > z) 
print((y - 5) == x)
print("\nExercitiul numarul 3:")

#Ex.3: Ce va afișa următorul program?
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)
print("\nExercitiul numarul 4:")

#Ex.4: Ce va afișa următorul program?
x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else: print("else")
print("\nExercitiul numarul 5:")

#Ex.5: Ce va afișa următorul program?
x = "1"

if x == 1:
	print("one")
elif x == "1":
	if int(x) > 1:
        	print("two")
	elif int(x) < 1:
        	print("three")
	else:
        	print("four")
if int(x) == 1:
	print("five")
else:
	print("six")
print("\nExercitiul numarul 6:")

#Ex.6: Ce va afișa următorul program?
x = 1
y = 1.0
z = "1"

if x == y:
	print("one")
if y == int(z):
	print("two")
elif x == y:
	print("three")
else:
	print("four")
print("\nExercitiul numarul 7:")
#Ex.7: Ce va afișa următorul program?

while True:
    print("I'm stuck inside a loop.")

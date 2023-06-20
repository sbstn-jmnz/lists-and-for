fruits = ["apple", "banana", "cherry", "strawberry", "kiwi"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

print("------------------------------------------")

position = 0
while position < len(fruits):
  print(fruits[position])
  position += 1

# Python viene con un iterador llamado for. El for funciona para todas las colecciones (listas, diccionarios y las tuplas), secuencias y strings.

print("------------------------------------------")

for fruit in fruits:
  print(fruit)

print("------------------------------------------")

instruments = ["Guitar", "Drums", "Bass", "Piano"]
for instrument in instruments:
  print(instrument)

print("------------------------------------------")

for letter in "Banana":
  print(letter)

print("------------------------------------------")

# Podemos detener el for con la palabra reservada break
fruits = ["apple", "banana", "cherry", "strawberry", "kiwi"]

for fruit in fruits:
  if fruit == "banana":
    break
  print(fruit)

print("------------------------------------------")

# Podemos saltar una vuelta con la palabra reservada continue
fruits = ["apple", "banana", "cherry", "strawberry", "kiwi"]

for fruit in fruits:
  if fruit == "banana":
    continue
  print(fruit)
# Las listas en python permiten guardar varios items o valores en una sola variable.
# Las listas son UNA de las estructuras de datos que tiene python. Otras que veremos más adelante son las Tuplas, Sets y los Diccionarios.
# Las listas se pueden crear con los corchetes []

fruits = ["apple", "bananas", "cherry"]

print(fruits)

# Los elementos en una lista están ordenados por su índice que parte en cero.
print(fruits[0]) # apple
print(fruits[2]) # cherry

# Si intentamos acceder a un elemento fuera del rango, obtendremos un error

# fruits[4] # error indice fuera de rango

# Con índices negativos contamos los elementos en orden inverso. De atrás hacia adelante
print(fruits[-2])

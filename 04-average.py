grades = [3,5,4,6,4,5,1,2,3,4,5]

# Acumulador
sum = 0

# Recorremos la lista y vamos sumando su valor en el acumulador
for grade in grades:
  sum += grade

# Ya tenemos la suma, solo falta dividir por la cantidad de notas
print(f"El promedio de las notas es {sum/len(grades)}")
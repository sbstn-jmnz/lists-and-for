# Cada arreglo corresponde a las calificaciones de un estudiante
grades_list = [[2.9, 2.7, 1.7, 4.3, 3.4],[3.9, 4.7, 2.7, 4.3, 3.4],[4.9, 2.7, 3.7, 4.3, 3.4],[5.9, 2.7, 3.7, 2.3, 1.4],[1.9, 4.7, 4.7, 2.3, 3.6]]

# Se pide calcular el promedio de cada estudiante en un nuevo arreglo llamado averages
averages = []

for grades in grades_list:
  sum = 0
  for grade in grades:
    sum += grade
  average = sum/len(grades)
  averages.append(average)

print(averages)


print("-------------------------------")

for num_a in [1,2,3,4,5,6,7,8,9,10]:
  print(f"La tabla del {num_a}")
  for num_b in [1,2,3,4,5,6,7,8,9,10]:
    print(f"{num_a} x {num_b} = {num_a*num_b}")
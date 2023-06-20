dogs =  []
menu_option = ""
while menu_option != "3":
    print("Bienvenido al Tinder de Perritos")
    print("1. Agregar cachorros")
    print("2. Ver cachorritos")
    print("3. Salir")
    menu_option = input()

    if menu_option == "1":
      dog = []
      name = input("Ingrese el Nombre de su pulgoso: ")
      age = input("Ingrese la edad de su pulgoso: ")
      breed = input("Ingrese la raza de su pulgoso: ")
      dog.append(name)
      dog.append(age)
      dog.append(breed)
      dogs.append(dog)

      print(f"{name} agregado completamente")
    
    elif menu_option == "2":
      index = 0
      while index < len(dogs):
        print("----------------------")
        print(f"Cachorro llamado {dogs[index][0]}")
        print(f"Edad: {dogs[index][1]}")
        print(f"Raza: {dogs[index][2]}")
        index += 1
    
    elif menu_option == '3':
      print("Gracias por jugar.")

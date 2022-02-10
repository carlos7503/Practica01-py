print("Este es mi primer programa para la práctica de las instrucciones básicas")
edadlegal=18
inicio=0
nombre=input("¿Cuál es tu nombre?  ")
edad=int(input("¿Cuál es tu edad?  "))
if edad >= edadlegal:
    print(f"{nombre}, Felicidades, eres mayor de edad")
    cuenta=int(input("cuántas repeticiones se require? "))
    for inicio in range(cuenta):
        print(inicio+1)
    
else:
    print(f"lo siento {nombre} no cumple con la edad suficiente")


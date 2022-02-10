edadlegal = 18
edad = int(input("¿Cuál es su edad? "))
if edad > 0 and edad < 100:
    if edad >=18:
        print(f"felicidades eres mayor de edad, tienes; {edad}")
    else:
        print(f"te faltan {edadlegal - edad} años para cumplir la mayoría de edad")
else:
    print("Edad incorrecta")
print("Final del proceso")


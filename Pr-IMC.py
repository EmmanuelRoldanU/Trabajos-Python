nombre = input("Escriba su nombre porfavor: ")
ap = input("Escriba su apellido paterno porfavor: ")
am = input("Escriba su pallido materno porfavor: ")

#codigo de introducir edad
while True:
    try:
        edad = int(input("Introduce tu edad:"))
        if 0 <= edad <= 120:
            break  # Salir del bucle si se proporciona una edad válida
        else:
            print("Por favor, introduce una edad válida.")
    except ValueError:
        print("Por favor, introduce una edad.")


#codigo para la estatura
while True:
    try:
        numero1 = float(input("Introduce tu estatura en metros: "))
        if 0 <= numero1 <= 2.5:
            break  # Salir del bucle si se proporciona un número válido en el rango
        else:
            print("Por favor, introduce una estatura correcta.")
    except ValueError:
        print("Por favor, introduce una estatura correcta: ")
    

#codigo para el peso
while True:
    peso = input("Introduce tu peso en kilogramos: ")
    try:
        numero2 = float(peso)
        break
    except ValueError:
        print("Por favor, introduce un peso valido.")


#formula para realizar convercion i obtener el IMC
IMC = numero2 / numero1**2

print((nombre)+(" ")+(ap)+(" ")+(am))
print(f"Tu edad es de: {edad}")
if edad < 18: print("Uste es menor de edad")

else: print("Usted es mayor de edad")


print(f"Tu estatura es: {numero1}mts")
print(f"Tu peso es: {numero2} Kg")

print("IMC: " + str(IMC))

print("Su estado de salud es")

if IMC >= 0 and IMC <=15.90 : print ("Desnutricion, se recomienda atencion urgente con el nutriologo y examenes medicos")
elif IMC >= 16.00 and IMC <16.99 : print("Falto de paso, se recominda atencion con un nutriologo")
elif IMC >= 17.00 and IMC <18.49 : print("Delgado, se recomienda estar atento a la alimentacion")
elif IMC >= 18.50 and IMC <24.99 : print("Normal")
elif IMC >= 25.00 and IMC <29.99 : print("Poco pasado de peso, se recomienda estar atento a la alimentacion")
elif IMC >= 30.00 and IMC <34.99 : print("Obeso, se recomienda atencion con un nutriologo")
elif IMC >= 35.00 and IMC <39.00 : print("Sobre Peso, atencion urgente con el nutriologo y examenes de salud")
elif IMC >= 40.00: print("Panteon Seguro, F en el chat")


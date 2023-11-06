# Programa 1: Identificar la longitud de una palabra
while True:
    palabra = input("Ingresa una palabra: ")
    N = len(palabra)

    if 4 <= N <= 8:
        print("La palabra es correcta.")
    elif N < 4:
        print(f"Hacen falta letras, solo tiene {N} letras.")
    else:
        print(f"Sobran letras, tiene {N} letras.")

    respuesta = input("¿Deseas realizar otro cálculo? (s para repetir, aplasta cualquier letra para continuar): ")
    if respuesta.lower() != 's':
        break





# Separación visual entre programas
print("\n" + "="*40 + "\n")





# Programa 2: Identificar el cuadrante de coordenadas
while True:
    # Solicitar al usuario que ingrese la coordenada X
    while True:
        try:
            x = float(input("Ingrese la coordenada X: "))
            break  # Salir del bucle interior si se ingresa un número válido, se agrgo limitante a puros numeros y no letras
        except ValueError:
            print("Debes ingresar un número válido para la coordenada X.")

    # Solicitar al usuario que ingrese la coordenada Y
    while True:
        try:
            y = float(input("Ingrese la coordenada Y: "))
            break  # Salir del bucle interior si se ingresa un número válido, se agrego limitante a numero y no letras
        except ValueError:
            print("Debes ingresar un número válido para la coordenada Y.")

    if x == 0 or y == 0:
        print("Ambas coordenadas son iguales a 0, el punto no se encuentra en ningún cuadrante.")
    else:
        if x > 0 and y > 0:
            cuadrante = "I"
        elif x < 0 and y > 0:
            cuadrante = "II"
        elif x < 0 and y < 0:
            cuadrante = "III"
        else:
            cuadrante = "IV"
        print(f"El punto se encuentra en el cuadrante {cuadrante}.")

    respuesta = input("¿Deseas realizar otro cálculo? (s para repetir, aplasta cualquier letra para terminar.): ")
    if respuesta.lower() != 's':
        break
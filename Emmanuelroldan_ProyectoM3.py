# Importamos la librería random para generar números aleatorios y matplotlib para visualizar los resultados
import random
import matplotlib.pyplot as plt

# Función para inicializar la máquina de Galton con canicas en la parte superior
def inicializar_canicas(cantidad):
    return [1] * cantidad                                 # Creamos una lista con la cantidad especificada de canicas (inicialmente en la parte superior)

# Función para simular el movimiento de las canicas a través de los niveles de la máquina de Galton
def simular_galton(canicas, niveles):
    for nivel in range(niveles):
        nuevas_canicas = []
        for canica in canicas:
            movimiento = random.choice([-1, 1])           # -1 para izquierda, 1 para derecha
            nuevas_canicas.append(canica + movimiento)    # Movemos la canica según la dirección aleatoria
        canicas = nuevas_canicas                          # Actualizamos la posición de las canicas para el siguiente nivel
    return canicas

# Función para visualizar los resultados utilizando Matplotlib
def visualizar_resultados(resultados):
    plt.hist(resultados, bins=range(min(resultados), max(resultados) + 2), align='left', rwidth=0.8)
    plt.title('Simulación de la Máquina de Galton')
    plt.xlabel('Niveles')
    plt.ylabel('Cantidad de Canicas')
    plt.show()

# Uso de las funciones
cantidad_canicas = 3000
niveles_galton = 12

# Inicializamos las canicas en la parte superior de la máquina
canicas_iniciales = inicializar_canicas(cantidad_canicas)

# Simulamos el movimiento de las canicas a través de los niveles
resultados_simulacion = simular_galton(canicas_iniciales, niveles_galton)

# Visualizamos los resultados
visualizar_resultados(resultados_simulacion)

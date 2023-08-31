# Importar el módulo 'math' para realizar cálculos matemáticos, incluyendo la raíz cuadrada.
import math

# Definir una función para calcular la distancia entre dos puntos en un plano cartesiano.
def calcular(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Definir una función para encontrar el par de puntos más cercanos en un conjunto de puntos.
def encontrar_par_mas_cercano(puntos):
    # Inicializar la distancia mínima como infinito y el par más cercano como vacío.
    min_distancia = float('inf')
    par_mas_cercano = None

    # Iterar sobre todos los pares de puntos posibles.
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            # Calcular la distancia entre los puntos i y j.
            distancia = calcular(puntos[i], puntos[j])
            
            # Si la distancia calculada es menor que la distancia mínima actual,
            # actualizar la distancia mínima y el par más cercano.
            if distancia < min_distancia:
                min_distancia = distancia
                par_mas_cercano = (puntos[i], puntos[j])

    # Devolver el par de puntos más cercanos y la distancia entre ellos.
    return par_mas_cercano, min_distancia

# Definir un decorador que imprimirá mensajes antes y después de ejecutar la función decorada.
def distancia_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calculando distancia...")
        result = func(*args, **kwargs)
        print("Distancia calculada.")
        return result
    return wrapper

# Aplicar el decorador a la función 'pares_cercanos'.
@distancia_decorator
def pares_cercanos(*args, **kwargs):
    # Llamar a la función 'encontrar_par_mas_cercano' con el primer argumento pasado a 'pares_cercanos'.
    par_mas_cercano, min_distancia = encontrar_par_mas_cercano(args[0])
    return par_mas_cercano, min_distancia




puntos = []

for i in range(4):
  numero1 = input("escribe el numero 1 de la coordenada numero" + "" +  str(i + 1))
  numero2 = input("escribe el numero 2 de la coordenada numero" + "" +  str(i + 1))

  tupla = (int(numero1) , int(numero2))
  puntos.append(tupla)


par_mas_cercano, min_distancia = pares_cercanos(puntos)
print("Los puntos más cercanos son:", par_mas_cercano)
print("La distancia entre ellos es:", min_distancia)

def imprimir_saludo():
    print("Hola, bienvenido/a.")
    print("Espero que estés teniendo un buen día.")

def imprimir_fecha():
    import datetime
    fecha_actual = datetime.datetime.now()
    print("Hoy es", fecha_actual.strftime("%d/%m/%Y"))

def obtener_lista_numeros():
    numeros = []
    cantidad_numeros = int(input("Ingrese la cantidad de números que desea ingresar: "))
    for i in range(cantidad_numeros):
        numero = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)
    return numeros

obtener_lista_numeros()
def generar_numero_aleatorio():
    import random
    numero = random.randint(1, 100)
    return numero

def imprimir_pi():
    import math
    print("El valor de Pi es:", math.pi)

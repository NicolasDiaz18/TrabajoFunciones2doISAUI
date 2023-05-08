def saludar(nombre, saludo="Hola"):
    print(saludo + ", " + nombre)
    
def multiplicar_por_n(numero, n=2):
    resultado = numero * n
    return resultado

def suma(a, b=0):
    #Función que retorna la suma de dos números, si solo se ingresa un número, asume que el segundo es 0.
    return a + b

def comparar_numeros(numero, referencia=0):
    #Compara un número dado con una referencia (por defecto, cero)
    if numero > referencia:
        print(f"{numero} es mayor que {referencia}")
    elif numero < referencia:
        print(f"{numero} es menor que {referencia}")
    else:
        print(f"{numero} es igual a {referencia}")

def calcular_area_rectangulo(base, altura=10):
    area = base * altura
    return area

calcular_area_rectangulo()
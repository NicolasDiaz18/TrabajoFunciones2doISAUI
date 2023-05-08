"""resultado = 0
def suma (a, b):
    resultado = a + b
    return resultado
print (suma(4, 5))
"""

"""def division (d, e):
    if (e == 0):
        print ("No se puede dividir por 0")
    else:
        cociente = (d/e)
    return cociente
print (division(10, 5))
    """
    
"""def mayor (primero, segundo):
    if(primero > segundo):
        print("El primero es mayor")
    elif(primero < segundo):
        print("El segundo es mayor")
    else:
        print("Son iguales")
    return mayor
print(mayor(1, 2))"""
 
       
"""def pares(f):
    if(f % 2 == 0):
        print("El num ingresado es par")
    else:
        print("El num ingresado es impar")
    return pares
print(pares(5))"""

def vecMayor (vec):
    for i in range (0, len(vec)):
        if i == 0:
            mayor = vec[i]
        if (vec[i] > mayor):
            mayor = vec[i]
    return mayor

vec = [1, 30, 20, 15, 100, 4, 6, 40]
print(vecMayor(vec))

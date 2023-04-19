'''
Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la 
serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

'''
# Importación de la función calculoDelFactorial desde el archivo "Cuarto_punto"
from Cuarto_punto import calculoDelFactorial
# Importación de la libreria math de python
import math

def funcionExponencial(x:float,n:int) -> float:
    """Función que calcula el valor aproximado de la función exponencial de un parámetro x haciendo uso de los primeros n terminos de la 
        serie de Maclaurin.

    Args:
        x (float): Primer parámetro.
            Número al cual se le calculara la función exponencial 
        n (int): Segundo parámetro.
            Número que indicará cuantos terminos de la serie de Maclaurin se usarán para realizar el cálculo

    Returns:
        float: exp
    """
    exp : float = 0
    for i in range (n):
        # Bucle for que calcula el valor aproximado de la función exponencial usando la serie de Maclaurin 
        exp += (x**i)/(calculoDelFactorial(i))
        error = abs(exp - math.exp(x))
        # Condicional que determina la cantidad de terminos necesarios para que la aproximación de la función por series de Maclaurin sea menor al 0.1% de error  
        if error >= 0.001:
            terminos = "No hay terminos suficientes" 
        else:
            terminos = i + 1 
            break  
    return "La aproximación de la funcion exponencial es: {}\nEl valor real de la función exponencial es: {}\nEl error entre el valor aproximado y el valor real es: {}\nEl número de terminos necesarios para que el error sea menor a 0.1% es: {}".format(exp,math.exp(x),error,terminos)

if __name__ == "__main__":
    x = float(input("Ingrese el valor de x: "))
    n = int(input("Ingrese el número de terminos para calcular la serie de Maclaurin: "))
    # Llamado de la función fucionExponencial y envío de los parámetros x y n 
    exponencial = funcionExponencial(x,n)
    print(exponencial)
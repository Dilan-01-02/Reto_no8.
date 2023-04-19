'''
Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la 
serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

'''
# Importación de la función calculoDelFactorial desde el archivo "Cuarto_punto"
from Cuarto_punto import calculoDelFactorial
# Importación de la libreria math de python
import math

def funcionSeno(x:float,n:int) -> float:
    """Función que calcula el valor aproximado de la función seno de un parámetro x haciendo uso de los primeros n terminos de la 
        serie de Maclaurin.

    Args:
        x (float): Primer parámetro.
            Número al cual se le calculara la función seno
        n (int): Segundo parámetro.
            Número que indicará cuantos terminos de la serie de Maclaurin se usarán para realizar el cálculo

    Returns:
        float: sen
    """
    sen : float = 0 
    for i in range (n):
        # Bucle for que calcula el valor aproximado de la función seno usando la serie de Maclaurin
        sen = sen + (((-1)**i)*((x**(2*i+1))/calculoDelFactorial(2*i+1)))
        error = abs(sen - math.sin(x))
        # Condicional que determina la cantidad de terminos necesarios para que la aproximación de la función por series de Maclaurin sea menor al 0.1% de error  
        if error >= 0.001:
            terminos = "No hay terminos suficientes" 
        else:
            terminos = i + 1
            break  
    return "La aproximación de la función seno es: {}\nEl valor real de la función seno es: {}\nEl error entre el valor aproximado y el valor real es: {}\nEl número de terminos necesarios para que el error sea menor a 0.1% es: {}".format(sen,math.sin(x),error,terminos)
        
    return sen
    
if __name__ == "__main__":
    x = float(input("Ingrese el valor de x: "))
    n = int(input("Ingrese el número de terminos para calcular la serie de Maclaurin: "))
    # Llamado de la función fucionSeno y envío de los parámetros x y n 
    seno = funcionSeno(x,n)
    print(seno)
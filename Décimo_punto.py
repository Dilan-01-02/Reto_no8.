'''
Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la 
serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

'''
# Importación de la libreria math de python
import math

def funcionArcotangente(x:float,n:int) -> float:
    """Función que calcula el valor aproximado de la función arcotangente de un parámetro x en el rango [-1, 1] haciendo uso de los primeros n terminos de la 
        serie de Maclaurin.

    Args:
        x (float): Primer parámetro.
            Número al cual se le calculara la función arcotangente
        n (int): Segundo parámetro.
            Número que indicará cuantos terminos de la serie de Maclaurin se usarán para realizar el cálculo

    Returns:
        float: arctan
    """
    arctan : float = 0 
    for i in range (n):
        # Bucle for que calcula el valor aproximado de la función arcotangente usando la serie de Maclaurin
        arctan = arctan + (((-1)**i)*((x**(2*i+1))/(2*i+1)))
        error = abs(arctan - math.atan(x))
        # Condicional que determina la cantidad de terminos necesarios para que la aproximación de la función por series de Maclaurin sea menor al 0.1% de error  
        if error >= 0.001:
            terminos = "No hay terminos suficientes" 
        else:
            terminos = i + 1
            break  
    return "La aproximación de la función arcotangente es: {}\nEl valor real de la función arcotangente es: {}\nEl error entre el valor aproximado y el valor real es: {}\nEl número de terminos necesarios para que el error sea menor a 0.1% es: {}".format(arctan,math.atan(x),error,terminos)
    return arctan
    
if __name__ == "__main__":
    bandera : bool = True 
    while bandera or x<-1 or x>1:
        # Bucle while que pide el valor de x y comprueba que este se encuentre en el rango [-1, 1]
        bandera = False
        x = float(input("Ingrese el valor de x (debe estar en el rango [-1, 1]): "))
        if x<1 and x>1:
            print("El número ingresado no se encuentra en el rango [-1, 1]")
    n = int(input("Ingrese el número de terminos para calcular la serie de Maclaurin: "))
    # Llamado de la función fucionArcotangente y envío de los parámetros x y n 
    arcotangente = funcionArcotangente(x,n)
    print(arcotangente)
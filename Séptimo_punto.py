'''
Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

'''
def tablaDeMultiplicar(x:int):
    """Función que genera la tabla de multiplicar de un parámetro x  

    Args:
        x (int): Primer parámetro.
            Número al cual se le generará la tabla de multiplicar 
    """
    mult : int = 0 
    for i in range (1,11):
        # Bucle for que calcula el valor de la multiplicación entre el parámetro x y el número entre 1 y 10
        mult = mult + x
        print( str(x)+" * "+str(i)+" = "+str(mult))
    
if __name__ == "__main__":
    for i in range (1,10):
        # Bucle for que muestra las tablas de multiplicar desde el 1 hasta el 9
        print("===========")
        print("TABLA DEL "+str(i))
        print("===========")
        # Llamado de la función tablaDeMultiplicar y envío del parámetro x
        tabla = tablaDeMultiplicar(i)
'''
Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

'''
def calculoDePotencia(n:int,x:float) -> float:
    """Función que calcula el valor de un número real x elevado a un número natural n 

    Args:
        n (int): Primer parámetro.
            Número que será la potencia de x
        x (int): Segundo parámetro.
            Número que se elevará a la n 

    Returns:
        int: Retorna potencia. 

    """
    potencia = 1
    for i in range (1, n+1):
        # Bucle for que calcula la potencia de un número real x elevado a un número natural n
        potencia = potencia*x
    return potencia

if __name__ == "__main__":
    n = int(input("Ingrese un número natural: "))
    x = float(input("Ingrese un número real: "))
    # Llamado de la función y envio de los parámetros n y x 
    pot = calculoDePotencia(n,x)
    print(str(x)+"^"+str(n)+" = "+str(pot))
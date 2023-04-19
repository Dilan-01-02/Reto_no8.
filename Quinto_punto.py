'''
Calcular el valor de 2 elevado a la potencia n usando ciclos for.

'''
def calculoDePotencia(n:int) -> int:
    """Función que calcula el valor de 2 elevado a una potencia n s

    Args:
        n (int): Primer parámetro.
            Número el cual será la potencia del número 2

    Returns:
        int: Retorna potencia. 

    """
    potencia : int = 1
    for i in range (1,n+1):
        # Bucle for que calcula el valor de 2 elevado a una potencia dada 
        potencia = potencia*2
    return potencia

if __name__ == "__main__":
    n = int(input("Ingrese un número: "))
    # LLamado de la función y envío del parámetro n 
    pot = calculoDePotencia(n)
    print("2^"+str(n)+" = "+str(pot)) 
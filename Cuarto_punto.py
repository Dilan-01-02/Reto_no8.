'''
Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

'''
def calculoDelFactorial (x:int) -> int:
    """Función que calcula el factorial de los números desde 1 hasta un número n dado recibiendo como parámetros un número entero n 

    Args:
        n(int): Primer parámetro. 
            Último número al cual se le calculará el factorial 

    """
    factorial : int = 1
    for i in range(1, x+1):
        factorial = factorial*i
    return factorial

if __name__ == "__main__":
    bandera : bool = True
    while bandera or n<0:
        # Bucle while que recibe un número natural n y comprueba que el número ingresado es natural 
        bandera = False
        n = int(input("Ingrese un número natural: "))
        if n<0:
            print("El número ingresado no es natural")
    # Llamado de la funcion calculoDelFactorial y envío del parámetro n 
    for i in range (1,n+1):
        fact = calculoDelFactorial(i)
        print(str(i)+"! = "+str(fact))

'''
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

'''

bandera : bool = True
# Bucle while en el que se ingresa un número y comprueba que el número ingresado es mayor o igual a dos
while bandera or n<2:
    bandera = False
    n = int(input("Ingrese un número natural mayor o igual a 2: "))
    
    if n<2:
        print("El número ingresado no es mayor o igual a dos")

# Condicional que convierte un posible número impar ingresado a uno par
if n % 2 != 0:
    n -= 1

print("LOS NÚMEROS PARES ORDENADOS DE FORMA DESCENDENTE DESDE EL NÚMERO " +str(n)+" HASTA 2:")
# Bucle for que muestra los números pares de forma descendente  desde el número ingresado hasta 2
for i in range (n, 1, -2):
    print(i)  
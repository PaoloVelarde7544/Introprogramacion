#Diseñar un programa que almacene en  un vector llamado FACT, el factorial de los primeros 20 números naturales.
#FACT = {1!, 2!, 3!, … 20!} . Debe diseñar una función que calcule el factorial de un número, por lo tanto,
#esta función tiene un parámetro y DEVUELVE (o retorna) un valor.

print("FACT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]")

def factorial (FACT,n):
    if (n>0):
        FACT=factorial(FACT,n-1)
        FACT=FACT*n

    return FACT


try:

    numero = int(input("inserta un numero de la lista: "))


    calculo = factorial(1, numero)

    print(f"El Factorial de {numero} es {calculo}")

except:
    print("Tiene que ser un valor numerico")


#Definir una función inversa() que calcule la inversión de una cadena.
def inversa(cadena):
    cadena_inversa=""
    for caracter in cadena:
        cadena_inversa = caracter + cadena_inversa
    return cadena_inversa

texto = input("Ingrses un texto: ")
inverso = inversa(texto)

print("Cadena origina: " + texto)
print("Cadena invertida: " + inverso)
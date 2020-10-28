#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def esvocal (c):
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
        return True
    elif c=="A" or c=="E" or c=="I" or c=="O" or c=="U":
        return True
    return False
caracter=input("Ingrese una vocal: ")
print(esvocal(caracter))
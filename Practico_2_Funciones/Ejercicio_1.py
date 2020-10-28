#Definir una función que tome como argumento dos números y devuelva el mayor de ellos.
def mayor (x,y):
    if x>y:
        return x
    return y

r=mayor(int(input("Ingrese a: ")),int(input("Ingrese b: ")))
print("El mayor es ",r)








#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos
def mayor (x,y,z):
    if x>y>z:
        return x
    elif y>x>z:
        return y
    return z
r=mayor(int(input("Ingrese x: ")),int(input("Ingrese y: ")),int(input("Ingrese z: ")))
print("El mayor es ",r)
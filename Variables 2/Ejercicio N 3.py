import math

radio = int(input("ingrese el radio del circulo: "))
area = math.pi + radio**2
perimetro = 2 * math.pi * radio
mensaje = f"El area del circulo es igual a: {area} y el perimetro del circulo es: {perimetro}"
print(mensaje)
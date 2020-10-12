num1 = int(input("Ingrese un dividendo: "))
num2 = int(input("Ingrese un divisor: "))
cociente = num1//num2
resto = num1%num2
if resto == 0:
    print(f"La division es exacta")
else:
    print("La division no es exacta")
print(f"cociente: {cociente}")
print(f"resto: {resto}")
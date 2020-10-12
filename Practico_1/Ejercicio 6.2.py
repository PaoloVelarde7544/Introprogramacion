num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))
min = min(num1, num2, num3 )
max = max(num1, num2, num3 )
mid = (num1 + num2 + num3 ) -min -max
print(min, " ", mid, " ", max)
if min == max and max == mid:
    print("Los numeros dadios son iguales")
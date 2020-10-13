num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))
var = 0
for i in range(num1+1, num2):
    var = var + i
print(var)
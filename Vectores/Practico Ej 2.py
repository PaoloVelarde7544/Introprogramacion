#Diseñar un programa que lea como entrada dos vectores de tamaño 5 y devuelva el vector suma.
# Ejemplo: si tenemos los vectores V1 = (a1, a2, …, a5) y V2 = (b1, b2, …, b5) el vector suma se define como el vector obtenido
#de sumar componente a componente: V1 + V2 = (a1+ b1, a2+ b2, …, a5+ b5).

vectorA = []
vectorB = []

for i in range (0,5):
    num = int(input("Ingrese un numero: "))
    vectorA.append(num)


for i in range (0,5):
    num = int(input("Ingrese un numero: "))
    vectorB.append(num)


vectorSuma = []
for i in range (0,5):
    num = vectorA[i]+vectorB[i]
    vectorSuma.append(num)

print(vectorA)
print(vectorB)
print(vectorSuma)
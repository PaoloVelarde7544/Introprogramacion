#Diseñar un programa que lea como entrada dos vectores de tamaño 5 y devuelva el vector suma.
# Ejemplo: si tenemos los vectores V1 = (a1, a2, …, a5) y V2 = (b1, b2, …, b5) el vector suma se define como el vector obtenido
#de sumar componente a componente: V1 + V2 = (a1+ b1, a2+ b2, …, a5+ b5).


vec1=["a1","a2","a3","a4","a5"]
vec2=["+b1","+b2","+b3","+b4","+b5"]

vecR=[]



for i in range (len(vec1)):
    vecR.append(vec1[i])

for i in range (len(vec2)):
    vecR[i]=vecR[i]+vec2[i]

print(vecR)
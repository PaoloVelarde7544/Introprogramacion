peso = int(input("Ingrese su peso: "))
mensaje = f"Su peso es de {peso} kg "
print(mensaje)

estatura = float(input("Ingrese su estatura: "))
mensaje = f"Su estatura es de {estatura} m "
print(mensaje)

indice_masa_corporal = peso / estatura**2
mensaje = f"Tu indice de masa corporal es {indice_masa_corporal}"
print(mensaje)
peso = float(input("Ingrese su peso: "))
mensaje = f"Su peso es de {peso} kg "
print(mensaje)

estatura = float(input("Ingrese su estatura: "))
mensaje = f"Su estatura es de {estatura} m "
print(mensaje)

edad = int(input("Ingrese su edad: "))

indice_masa_corporal = peso/(estatura**2)
mensaje = f"Tu indice de masa corporal es {indice_masa_corporal}"
print(mensaje)
if indice_masa_corporal<22.0 and edad<45:
    print("Condicion de riezgo bajo")
elif indice_masa_corporal<22.0 and edad>=45:
    print("Condicion de riezgo medio")
elif indice_masa_corporal>=22.0 and edad <45:
    print("Cindicion de riezgo medio")
elif indice_masa_corporal>=22.0 and edad>=45:
    print("Condicion de riezgo alto")


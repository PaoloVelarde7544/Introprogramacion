monto_invertir = int(input("Ingrese monto a invertir: "))
interes_anual = int(input("Ingrese interes anual: "))
años_invertidos = int(input("Ingrese el numero de años"))
interes_compuesto = monto_invertir * (1 + interes_anual) ** años_invertidos
mensaje = f"la ganancia neta generada es de {interes_compuesto}: "
print(mensaje)
horas_trabajadas_texto = input("Ingrese cantidad horas trabajadas: ")
paga_por_hora_texto = input("Ingrese paga por hora: ")

horas_trabajadas_num = int(horas_trabajadas_texto)
paga_por_hora_num = float(paga_por_hora_texto)

monto_a_pagar = horas_trabajadas_num + paga_por_hora_num
monto_a_pagar_texto = str(monto_a_pagar)
mensaje = "Monto total a pagar: " + monto_a_pagar_texto
print(mensaje)


#Crea una aplicación que pida un numero por teclado y después comprobaremos si el numero introducido es capicua,
#es decir, que se lee igual sin importar la dirección. Por ejemplo, si introducimos 30303 es capicua,
#si introducimos 30430 no es capicua. Piensa como puedes dar la vuelta al número. Una forma es dividiendolo entre 10 y
#sacando unidad por unidad. Otra es pasarlo a String y revisar posición por posición

numero=int(input("Ingrese un numero capicua: "))

digito1 = numero//10000
digito2 = (numero//1000) % 10
digito3 = (numero//100) % 10
digito4 = (numero//10) % 10
digito5 = numero % 10

if digito1==digito5 and digito2==digito4:
    print("Es capicua")
else:
    print("No es capicua")
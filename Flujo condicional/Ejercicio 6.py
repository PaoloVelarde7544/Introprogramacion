año = int(input("Ingrese el año: "))
if año%4 ==0:
    if año%100 ==0:
        if año%400 ==0:
            print("El año que ingresaste es bisiesto")
        else:
            print("El año que ingresaste no es bisiesto")
    else:
        print("El año que ingresaste es bisiesto")
else:
    print("El año que ingresaste no es bisiesto")


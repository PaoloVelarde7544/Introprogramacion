palabra_1 = input("Palabra 1: ")
palabra_2 = input("Palabra 2: ")
long_1 = len(palabra_1)
long_2 = len(palabra_2)
if long_1 > long_2:
    print(f"La palabra {palabra_1} tiene {long_1 - long_2} letras mas que {palabra_2}")
elif long_1 == long_2:
    print("Las dos palabras tienen el mismo largo")
else:
    print(f"La palabra {palabra_2} tiene {long_2 - long_1} letras mas que {palabra_1}")
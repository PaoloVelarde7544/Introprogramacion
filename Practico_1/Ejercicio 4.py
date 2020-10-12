num = int(input("Ingrese un numero : "))
for i in range (0,abs(num)+1):
   if num<0 :
        print(2**-i)
   else:
        print(2**i)

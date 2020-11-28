def Factorial(numero):
    print("Para:",numero)

    for i in range(1,numero+1):
        factorial = 1
        factorial = (i * factorial)
        print(factorial,end="")
    print("")


for n in range(1,21):
    Factorial(n)
n = int(input("N Numero: "))
j = 1
x=1
while j <= n:
    num = x
    i = 2
    cont = 0
    while i < num:
        if(num % i == 0):
            cont += 1
        i += 1

    if(cont == 0):
        print(num)
        j += 1
    x += 1
n = int(input("Coloque un numero:"))
listaEnteros = []
listaCadenas = []
e = ""
i = 1
while i <= n:
    try:
        e = input("Ingrese elemento: ")
        num = int(e)
        listaEnteros.append(num)
    except:
        listaCadenas.append(e)
    i = i + 1
    
print(listaEnteros)
print(listaCadenas)
lista = []

n = int(input("numero: "))
i = 1
while i <= n:
    num = int(input("numero: "))
    lista.append(num)
    i += 1
print(lista)

numMayor = lista[0]
i = 1
while  i < len(lista):
    if(lista[i] > numMayor):
        numMayor = lista[i]
    i += 1
print("El numero mas alto es: ",numMayor)
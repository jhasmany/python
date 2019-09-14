lista1 = [8,9,4,2]
lista2 = [10,15,20,14]
lista3 = []
contLista1=0
contLista2=len(lista2)-1
i = 1
while i <= 8:
    if(i%2==1):
        lista3.append(lista1[contLista1])
        contLista1 += 1
    else:
        lista3.append(lista2[contLista2])
        contLista2 -= 1
    i += 1
print(lista3)
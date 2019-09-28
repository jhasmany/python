from operacion import *

lista = ["uno","dos","tres","cuatro","cinco","cuatro"]
print(lista)

#Imprime la lista del 0 al 5 con salto de a 2
lista[1] = 1.5
print(lista[0:5:2])

#INSERTA UN NUEVO ELEMENTO
lista.append("new element")
lista.insert(1,"jose")
print(lista)

#ELIMINA ELEMENTO
lista.remove("tres")
print(lista)

#EXTIENE DOS ELEMENTOS AL FINAL DE LA LIST
lista.extend(["siete","ocho"])
print(lista)

#REMPLAZ LOS DOS ELEMENTOS EN LAS POSICIONES
lista[0:2]=(2,"ana")
print(lista)

#Obtinen la posicion del elemento
n = lista.index("cuatro")
print(n)

#lista sin duplicados
listaUnica = list(set(lista))
print(listaUnica)

#El elemento cuatro cuantas veces se repite
n1 = lista.count("cuatro")
print("count:",n1)

#lista duplicado
print(duplicado([1,2,3,4,5,4]))

#revertir lista
print(lista)
lista.reverse()
print(lista)

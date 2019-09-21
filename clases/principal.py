from operacion import *

n1 = 5#int(input("n1:"))
n2 = 4#int(input("n2:"))
suma1(n1,n2)

# listaUno = [2,4,8,10]
# suma2(listaUno)

lis1 = [2,4,6]
suma2(lis1)

lis2 = [1,3,5]
suma2(lis2)

print("Listas Pares e impares")
# n = int(input("N:"))
# i = 1
# l1 = []
# l2 = []
# l3 = []
# while i <= n:
#     num = int(input("Ingrese numero: "))
#     l1.append(num)
#     if(num%2 == 0):
#         l2.append(num)
#     else:
#         l3.append(num)
#     i = i + 1
n = int(input("N:"))
l1 = []
l1 = cargar(n)
l2 = listaPar(l1)
l3 = listaImpar(l1)

print(l1)
print(l2)
print(l3)


from operacion2 import *

# l1 = [2,4,6,8]
# l2 = [1,2,3,4]
# lis = suma(l1,l2)
# print(lis)

operacion = int(input("operacion: "))
if(operacion == 1):
    nombre = input("Coloque nombre: ")
    print(obtenerNumero(nombre))
   
if(operacion == 2):
    lista2 = ['a','jose','ana','Roberto','maria','Gonzalo','Mauricio']
    l1 = clasificaNombresCortos(lista2)
    l2 = clasificaNombresLargos(lista2)
    print(l1)
    print(l2)

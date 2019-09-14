# lista = [1,2,3,10.5,"Jose",False,"Jhire"]
# print(lista[5])

# i=0
# while i<len(lista):
#     print(lista[i])
#     i += 1

nombres = []
i=0
while i < 7:
    name = input("Inserte nombre: ")
    nombres.append(name)
    i+=1
print(nombres)

nombreBuscar = input("Buscar: ")
sw = False
for nom in nombres:
    if(nombreBuscar == nom):
        sw = True

if(sw):
    print(nombreBuscar, " se encuentra en la Lista")
else:
    print(nombreBuscar, " No se encuentra en la Lista")

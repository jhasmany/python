tupla=("jose","ana","diego","jose")
print(tupla)
#Cuenta el elemento jose
print(tupla.count("jose"))
#Devuelve posicion
print(tupla.index("ana"))
#Tamaño de la tupla
print(len(tupla))
#duplica la tupla
print(tupla*3)
#Devuelve si existe el elemento en la tupla
print("diego" in tupla)

for n in tupla:
    print(n)

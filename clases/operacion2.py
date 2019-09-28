def suma(n1,n2):
    lista = []
    i=0
    while i < len(n1):
        lista.append(n1[i]+n2[i])
        i = i+1
    return lista

def obtenerNumero(nombre):
    cadena = "jose 123 ama 222 pedro 333 carlos 567"    
    lista = cadena.upper().split(" ")
    nombre = nombre.upper()
    numero = -1
    i = 0
    while i < len(lista)-1:
        if(nombre == lista[i]):
            numero =  lista[i+1]
        i = i + 2

    if(numero == -1):
        return "No existe nombre en la lista"
    return numero

def clasificaNombresCortos(lista2):
    listaNombresCortos=[]

    for e in lista2:
        if(len(e) <= 5):
            listaNombresCortos.append(e)
    return listaNombresCortos

def clasificaNombresLargos(lista2):
    listaNombresLargos=[]

    for e in lista2:
        if(len(e) > 5):
            listaNombresLargos.append(e)
    return listaNombresLargos









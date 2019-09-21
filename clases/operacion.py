def suma1(n1, n2):
    num1 = n1
    num2 = n2
    res = num1 + num2
    print("resultado de la suma:", res)

def suma2(n):
    a = 0
    for i in n:
        a = a + i
    print("suma",a)
    suma1(4,6)

def cargar(n):
    l1 = []
    i = 1
    while i <= n:
        num = int(input("Ingrese numero: "))
        l1.append(num)
        i = i + 1
    return l1

def listaPar(lista):
    l = []
    for num in lista:
        if(num%2 == 0):
            l.append(num)
    return l

def listaImpar(lista):
    l = []
    for num in lista:
        if(num%2 == 1):
            l.append(num)
    return l

def suma1(n1,n2):
    lis3 = []
    for num in n1:
        lis3.append(num)
    
    for num in n2:
        lis3.append(num)
    
    return lis3

def promedio(n):
    lis3 = []
    sum = 0
    for num in n:
        sum = sum + num
    
    return (sum/len(n))

def cargarCadenas(n):
    l1 = []
    i = 1
    while i <= n:
        nom = input("Ingrese nombre: ")
        l1.append(nom)
        i = i + 1
    return l1

def ordenar(lista):
    ultimoElemento = lista[len(lista)-1]
    j = len(lista)-1
    while j > 0:
        lista[j] = lista[j-1]
        j = j - 1
    lista[0] = ultimoElemento
    return lista

def ordenar3(lis1):
    lis2 = []
    x = lis1[len(lis1)-1]
    lis2.append(x)
    j = 0
    while j < len(lis1)-1:
        lis2.append(lis1[j])
        j = j + 1
    return lis2


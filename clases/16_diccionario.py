dic = {'a1':"Jose",'a2':True,'a3':100, 'a4':[1,2,3,4,[1.5,1.8,1.9],6]}
print(dic['a3'])
print(dic['a4'][4])
print(dic['a4'][4][1])

#Creando diccionario por una lista
lista = [100,200,300,400]
dic2 = dict(zip('abcd',lista))
print(dic2)

#item
#dict_items([('a', 100), ('b', 200), ('c', 300), ('d', 400)])
print(dic2.items())

#Obtiene keys
print(dic2.keys())

#obtiene valores
print(dic2.values())

#Vacia el diccionario
#print(dic2.clear())

#copiar diccionario
dic3 = dic2.copy()
print(dic3)

#Setea el valor 55 en los keys a,b,c
dic4 = dic2.fromkeys(['a','b','c'],55)
print(dic4)

#obtien el elemento 
print(dic2.get('d'))

#elimina el elemento
print(dic2.pop('a'))
print(dic2)


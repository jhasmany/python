i = 1
sumPar = 0
sumImpar = 0
contadorPar = 0
contadorImpar = 0
while i <= 10:
  num = int(input("Numero: "))
  if(num % 2 == 0):
    sumPar = sumPar + num
    contadorPar += 1
  else:
    sumImpar = sumImpar + num
    contadorImpar += 1
  i+=1
if(sumPar > 0):  
    print("Promedio Par:",sumPar/contadorPar)

if(sumImpar > 0):  
    print("Promedio Impar:",sumImpar/contadorImpar)


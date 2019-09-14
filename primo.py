num = int(input("Numero: "))
i=2
cont=0
while i < num:
  if(num % i == 0):
    cont+=1
  i+=1

print(cont)
if(cont == 0):
    print(num, " es primo")
else:
    print(num, " no es primo")

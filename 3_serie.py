
num = int(input("Numero: "))
i = 1
num1 = 2
num2 = 555555
sumNum1 = 0
sumNum2 = 0

while i <= num:
  if(i % 2 == 1):
    sumNum1 = sumNum1*10 + num1
    print(sumNum1)
  else:
    sumNum2 = int(num2/10)
    print(sumNum2)
    num2=sumNum2    
  i+=1

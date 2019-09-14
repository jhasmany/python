L1 = []
L2 = []
L3 = []
n = int(input("numero: "))
i = 1
while i <= n:
    num = int(input("numero: "))
    L1.append(num)
    if(num >= 10):
        L2.append(num)
    else:
        L3.append(num)
    i += 1

print(L1)
print(L2)
print(L3)

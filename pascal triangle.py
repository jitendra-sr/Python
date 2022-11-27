a=int(input('enter the number: '))
import math as m
for i in range(0,a):
    for j in range(0,i+1):
        print(m.comb(i,j),end=' ')
    print()

a=int(input('Enter Number: '))
i=0
j=1
k=0
print(i,end=',')
print(j,end=',')
while (i+j)<a:
    k=i+j
    i,j=j,k
    print(k,end=',')
    

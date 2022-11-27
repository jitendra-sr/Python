a=input('Enter Number: ')
p=len(a)
n=int(a)
m=n
k=0
while n:
    i=n%10
    n//=10
    j=i**p
    k=k+j
    print(i,'**',p,'=',j,', Sum is:',k)
if m==k:
    print('Armstrong Strong')
else:
    print(m,'is not eqal',k)
    print(m,'is Not an Armstrong Number')

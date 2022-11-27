n=int(input('Enter Number: '))
temp=n
rev=0
while(n):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print('Palindrome')
else:
    print('NOT')


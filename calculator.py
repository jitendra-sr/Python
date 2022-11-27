import math
from string import *
print('\t Scientific Calculator')
entry=input('Enter Number: ')
if (entry.islower() or entry.isupper() or entry.isspace() or entry.istitle()):
    print('It is a String')
elif (not entry.islower() and not entry.isupper() and not entry.isspace() and not entry.istitle()):
    num=float(entry)
    op='Select Your Operation'
    a,b,c,d,e,f,g,h,i,r='ceil','floor','abs','round','sqrt','log','exp','sin','tan','factorial'
    j,k,l,m,n,o,p,q='min','max','pow','add','sub','multiply','divide','percent'
    print(op)
    print(a,b,c,d,e,f,g,h,i,r,j,k,l,m,n,o,p,q)
    sel=input('Enter Your Operation: ')
    if sel==a or sel==b or sel==c or sel==d or sel==e or sel==f or sel==g or sel==h or sel==i or sel==r:
        if sel==a:
            print(math.ceil(num))
        elif sel==b:
            print(math.floor(num))
        elif sel==c:
            print(abs(num))
        elif sel==d:
            print(round(num))
        elif sel==e:
            if num>=0:
                print(math.sqrt(num))
            elif num<0:
                num=num*(-1)
                print(complex(0,math.sqrt(num)))
            else:
                print('PROGRAMMING MISTAKE 1')
        elif sel==f:
            if num>0:
                print(math.log(num))
            elif num<=0:
                print('Logarithm of Zero and Negative Number is not Defined')
            else:
                print('PROGRAMMING MISTAKE 2')
        elif sel==g:
            print(math.exp(num))
        elif sel==h:
            print(math.sin(num))
        elif sel==i:
            print(math.tan(num))
        elif sel==r:
            if type(num)==float or num<0:
                print('Factorial of Decimal and Negative Number is NOT Defined')
            elif num>=0:
                num=int(num)
                print(math.factorial(num))
            else:
                print('PROGRAMMING MISTAKE 3')
        else:
            print('PROGRAMMING MISTAKE 4')
    elif sel==j or sel==k or sel==l or sel==m or sel==n or sel==o or sel==p or sel==q:
        entry2=input('Enter Second Number: ')
        if (entry2.islower() or entry2.isupper() or entry2.isspace() or entry2.istitle()):
            print('It is a String')
        elif (not entry2.islower() and not entry2.isupper() and not entry2.isspace() and not entry2.istitle()):
            num2=float(entry2)
            if sel==j:
                print(min(num,num2))
            elif sel==k:
                print(max(num,num2))
            elif sel==l:
                print(pow(num,num2))
            elif sel==m:
                print(num+num2)
            elif sel==n:
                print(num-num2)
            elif sel==o:
                print(num*num2)
            elif sel==p:
                if num2==0:
                    print('Division by Zero is Not Defined')
                elif num2!=0:
                    print(num/num2)
                else:
                    print('PROGRAMMING MISTAKE 5')
            elif sel==q:
                print((num*num2)/100)
            else:
                print('PROGRAMMING MISTAKE 4')
        else:
            print('Enter Digits Only')
    else:
        print('Select Correct Operation')
else:
    print('Enter Digits Only')

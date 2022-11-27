'''
#printing number from backward
def num(s):
    if s==0:
        print('end')
    else:
        print(s)
        num(s-1)
num=int(input('enter th number: '))
fac(num)
'''
def fac(s):
    if s==0:
        return 1
    elif (s==1):
        return 1
    else:
        return s*fac(s-1)
num=int(input('enter the number: '))
print(fac(num))


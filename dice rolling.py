print('Enter Number Greater than 6 to Exit')
score=0
while True:
    dice=int(input('Enter Your Number: '))
    import random as rn
    num=rn.randint(1,6)
    print('Dice Number is: {}'.format(num))
    if dice==num:
        score+=1
        print('You Win {} times'.format(score))
    elif dice>6:
        break
    else:
        print('Better Luck Next Time')

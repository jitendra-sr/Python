print('Use Convention --> Rock as "R", Paper as "P", Scissor as "S"')
print('Enter "E" for EXIT')
uScore=0
cScore=0
while True:
    user=input('Rock, Paper or Scissor? ')
    if user in 'RPS':
        import random as rn
        cpu=rn.choice('RPS')
        if cpu=='R':
            print("Computer's Choice is: Rock")
        elif cpu=='P':
            print("Computer's Choice is: Paper")
        elif cpu=='S':
            print("Computer's Choice is: Scissor")

        if user!=cpu:
            if cpu=='R' and user=='S':
                cScore+=1
                print('You Lose... Rock smashes Scissor')
            elif cpu=='R' and user=='P':
                uScore+=1
                print('You Win! Paper covers Rock')
            elif cpu=='P' and user=='R':
                cScore+=1
                print('You Lose... Paper covers Rock')
            elif cpu=='P' and user=='S':
                uScore+=1
                print('You Win! Scissor cuts Paper')
            elif cpu=='S' and user=='R':
                uScore+=1
                print('You Win! Rock smashes Scissor')
            elif cpu=='S' and user=='P':
                cScore+=1
                print('You Lose... Scissor cuts Paper')
        else:
            print('Tie')
    elif user=='E':
        break
    else:
        print('Give correct input according to defined convention')
print('Final Scores:\nUser: {}\nComputer: {}'.format(uScore,cScore))
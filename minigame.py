#mini_game
import random
a=random.randrange(0,10)
b=int(input('Enter your number:'))

l=[a,b]
max_l=max(l)
min_l=min(l)
subtr=max_l-min_l

if subtr==0:
    print('Congratulations!!!You have won The game. It was '+str(a)+'.')
elif subtr==1:
    print('You are wrong with 1 number.You have one more opportunity')
    another_chance=int(input('Enter your number:'))
    if another_chance==a:
        print('Congratulations!!!You have won The game. It was '+str(a)+'.')
    else:
        print('You could not find the number. It was '+str(a)+'.')
else:
    print('You could not find the number. It was ' + str(a) + '.')

import random

answer = random.randint(1,100)
chance = 7

while(chance != 0):
    print(f'Chance : {chance}')
    guess = int(input("1~100 중 하나입니다 : "))
    chance -= 1
    if guess == answer:
        print(f'You win! Answer is {answer}')
        print(f'spend {chance} time!')
        break
    elif guess > answer:
        print(f'{guess} number is bigger')
    else :
        print(f'{guess} number is lower')

print(f'You lost. Answer is {answer}!')

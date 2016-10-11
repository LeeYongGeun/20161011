number = 23
running = True

while running:
    guess =int(input('Enter an integer : '))
    if guess == number:
        print('Congratylations, You guessed it. ')
        # running = False       ctrl+/
        break
    elif guess < number :
        print('No, It is a little higher than that. ')
    else:
        print('No, It is a little lower than that')
else:
    print('The while loop is over') # break구문 사용시 else는 작동안됨
print('Done')
print('t')

import random
import sys

n = int(sys.argv[1])
# print(n)
m = int(sys.argv[2])

secret = random.randint(1, n)
# print(secret)

while True:
    guess = int(input('your guess: '))

    if guess != secret:
        m -= 1

        if m != 1:
            print("\nYou have " + str(m) + ' moves left.' + '\n')
        else:
            print("\nYou have " + str(m) + ' move left.' + '\n')

        if guess < secret:
            print('secret is more than ' + str(guess) + '\n')
        if guess > secret:
            print('secret is less than ' + str(guess)+ '\n')
    
    if m == 0:
        print('\nYou lost.')
        print("Secret was " + str(secret))
        exit()
    
    if guess == secret:
        print("\nWOW WOW you won!!!")
        exit()


import random
import sys

n = int(sys.argv[1])
print(n)
m = int(sys.argv[2])

secret = random.randint(1, n)
# print(secret)

while True:
    guess = int(input('your guess: '))

    if guess != secret:
        m -= 1

        if guess < secret:
            print('secret is more than ' + str(guess))
        if guess > secret:
            print('secret is less than ' + str(guess))

        continue
    
    if m == 0:
        print('You lost.')
        exit()
    
    if guess == secret:
        print("WOW WOW you won!!!")
        exit()


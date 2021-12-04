import random
RandomNumber = random.randint(0,100)

while True:
    Number = int(input('Enter your number: '))
    if Number == RandomNumber:
        print ('Correct')
        break
    if Number >= RandomNumber:
        print ('Guess lower')
    if Number <= RandomNumber:
        print ('Guess higher')
    
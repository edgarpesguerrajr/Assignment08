import random
Number1 = random.randint(0,9)
Number2 = random.randint(0,9)
Number3 = random.randint(0,9)

while True:
    FirstNumber = int(input ('Enter your first number :'))
    SecondNumber = int(input ('Enter your second number :'))
    ThirdNumber = int(input ('Enter your number number :'))
  
    if FirstNumber == Number1:
        if SecondNumber == Number2:
            if ThirdNumber == Number3:
                print ('Winner')
                print (f'The random numbers are {Number1}, {Number2}, {Number3}.')
                break
            else:
                print ('You loss')
                print ('Try again')
                Choose = input('Yes or No:')
                if Choose == "No":
                    print (f'The random numbers are {Number1}, {Number2}, {Number3}.')
                    break
        else:
            print ('You loss')
            print ('Try again')
            Choose = input('Yes or No:')
            if Choose == "No":
                print (f'The random numbers are {Number1}, {Number2}, {Number3}.')
                break
    else:
        print ('You loss')
        print ('Try again')
        Choose = input('Yes or No:')
        if Choose == "No":
            print (f'The random numbers are {Number1}, {Number2}, {Number3}.')
            break
            
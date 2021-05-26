import random

def guess(x):
    ran_number = random.randint(1, x)
    guess = 0
    chances = 3

    while guess != ran_number and chances >= 0 :
        print(f'Chances : {chances}')
        guess = int(input("Enter a Guess Number : "))
        
        if guess < ran_number:
            print("Try again. It's too low")
            chances -= 1
        elif guess > ran_number:
            print("Try again. It's too high")
            chances -= 1
        
    if chances == 0:
        print('Oops, Game Over!')
    else:
        print(f"Yeay, you are right! The number is {ran_number}")
    

# guess(10)
    


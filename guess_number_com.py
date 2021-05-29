import random

def guess(x):
    ran_number = random.randint(1, x)
    guess = 0
    chances = 3

    while guess != ran_number and chances >= 0 :
        print(f'Chances : {chances}')
        print('=' * 20)
        guess = int(input(f"Enter a Guess Number (1 - {x}): "))
        
        print('=' * 20)
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
    print('=' * 20)
    

# guess(10)

while True:
    range = 0;
    print('Guess a Number Game')
    print("""
    Menu (max range number) :
    1. (5)
    2. (10)
    3. (50)
    4. (100)
    0. Exit
""")
    menu = int(input('Choose Menu : '))

    if menu == 0:
        print('=' * 20)
        print('Quit Game!')
        break
    elif menu == 1:
        range = 5
    elif menu == 2:
        range = 10
    elif menu == 3:
        range = 50
    elif menu == 4:
        range = 100
    else:
        print('=' * 20)
        print('Menu Not Found. Please Choose an Available Menu!')
        print('=' * 20)
        continue
    
    print('=' * 20)
    print('Game Start!')
    print('=' * 20)
    guess(range)


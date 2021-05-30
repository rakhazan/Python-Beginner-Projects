import random as r

def guess(x) :
    low = 1
    high = x

    feedback = ''

    while feedback != 'c':
        print('=' * 20)
        if high != low:
            g = r.randint(low, high);
        else:
            g = low     # Could also be high because high =  low
        
        feedback = input(f"Is your number = {g} | too high(H), too low(L), correct (C) | : ").lower()
        if feedback == 'h':
            high = g - 1
        elif feedback == 'l':
            low = g + 1
    
    print('Yay! The COM guessed number ({g}) correctly')

# guess(10)
print('=' * 20)
print('Guess Number Game')
while True:
    print('=' * 20)
    print("""
    Menu (your max number):
    1. (5)
    2. (10)
    3. (50)
    4. (100)
    0. Exit
    """)
    menu = int(input('Choose Menu : '))
    max = 0
    print('=' * 20)
    if menu == 0:
        print('Quit Game')
        break
    elif menu == 1:
        max = 5
    elif menu == 2:
        max = 10
    elif menu == 3:
        max = 50
    elif menu == 4:
        max = 100
    else:
        print("Menu Not Found! Please Choose an Available Menu!")
        continue
    
    print('Game Start !')
    guess(max)

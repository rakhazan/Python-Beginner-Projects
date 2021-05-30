import random as r

def guess(x) :
    low = 1
    high = x

    feedback = ''

    while feedback != 'c':
        if high != low:
            g = r.randint(low, high);
        else:
            g = low     # Could also be high because high =  low
        
        feedback = input(f"Is number = {g} | too high(H), too low(L), correct (C) | : ").lower()
        if feedback == 'h':
            high = g - 1
        elif feedback == 'l':
            low = g + 1
    
    print('Yay! The COM guessed number ({g}) correctly')

guess(10)

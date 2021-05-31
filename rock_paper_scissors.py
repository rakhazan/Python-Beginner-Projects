import random

def play(user):
    print('=' * 20)
    # com choice
    com = random.choice(['r', 'p', 's'])

    print(f'You: {get_choice(user)} VS COM: {get_choice(com)}')
    print('=' * 20)
    if user == com:
        return ('t', 'It\'s a tie') 
    if is_win(user, com):
        return ('w', 'You Win!')
    return ('l' ,'You Lost!')
    
def is_win(p1, p2):
    if (p1 == 'r' and p2 == 's') or (p1 == 's' and p2 == 'p') or (p1 == 'p' and p2 == 'r'):
        return True
    return False

def get_choice(choice):
    if choice == 'r':
        return 'Rock'
    if choice == 'p':
        return 'Paper'
    if choice == 's':
        return 'Scissors'

print('=' * 20)
print('Rock Paper Scissors Game')

win = 0
lost = 0
tie = 0

ulang = 'y'
while ulang == 'y':
    print('=' * 20)
    user = input('What\'s your choice ? | rock(r), paper(p), scissors(s) : ').lower()
    if user != 'r' and user != 'p' and user != 's':
        print('Choice Not Found! Please select the right choice!')
        continue

    status, msg = play(user)

    if status == 'w':
        win += 1
    elif status == 'l':
        lost += 1
    elif status == 't':
        tie += 1
    
    print(msg)
    print('=' * 20)
    print(f'Score (win : lost : tie) | {win} : {lost} : {tie}')
    print('=' * 20)
    ulang = input('Try Again ? | yes(y), no(n) : ').lower()
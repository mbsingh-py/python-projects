import random

print(f"{'*'*10} SNAKE WATER GUN {'*'*10}")
print(f'\nS for Snake \nW for Water \nG for Gun\n')
dict1 = {'s': -1, 'w': 0, 'g':1}
dict2 = {'s': 'Snake', 'w': 'Water', 'g':'Gun'}
choose = ['s', 'w', 'g']
user_win_count = 0
user_lose_count = 0
match_draw_count = 0
game_played = 0
    
while True:
    game_played += 1
    computer_str = random.choice(choose)
    computer = dict1[computer_str]
    
    while True:
        you = input(f'Enter \'S, W, G\': ')
        you = you.lower()
        if you in choose and len(you) == 1:
            user = dict1[you]
            break
        else:
            print('Enter only (S/W/G)')
            continue

    if computer == user:
        result = 'Match Draw'
    elif user == -1:
        if computer == 0:
            result = 'Win'
        else:
            result = 'Lose'
    elif user == 0:
        if computer == 1:
            result = 'Win'
        else:
            result = 'Lose'
    elif user == 1:
        if computer == -1:
            result = 'Win'
        else:
            result = 'Lose'
    
    if result == 'Win':
        user_win_count += 1
    if result == 'Lose':
        user_lose_count += 1
    if result == 'Match Draw':
        match_draw_count += 1

    print(f'\nComputer: {dict2[computer_str]} \nYou: {dict2[you]} \nResult: {result}')
    while True:
        again = input(f'\nDo you want to play again(y/n): ')
        if again.lower() in ['y', 'n']:
            break
        else:
            print('Enter only (y/n)')
    if again.lower() == 'n':
        print('Game End...')
        break

print(f'\nGame Played: {game_played} \nWin:{user_win_count} \nLose: {user_lose_count} \nMatch Draw = {match_draw_count}')

from random import randint
low = 1   
high = 100
max_attempts = 20  # Attempts


# Name validation
def name_validation():
    while True:
        name = input("Enter your name: ").strip()
        clean_name = name.replace(" ", "")
        if clean_name == "":
            print("Empty name is not allowed!")
        elif clean_name.isalpha():
            name = " ".join(name.split()).title()
            break
        else:
            print("Only alphabets and spaces are allowed!")

    return name


users = {}
n = randint(1000, 10000)*1000
while True:
    x = randint(low, high)
    n += 1   # To create user_id
    attempts = max_attempts

    print(f"\n{'*'*15} NUMBER GUESSING GAME {'*'*15} \n\nRules: \n• You have to guess a number between {low} and {high}. \n• You have {max_attempts} attempts to guess it. \n• Your score will be 5 times the remaining attempts. \n{'*'*8} All the best {'*'*8} \n")
    name = name_validation()

    clean = name.lower().replace(" ", "")
    prefix = clean[:3] if len(clean) >= 3 else clean.ljust(3, "x")
    user_id = f"{prefix}{n}"        # Used to avoid same name issue
    
    print(f"\nName: {name} \nuser_id: {user_id} \nattempts: {attempts}\n")

    while True:
        try:
            num = int(input("Enter your guess: "))
        except ValueError:
            print(f"Only integers allowed!")
            continue
        if num != x:
            attempts -= 1
            print(f"Remaining attempts: {attempts}")
            if attempts == 0:
                print(f"\nYour chance is over \nBetter luck next time! The number was {x}")
                break
            else:
                if num < x:
                    print(f"Hint: Higher the number")
                else:
                    print(f"Hint: Lower the number")
        else:
            print(f"\nCongrats! You guessed it right")
            break
    
    score = attempts * 5
    users[user_id] = {"name": name, "score": score}
    print(f"Player: {name} \nuser_id: {user_id} \nscore: {score}")

    print(f"\nIs there any player remaining or End game and calculate result? \nType: \n'y' for next player \n'n' to calculate result")
    while True:
        nxt_round = input("(y/n): ").strip()
        if nxt_round.lower() == "y":
            run_again = True
            break
        elif nxt_round.lower() == "n":
            run_again = False
            break
        else:
            print("Only 'y' or 'n' are allowed!")
            continue

    if run_again:
        continue
    else:
        break


if not users:
    print("No players played the game.")
else:
    # Finding max_score
    max_score = 0
    for data in users.values():
        if data['score'] > max_score:
            max_score = data['score']


    print(f"\nPlayers with highest score ({max_score}):")
    for userId, data in users.items():
        if data['score'] == max_score:
            print(f"• Name: {data['name']:<15} user_id: {userId:<12}")

    print(f"\nAll players (playing order): ")
    s_no = 0
    for userId, data in users.items():
        s_no += 1
        print(f"{s_no:>3}  Name: {data['name']:<15} user_id: {userId:<15} Score: {data['score']}")

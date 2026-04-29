import random as rand

def retry():
    while True:
        print("Want to play again ?")
        rtry = input("-->").lower()
        if rtry == "yes":
            game()
        elif rtry == "no":
            print("Thanks for playing!")
            break
            break
        else:
            print("please enter (yes/no)")

def game():
    print("Rock! Paper! Sccicor!")
    running = True
    my_score = 0
    bot_score = 0
    while running:
        

        rps = ["Rock", "Paper", "Sccicor"]
        r = rand.randint(0, 3 - 1)
        bot = rps[r]
        user = input("Your turn: ").title()
        #wins
        print(f"Bot: {bot}")
        if user == "Rock" and bot == "Sccicor":
            print("  You Win!")
            my_score += 1
            print(f"You: {my_score} Bot: {bot_score}")
        elif user == "Paper" and bot == "Rock":
            print("  You Win!")
            my_score += 1
            print(f"You: {my_score} Bot: {bot_score}")
        elif user == "Sccicor" and bot == "Paper":
            print("  You Win!")
            my_score += 1
            print(f"You: {my_score} Bot: {bot_score}")
        #loses
        elif user == "Rock" and bot == "Paper":
            print("Bot win!")
            bot_score += 1
            print(f"You: {my_score} Bot: {bot_score}")
        elif user == "Paper" and bot == "Sccicor":
            print("Bot win!")
            bot_score += 1
            print(f"You: {my_score} Bot: {bot_score}")
        elif user == "Sccicor" and bot == "Rock":
            print("Bot win!")
            bot_score += 1
            print(f"You: {my_score} Bot: {bot_score}")
        elif user == bot:
            print("Draw!")
            print(f"You: {my_score} Bot: {bot_score}")
        elif not user in rps:
            print("incorrect spell")
        if my_score == 3:
            print("YOU VICTORY!")
            retry()
            break
            
        elif bot_score == 3:
            print("YOU LOSE!")
            retry()
            break
            
#The start here----
print("This is Rock Paper sccicor game")
print("Enter [S] to start")
start = input("-->").lower()
if start == "s" or start == "start":
    game()
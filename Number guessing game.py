import random
def endless():
    atemptt = 0
    random_num = random.randint(1,100)
    print('Try to geuss number between 1-100')
    print('You Have endless atempt to guess')
    while True:
        try:
            player_guess = int(input('-->'))
            if player_guess == random_num:
                if atemptt == 0:
                    print('Excellent, in first try!')
                if atemptt == 1:
                    print('Rare moment, 2nd try')
                else:
                    print('You did it!')
                print('You take',atemptt,'atemptt to guess')
                
                endless_retry()
            elif player_guess <= random_num:
                print('Try High!')
                atemptt += 1
            elif player_guess >= random_num:
                print('Try Low!')
                atemptt += 1
        except ValueError:
            print('please Enter number Only!')
def strt():
    print('Write [S]to Start')
    start = input('-->').lower()
    if start == 's':
        game()
    else:
        print('please enter valid option!')
        strt()
def endless_retry():
    print()
    print('[P]to Play again')
    print('[A]to limited atempt')
    print('[Q]to quit')
    player = input('-->').lower()
    if player == 'p':
        endless()
    if player == 'q':
        print('Thanks for playing!')
        quit()
    elif player == 'a':
        game()
    else:
        print('please choice')
        endless_retry()
def retry():
    print()
    print('[P]to Play again')
    print('[E]to endless atempt')
    print('[Q]to quit')
    player = input('-->').lower()
    if player == 'p':
        game()
    if player == 'q':
        print('Thanks for playing!')
        quit()
    elif player == 'e':
        endless()
    else:
        print('please choice')
        retry()
def game():
    atemptt = 5
    random_num = random.randint(1,100)
    print('Try to geuss number between 1-100')
    print('You Have 5 atempt to guess')
    while True:
        try:
            player_guess = int(input('-->'))
            if player_guess == random_num:
                print()
                if atemptt == 5:
                    print('Excellent, in first try!')
                if atemptt == 4:
                    print('Rare moment, 2nd try')
                else:
                    print('You did it!')
                print('atemptt left',atemptt)
                retry()
            elif player_guess > 100 or player_guess < 1:
                print("You can olny guess between 1-100")
            elif atemptt <= 0:
                print()
                print('You lose')
                print('The number is',random_num)
                print('Atemptt left',atemptt)
                retry()
            elif player_guess <= random_num:
                print('Try High!')
                atemptt -= 1
                if atemptt == 0:
                    print('Your last atempt')
            elif player_guess >= random_num:
                print('Try Low!')
                atemptt -= 1
                if atemptt == 0:
                    print('Your last atempt')
        except ValueError:
            print('please Enter number Only!')
#--------------------------------
print('Enter Your Name')
name = input('-->').upper()
print('Hello',name +', This is Number guessing Game')
strt()
    
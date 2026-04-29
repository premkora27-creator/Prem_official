#Clarie 3.0
import random

def calculator():
    bot_greet = [
        "How Can i Help You","How Can i assist you?"
    ]
    while True:
        try:
            try:
                calcu = [input("-->  ").split()]
            except:
                print("error")
            if calcu[0] == None:
                print("You didn't add any number!")
            elif calcu[2] == None:
                try:
                    print("You Didn't add 2nd number!")
                    num2 = int(input("2nd number: "))
                except ValueError:
                    print("please Enter Number Only!")
            num1 = int(calcu[0])
            num2 = int(calcu[2])
        except ValueError:
            if "info" in calcu:
                print("")
                print("Here Infromation about this calculator")
                print("+ = adition. - = subtraction.")
                print("* = multiplication / = division.")
                print("You can't calculate more that two numbers")
                print("Example: 10 + 20 right: 10 + 20 + 30 wrong:")
                print("type [back] or [quit] go back")
                print("")
                calculator();break
            elif "back" or "quit" or 'q' in calcu:
                print("")
                print(random.choice(bot_greet))
                main();break
        
        if num2 == 0 and calcu[1] == '/':
            print(f"You can't divide {num1} by 0")
        elif '+' in calcu:
            print(f"Answer: {num1 + num2}")
        elif '*' in calcu:
            print(f"Answer: {num1 * num2}")
        elif '-' in calcu:
            print(f"Answer: {num1 - num2}")
        elif '/' in calcu:
            print(f"Answer: {num1 / num2}")
        else:
            print("else running")

# main loop
def main():
    bot = "Clarie"
    greet = [
        "hi","hii","hello","helo",
        "*whatshup","namaste","greet"
        ]
    bot_greet = [
        "How Can i Help You","How Can i assist you","need any help?"
    ]
    running = True
    while running:
        user = input("You: ").lower()
        if user in greet:
            print(f"{bot}: {user.title()} {random.choice(bot_greet)}")
        elif user == "+" or user ==  '*' or user == '/' or user == '-':
            print("Its look you want to calculation ?")
            verify = input("(y/n)? ").lower()
            if verify == 'y' or verify == "yes":
                    print("")
                    print("OK, Here your calculator!")
                    print("Example: 1 + 2 [Enter]")
                    print("for more infromation type [info]")
                    calculator();break
            elif verify == 'n' or verify == "no":
                print("Ok, how can i help you then?")
                main();break
        elif user == "calculator" or user == "calculation":
                print("")
                print("OK, Here your calculator!")
                print("Example: 1 + 2 [Enter]")
                print("for more infromation type [info]")
                calculator();break
        else:
            print("Sorry, i can't do it")
print("Hi i am Clarie, how i can assist you ?")
print()
main()
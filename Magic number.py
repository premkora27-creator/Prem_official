def game():
    print("Enter Any Number")
    try:
        user = int(input("-->"))
        input("now double your number: ")
        input("add 9 to the result: ")
        input("subtract 3 from result: ")
        input("now half your number: ")
        input("finaly subtract the number you enterd at first: ")
        print("Your result is: 3")
        print("Right!")
    except ValueError:
        print("please enter number only")
        game()
game()
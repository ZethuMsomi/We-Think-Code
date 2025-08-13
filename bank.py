def talk():
    say_hello = input("Hi there: ")
    greeting = say_hello.strip().upper()
    if greeting == "HELLO" or greeting.startswith("HELLO"):
        print("You get $0")
    elif greeting.startswith("H"):
        print("You get $20")
    else:
        print("You get $100")
talk()



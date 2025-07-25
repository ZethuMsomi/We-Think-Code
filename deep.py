def deep():
    question = input("What is the answer to the question of Life, the Universe and Everything? ");
    answer = question.lower().strip()
    if answer == "42":
        print("Yes")
    elif answer == "forty-two":
        print("Yes")
    elif answer == "forty two":
        print("Yes")
    else:
        print("No")
deep()




easy_questions = """\nClasses and objects are the two main aspects of object oriented programming.
A __1__ creates a new type where objects are instances of the class.
 Variables that belong to an object or class are referred to as __2__.
 Objects can also have functionality by using functions that belong to a class.
 Such functions are called __3__ of the class.
"""
easy_answers = ["class", "fields", "methods"]

medium_questions = """\nCollectively, the fields and methods can be referred to as
the __1__ of that class. Fields are of two types - they can belong to each
instance/object of the class or they can belong to the class itself.
They are called __2__ and __3__ respectively.
"""
medium_answers = ["attributes", "instance variables", "class variables"]

hard_questions = """\nThe __init__ method is run as soon as an object of a class is
instantiated (i.e. created). The method is useful to do any __1__. One of the
major benefits of object oriented programming is reuse of code and one of the
ways this is achieved is through the __2__ mechanism. It’s important to note
that child classes override or extend the functionality (e.g., attributes and
behaviors) of __3__ classes.
"""

hard_answers = ["initialization", "inheritance", "parent"]

blank_spaces = ["___1___", "___2___", "___3___"]

# promts the user to enter the answer and once its entered it remains


def guess_check(index):
    guess = input("\nWhat is the value of {} : ".format(index)).lower()
    return guess


def quiz_level():
    level = ""
    levels = ["easy", "medium", "hard"]
    while level not in levels:
        level = input("Please choose a level (easy, medium, hard): ").lower()
        if level == "easy":
            return easy_questions, easy_answers  # if the level is easy, it returns easy_questions and easy_answers
        elif level == "medium":
            return medium_questions, medium_answers
        elif level == "hard":
            return hard_questions, hard_answers
        else:
            print("The entered value is not valid. Please choose your level")


def play_game():
    index = 0
    user_level, answer = quiz_level()
    while index < len(blank_spaces):
        print(user_level)
        user_guess = guess_check(blank_spaces[index])
        if user_guess == answer[index]:
            print("\nIt is correct answer!.\n")
            user_level = user_level.replace(blank_spaces[index], user_guess)
            index += 1
        else:
            print("\nNot correct.\n")
    input("To end the game, press enter")


play_game()

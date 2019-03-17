

easy_questions = """Classes and objects are the two main aspects of object oriented programming.
A __1__ creates a new type where objects are instances of the class.
 Variables that belong to an object or class are referred to as __2__.
 Objects can also have functionality by using functions that belong to a class.
 Such functions are called __3__ of the class. __4__ is a class variable or
 instance variable that holds data associated with a class and its objects.
"""

medium_questions = """Collectively, the fields and methods can be referred to as
the __1__ of that class. Fields are of two types - they can belong to each
instance/object of the class or they can belong to the class itself.
They are called __2__ and __3__ respectively. __4__ is an individual object
of a certain class.
"""

hard_questions = """The __init__ method is run as soon as an object of a class is
instantiated (i.e. created). The method is useful to do any __1__. One of the
major benefits of object oriented programming is reuse of code and one of the
ways this is achieved is through the __2__ mechanism. It’s important to note
that child classes override or extend the functionality (e.g., attributes and
behaviors) of __3__ classes. __4__ is the assignment of more than one function
to a particular operator.
"""
easy_answers = ["class", "fields", "methods", "class member"]
medium_answers = ["attributes", "instance variables", "class variables", "instance"]
hard_answers = ["initialization", "inheritance", "parent", "operator overloading"]

blank_spaces = ["__1__", "__2__", "__3__", "__4__"]

# promts user to enter level
your_level = input('Choose your game difficulty (easy, medium, hard): ')
levels = ['easy', 'medium', 'hard']
level = ""

#


def guess(questions, answers):
    # Prompts user to answer the question until it reaches 4
    question = 0
    while question < len(blank_spaces):
        print(questions)
        guess = input('What is the answer for the' + blank_spaces[question])
        if guess == answers[question]:
            print('Right')
            questions = questions.replace(blank_spaces[question], guess)
            question += 1
        else:
            print('Try again')
    input("To end the game, press enter")


while level not in levels:
    if your_level == 'easy':
        # we assign variables questions and answers to different data based on leve;
        questions = easy_questions
        answers = easy_answers
        guess(questions, answers)
        break
    elif your_level == 'medium':
        questions = medium_questions
        answers = medium_answers
        guess(questions, answers)
        break
    elif your_level == 'hard':
        questions = hard_questions
        answers = hard_answers
        guess(questions, answers)
        break

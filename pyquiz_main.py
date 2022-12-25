"""
PyQuiz Main File

PyQuiz is a study tool to help students prepare for a quiz, text, exam,
or anything else of the sort. The tool allows users to enter terms to study along with their
definitions and gives different options of modes to play to practice learning and mastering the terms.

Final Project
by Ian Cox
CS021, Cafiero
"""

import random


def playflip(t, d):
    # flashcards game mode
    starred = [] # list for the starred terms
    starred_defs = [] # list for the definitions of the starred terms
    counter = 0 # will later cycle through the definitions for each term
    for term in t:
        print(term)
        ent = input('Click enter to flip card')
        if ent == "":
           y = 0
           while y < 100:
               print("\n")
               y += 1
           print(d[counter])
           star = input("Do you want to star this term or move on? [type 'star' to star or click enter to "
                                "advance]")
           if star == 'star':
               starred.append(term)
               starred_defs.append(d[counter])
           counter += 1
    counter = 0 # reset this to zero to cycle through the starred terms
    study_more = True
    while study_more:
        study = input("Would you now like to study your starred terms? ['y' for yes, 'n' for no]: ")
        if study == 'y':
            for s in starred:
                print(s)
                ent = input('Click enter to flip card')
                if ent == "":
                    y = 0
                    while y < 100:
                        print("\n")
                        y += 1
                    print(starred_defs[counter])
                counter += 1
            study_more = False
        elif study == 'n':
            study_more = False
        else:
            print("That was an invalid response, try again.")


def mult(t, d):
    # multiple choice game mode
    score = 0
    for term in t:
        print(term)
        ind = t.index(term)
        x = 1 # variable to cycle through the mode, increments by 1 each play through
        # correct answer
        correct = 0
        used = []  # terms that have already been used so they can't get used again
        range_x = 0
        if len(t) >= 4:
            range_x = 5
            rand = random.randint(1, 4)  # picks random num from 1 to 4 to decide what number will be assigned
        else:
            range_x = len(t) + 1
            rand = random.randint(1, len(t))  # picks random num from 1 to whatever the length of the list is
        while x < range_x:
            if x == rand:
                randdef = d[ind]
                print(f'{x}: {randdef}')
                correct = rand
                used.append(randdef)
            else:
                randdef = random.choice(d)
                while x != rand and randdef == d[ind]:
                    randdef = random.choice(d)
                through_used = True
                while through_used:
                    if randdef in used:
                        randdef = random.choice(d)
                    else:
                        through_used = False
                print(f'{x}: {randdef}')
                used.append(randdef)
            x += 1
        guess = int(input("What is your guess? [enter a number 1-4]"))
        if correct == guess:
            print("You were correct!")
        else:
            print(f"That's not correct. The correct answer was: {correct}")
    return score


if __name__ == '__main__':

    print("Hi, welcome to PyQuiz, a python created study tool that will help prepare you for your exams!")
    print("Created by Ian Cox")

    terms = []
    defs = []
    star = []

    dec = True

    while dec:
        t = input("Enter a term: ")
        terms.append(t)
        d = input("Enter the definition for the term that you just entered: ")
        defs.append(d)
        again_correct = True
        while again_correct:
            cont = input("Would you like to add another term + definition or stop ['y' to add more, 'n' to stop]: ")
            if cont == 'n':
                again_correct = False
                dec = False
            elif cont == 'y':
                again_correct = False
            elif cont != 'y' and cont != 'n':
                print("That was an invalid response, try again.")

    choosing = True
    while choosing:
        mode = input(
            "Now the fun part... What mode would you like to play? \n1.) Flashcards Practice [enter '1'] \n2.) "
            "Multiple "
            "Choice Game [enter '2']")
        if mode == '1':
            playflip(terms, defs)
            print("\nThanks for playing!")
            exit()
        elif mode == '2':
            mult(terms, defs)
            print("\nThanks for playing!")
            exit()
        else:
            print("The value that you entered was invalid... Please try again!") # this will cycle back to the start
            # of the while loop so the user can choose again





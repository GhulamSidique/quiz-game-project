# Ghulam Sidique
# gsidique37@gmail.com

# following questions can be extended in size
# the correst options are the keys of the dictionary
questions = {
    "What is the result of 2+9 ?": "B",
    "What is the result of 12*5 ?": "C",
    "What is the result of 16/4 ?": "D",
    "What is the result of 55-27 ?": "A",
}

# these are the set options only chose those ones which are correct
# only options are visible to the user but not the correct answers
options = [
    ["A. 13", "B. 11", "C. 11.5", "D. All"],
    ["A. 40", "B. 50", "C. 60", "D. 62"],
    ["A. 4", "B. 2", "C. 8/2", "D. A & C"],
    ["A. B & C", "B. 29-1", "C. 28", "D. 27"],
]

# to pass the test the user has to obtain 60% score
passing_marks = 60

# this fuction will separate the qustions along with the options and also takes the input of the options from the user
def game():
    guesses = []  # to append the guesses here latter on
    correct_gusesse = 0  # initially no correct answer
    question_num = 1  # starting from qustion 1

    # following loop will print all the qustions which are in the list
    for key in questions:
        print("_____________________________")
        print(key)  # this will print the qustions

        # following loop will print all the options along with a single question
        for o in options[
            question_num - 1
        ]:  # [question_num-1] will select the question from location 0 = 1st question
            print(o)  # this will print all the options related to a single question

        print("Enter A, B, C or D :")
        guess = input("\n\tAnswer = :").upper()  # take input
        guesses.append(
            guess
        )  # the guess will be appended to the guesses list which was initially empty
        correct_gusesse += check(
            questions.get(key), guess
        )  # checks the correct answers and adds in it
        question_num += 1  # increment in qusetins by 1
    score(correct_gusesse, guesses)  # it is the function that will display the score


# this function will check the guesses of the user with the set answers
def check(answer, guess):
    if answer == guess:
        print("\nCORRECT")
        return 1  # this will add 1 point if the answer is correct
    else:
        print("WRONG!!!")
        return 0  # this will add 0 in case the answer is wrong


# this function will calculate the score of the guesses a user make
def score(correct_guesses, guesses):
    print("_____________________________")
    print("\n\t\tYour RESULT is: \n")

    print("\t\tCorrect Answers = ", end="")
    for q in questions:
        print(
            questions.get(q), end=" "
        )  # the set answers from dictionary defined above
    print()

    print("\t\tYour Answers    = ", end="")
    for g in guesses:
        print(g, end=" ")  # guesses of a user
    print()

    percentage = int(
        (correct_guesses / len(questions)) * 100
    )  # calculates the total percentage
    print("\n\t\tYour Score is " + str(percentage) + "%")

    message(
        percentage, passing_marks
    )  # message function to display the message whether the test is passed or not


# this function will check the passing percentage criteria and prints the message accordingly
def message(percentage, passing_marks):
    if percentage >= passing_marks:
        print("\n\t\tCogratulations!!\n\t\tYou passed the test")
    else:
        print("\n\t\tOops!! You Failed")


# this function will ask the user whether he wants to play again or not
def play_again():
    print("\nWould you like to play again??")
    print("Press y for Yes and n for No")
    response = input("\n\tYes/No = ").lower()
    if response == "y":
        return True
    else:
        return False


# --------------------------------------------------------------------------------
# the calling of functions starts from here
# --------------------------------------------------------------------------------

game()  # called the game function

while play_again():  # will run only when user wants to play again
    game()
print("\n\t\tThanks for attempting test")  # if user deos not want to play again

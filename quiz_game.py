
"""print("====================================")
print("         PYTHON QUIZ GAME")
print("====================================")

# Store questions and answers in a list

questions = [
    [
        "Which keyword is used to check a condition?",
        "A. for",
        "B. if",
        "C. print",
        "D. input",
        "B"
    ],
    [
        "Which data type stores True or False?",
        "A. int",
        "B. str",
        "C. bool",
        "D. float",
        "C"
    ],
    [
        "What is the output of 5 + 3?",
        "A. 2",
        "B. 8",
        "C. 15",
        "D. 53",
        "B"
    ],
    [
        "Which loop runs while a condition is True?",
        "A. if",
        "B. break",
        "C. while",
        "D. pass",
        "C"
    ],
    [
        "Which symbol checks equality?",
        "A. =",
        "B. ==",
        "C. !=",
        "D. +",
        "B"
    ]
]

# Start the game

play_again = "yes"

while play_again == "yes":

    name = input("\nEnter your name: ")
    score = 0
    total_questions = 5

    print("\nWelcome", name)
    print("Let's start the quiz!")

    # Display questions using for loop

    question_number = 1

    for question in questions:

        print("\nQuestion", question_number)
        print(question[0])

        print(question[1])
        print(question[2])
        print(question[3])
        print(question[4])

        # Validate user input

        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        while answer not in ["A", "B", "C", "D"]:
            print("Invalid input! Please enter A, B, C or D.")
            answer = input("Enter your answer: ").strip().upper()

        # Check answer

        if answer == question[5]:
            print("Correct answer!")
            score = score + 1

        else:
            print("Wrong answer!")
            print("Correct answer is:", question[5])

        question_number = question_number + 1

    # Calculate result

    percentage = (score / total_questions) * 100

    print("\n====================================")
    print("             QUIZ RESULT")
    print("====================================")

    print("Player:", name)
    print("Total questions:", total_questions)
    print("Correct answers:", score)
    print("Wrong answers:", total_questions - score)
    print("Percentage:", percentage, "%")

    # Performance feedback

    if percentage >= 80:
        print("Excellent performance!")

    elif percentage >= 60:
        print("Very good! Keep learning.")

    elif percentage >= 40:
        print("Good try! Practice more.")

    else:
        print("Don't give up! Try again.")

    # Ask to play again

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    while play_again != "yes" and play_again != "no":
        print("Please enter yes or no.")
        play_again = input("Play again? (yes/no): ").strip().lower()

print("\nThank you for playing!")
print("Goodbye!")"""

import random

print("====================================")
print("         PYTHON QUIZ GAME")
print("====================================")

questions = [
    ["Which keyword is used to check a condition?",
     "A. for", "B. if", "C. print", "D. input", "B"],

    ["Which data type stores True or False?",
     "A. int", "B. str", "C. bool", "D. float", "C"],

    ["What is the output of 5 + 3?",
     "A. 2", "B. 8", "C. 15", "D. 53", "B"],

    ["Which loop runs while a condition is True?",
     "A. if", "B. break", "C. while", "D. pass", "C"],

    ["Which symbol checks equality?",
     "A. =", "B. ==", "C. !=", "D. +", "B"]
]

play_again = "yes"

while play_again == "yes":

    name = input("\nEnter your name: ")
    score = 0

    random.shuffle(questions)

    for question in questions:

        print("\n" + question[0])

        print(question[1])
        print(question[2])
        print(question[3])
        print(question[4])

        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        while answer not in ["A", "B", "C", "D"]:
            print("Invalid answer!")
            answer = input("Enter A/B/C/D: ").strip().upper()

        if answer == question[5]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer:", question[5])

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n========== QUIZ RESULT ==========")
    print("Player:", name)
    print("Total Questions:", total_questions)
    print("Correct Answers:", score)
    print("Wrong Answers:", total_questions - score)
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 60:
        print("Very good!")
    elif percentage >= 40:
        print("Good try!")
    else:
        print("Keep practicing!")

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    while play_again != "yes" and play_again != "no":
        print("Please enter yes or no.")
        play_again = input("Play again? (yes/no): ").strip().lower()

print("\nThank you for playing!")
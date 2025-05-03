#Create the Quiz program that read the output file of the Quiz Creator.
#The user will answer the randomly selected question and check if the answer is correct.

#Modules imported
import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

output_file = "quiz_questions.txt"

#For a more engaging quiz_program or a main menu like
while True:
    print(Fore.YELLOW + "=========== Welcome to the Quiz! ==========")
    print(Fore.YELLOW + "What would you like to do?")
    print("1. Start Quiz")
    print("2. Exit")
    user_choice = input("\nEnter your choice (1 or 2): ").strip()

    if user_choice == '1':
        # A program that checks and reads the output file
        with open(output_file, "r", encoding="utf-8") as file:
            content = file.read().strip()

        question_blocks = content.split("=" * 50)
        questions = []

        for block in question_blocks:
            lines = block.strip().split('\n')
            if len(lines) < 6:
                continue

            question_text = lines[0][3:].strip()
            choices = {
                'a': lines[1][3:].strip(),
                'b': lines[2][3:].strip(),
                'c': lines[3][3:].strip(),
                'd': lines[4][3:].strip()
            }
            correct_answer = lines[5].split(":")[1].strip().lower()

            questions.append((question_text, choices, correct_answer))
#A program that select the questions randomly
        random.shuffle(questions)
        score = 0

        for index, (question, choices, correct) in enumerate(questions, 1):
            print(f"\n{Style.BRIGHT}Question {index}/{len(questions)}: {question}")
            for key, value in choices.items():
                print(f"  {key}. {value}")

            while True:
                user_answer = input("\nYour answer (a/b/c/d): ").lower()
                if user_answer in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print(Fore.YELLOW + "Invalid input. Please enter a, b, c, or d.")

            if user_answer == correct:
                print(Fore.GREEN + "Correct!")
                score += 1
            else:
                print(Fore.RED + f"Incorrect. The correct answer was: {correct}. {choices[correct]}")
    # Displaying the user's score
        print(f"\n{Style.BRIGHT}Quiz Finished! You scored {Fore.CYAN}{score}/{len(questions)}{Style.RESET_ALL}.\n")

#If the user wants to exit
    elif user_choice == '2':
        print(Fore.CYAN + "\nThank you for playing. Goodbye!")
        break
    else:
        print(Fore.YELLOW + "Invalid choice. Please enter 1 or 2.\n")


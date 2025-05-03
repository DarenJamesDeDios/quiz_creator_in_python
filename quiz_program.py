#Create the Quiz program that read the output file of the Quiz Creator.
#The user will answer the randomly selected question and check if the answer is correct.

#Modules imported
import random

#A program that checks and reads the output file
print("Please enter your saved output file created by quiz_creator program")
output_file = input()

with open(output_file, "r", encoding="utf-8") as file:
    content = file.read().strip()
#With this program the question is parse and stored onto a list
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
    print(f"Question {index}/{len(questions)}:{question}")
    for key, value in choices.items():
        print(f"  {key}. {value}")
    while True:
        user_answer = input("\nYour answer (a/b/c/d): ").lower() #so that the answer is always in lowercase for checking
        if user_answer in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Invalid input. Please enter a, b, c, or d.")
#A program that checks if the answer is correct

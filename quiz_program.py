#Create the Quiz program that read the output file of the Quiz Creator.
#The user will answer the randomly selected question and check if the answer is correct.

#A program that checks and reads the output file
print("Please enter your saved output file created by quiz_creator program")
output_file = input()

with open(output_file, "r", encoding="utf-8") as file:
    content = file.read().strip()

question_blocks = content.split("=" * 50)
questions = []

#A program that select the questions randomly
#A program that checks if the answer is correct
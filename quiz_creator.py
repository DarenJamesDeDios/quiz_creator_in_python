# Open the file in append mode to store the questions and answers
file = open("questions.txt", "a")

while True:
    # Ask for the question and answers
    question = input("Enter the question: ")
    answer_a = input("Enter answer a: ")
    answer_b = input("Enter answer b: ")
    answer_c = input("Enter answer c: ")
    answer_d = input("Enter answer d: ")
    correct_answer = input("Enter the correct answer (a, b, c, or d): ")

    # Write the question and answers to the file
    file.write(f"Question: {question}\n")
    file.write(f"a) {answer_a}\n")
    file.write(f"b) {answer_b}\n")
    file.write(f"c) {answer_c}\n")
    file.write(f"d) {answer_d}\n")
    file.write(f"Correct answer: {correct_answer}\n\n")

    # Ask if the user wants to add another question
    exit_choice = input("Would you like to add another question? (y/n): ")
    if exit_choice.lower() != 'y':
        print("Exiting...")
        break

# Close the file when finished
file.close()

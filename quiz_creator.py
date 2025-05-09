#Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.
import time  #Importing time for delays of printed strings .

filename =  "quiz_questions.txt"

print("\033[33m========\033[1mWelcome to Quiz Creator\033[0m\033[33m=========\033[0m") #Added color for a bit of effects hehe
time.sleep(2)

while True:
    #Asking the user to write a question
    print("\033[33mPlease enter your quiz question.\033[0m")
    questions = input("\033[33mQ\033[0m: ")

    #Asking the user to write 4 possible answer
    print("\033[33mPlease input the 4 possible answer.\033[0m")
    a = input("For letter a: ")
    b = input("For letter b: ")
    c = input("For letter c: ")
    d = input("For letter d: ")

    #Asking for the correct answer
    while True:
        correct_answer = input("The correct answer?(is it a, b, c, or d?): ")
        if correct_answer in ['a', 'b', 'c', 'd']:
            print("\033[33mSaving the question and answer...\033[0m")
            time.sleep(3)
            print("\033[32mDone!\033[0m")
            time.sleep(1)
            break
        else:
            print("\033[31mInvalid input, please choose only a, b, c, or d\033[0m")
            time.sleep(1)

    #A program that saves the quiz questions into a file
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"Q: {questions}\n")
        file.write(f"a. {a}\n")
        file.write(f"b. {b}\n")
        file.write(f"c. {c}\n")
        file.write(f"d. {d}\n")
        file.write(f"Correct Answer: {correct_answer}\n\n")
        file.write("=" * 50 + "\n\n")

    #Asking the user if they want to stop adding more quiz questions
    while True:
        print("\033[33mDo you want to add another quiz question?\033[0m")
        respond = input("\033[32myes\033[0m or \033[31mno\033[0m?: ").lower()
        if respond == 'yes':
            break
        elif respond == 'no':
            print("\033[33mExiting...\033[0m")
            time.sleep(3)
            print("Your quiz questions are now \033[32msaved\033[0m.")
            exit()
        else:
            print("Only \033[32myes\033[0m or \033[31mno\033[0m answer are allowed my friend.")
            time.sleep(1)
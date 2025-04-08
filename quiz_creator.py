#Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.
#Importing a module for saving purposes
import os

filename =  "quiz_questions.txt"

while True:
    #Asking the user to write a question
    print("Please enter your quiz question.")
    questions = input("Q: ") 
    #Asking the user to write 4 possible answer
    print("Please input the 4 possible answer.")
    a = input("For letter a: ")
    b = input("For letter b: ")
    c = input("For letter c: ")
    d = input("For letter d: ")
    #Asking for the correct answer
    correct_answer = input("The correct answer?(is it a, b, c, or d?): ")
    #Asking the user if they want to stop adding more quiz questions
    while True:
        print("Do you want to add another quiz question?")
        respond = input("yes or no?: ").lower()
        if respond == 'yes':
            break
        elif respond == 'no':
            print("Exiting, your quiz questions are now saved.")
            #A program that saves the quiz questions into a file
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"Q: {questions}\n")
                file.write(f"a. {a}\n")
                file.write(f"b. {b}\n")
                file.write(f"c. {c}\n")
                file.write(f"d. {d}\n")
                file.write(f"Correct Answer: {correct_answer}\n\n")
            exit()
        else:
            print("Only yes or no answer are allowed my friend.")
#Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.
while True:
    #Asking the user to write a question
    print("Please enter your quiz question")
    question = input("Q: ") 
    #Asking the user to write 4 possible answer
    print("Please input the 4 possible answer")
    a = input("For letter a: ")
    b = input("For letter b: ")
    c = input("For letter c: ")
    d = input("For letter d: ")
    #Asking for the correct answer
    correct_answer = input("The correct answer?(is it a, b, c, or d?): ")
    #Asking the user if they want to stop adding more quiz questions
    print("Do you want to add another quiz question?")
    respond = input("yes or no?: ").lower
    if respond == "yes":
        continue
    elif respond == "no":
        break
    else:
        print("Only yes or no answer are allowed my friend")
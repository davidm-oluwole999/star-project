import random

# question bank
questions = {
    "General Knowledge": [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What year did the Titanic sink?", "answer": "1912"}
    ],
    "Science": [
        {"question": "What is the chemical symbol for water?", "answer": "H2O"},
        {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"}
    ],
    "Sports": [
        {"question": "Who holds the record for the most goals in a single World Cup?", "answer": "Just Fontaine"},
        {"question": "Which country was the first to win the FIFA World Cup?","answer":"Uruguay"}
   ]   }   

def ask_question(category):
    #Selects a random question from the chosen category.
    question = random.choice(questions[category])
    
    #Prompts the user to answer the question.
    user_answer = input(question["question"] + "\n")

    #Compares the user's answer (converted to lowercase) with the correct answer (also in lowercase). 
    # Returns True if they match, otherwise False.
    return user_answer.lower() == question["answer"].lower()

def quiz():
    #Initializes the score.
    score = 0
   
    #Welcomes the user
    print("Welcome to the Quiz Game!")

    # Displays available categories.
    print("Categories: General Knowledge, Science, Sports")
    
    #Prompts the user to choose a category
    #Formats it with .title() to ensure the first letter of each word is capitalized.
    category = input("Choose a category: ").title()
    
    #Checks if the chosen category exists.
    if category in questions:
        
        # Loops through each question in the category.
        for _ in range(len(questions[category])):
           
           #Checks if the user answered correctly.
            if ask_question(category):
                
                 #Increases the score if the answer is correct.
                score += 1
                
                #Tells the user that they are correct.
                print("Correct!")
            else:
                #Tells they user that they got the answer wrong.
                print("Wrong!")
        #Tells the user their final score.
        print(f"Your final score is {score}/{len(questions[category])}")
    #If the chosen category does not exist:
    else:
        #Tells the user that they have chosen an invalid category
        print("Invalid category!")

#Starts the game by calling the function
quiz()
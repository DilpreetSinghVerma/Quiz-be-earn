import random
import os

# Kaun Banega Crorepati
print("Let's start our game")

# Questions and answers (with correct answers)
questions = {
    "Q1. Who is the Prime Minister of India?": {
        "options": {
            "A": "Rahul Gandhi", 
            "B": "Amit Shah", 
            "C": "Kejriwal", 
            "D": "Narendra Modi"
        },
        "correct": "D"
    },
    "Q2. What is the capital of India?": {
        "options": {
            "A": "Kolkata", 
            "B": "Mumbai", 
            "C": "Chennai", 
            "D": "Delhi"
        },
        "correct": "D"
    },
    "Q3. Which river flows through Delhi?": {
        "options": {
            "A": "Godavari", 
            "B": "Ganga", 
            "C": "Yamuna", 
            "D": "Brahmaputra"
        },
        "correct": "C"
    },
    "Q4. What is the highest mountain in the world?": {
        "options": {
            "A": "Kangchenjunga", 
            "B": "K2", 
            "C": "Mount Everest", 
            "D": "Lhotse"
        },
        "correct": "C"
    },
    "Q5. Who painted the Mona Lisa?": {
        "options": {    
            "A": "Michelangelo", 
            "B": "Raphael", 
            "C": "Donatello", 
            "D": "Leonardo da Vinci"
        },
        "correct": "D"
    }
}

# Initialize money and asked questions list
money = 0
asked_questions = []

# Load high score from file
if os.path.exists("money.txt"):
    with open("money.txt", "r") as f:
        content = f.read().strip()
        if content:
            high_score = int(content)
        else:
            high_score = 0
else:
    high_score = 0

# Game loop
while True:
    # Choose a random question that hasn't been asked yet
    available_questions = [q for q in questions if q not in asked_questions]
    if available_questions:
        question = random.choice(available_questions)
        asked_questions.append(question)
        answers = questions[question]["options"]
        correct_answer = questions[question]["correct"]

        # Print question and options in sequence
        print(question)
        for key in sorted(answers.keys()):
            print(f"({key}) = {answers[key]}")

        # Get user answer
        answer = input("Enter your answer carefully: ").upper()

        # Check if answer is correct
        if answer == correct_answer:
            print("Congratulations! You won 1000 rupees.")
            money += 1000
            print(f"Current money: {money}")

            # Update high score
            if money > high_score:
                high_score = money
                with open("money.txt", "w") as f:
                    f.write(str(high_score))
                print(f"New high score: {high_score}")

        else:
            print("Wrong Answer.")
            print(f"Game Over! Final money: {money}")
            print(f"High Score: {high_score}")
            break
    else:
        print("Game Over! You have answered all the questions.")
        print(f"Final money: {money}")
        print(f"High Score: {high_score}")
        break

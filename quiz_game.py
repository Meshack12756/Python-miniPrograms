import random

questions = {"Which tech stack does Wikipedia use: ": "LAMP stack",
             "What does CPU stand for? ": "Central Processing Unit",
             "What is the main programming language used for web development? ": "JavaScript",
             "Who founded Microsoft? ": "Bill Gates",
             "What does HTTP stand for? ": "Hypertext Transfer Protocol",
             "Which company developed the Python programming language? ": "Python Software Foundation",
             "What year was the first iPhone released? ": "2007",
             "What does RAM stand for in computing? ": "Random Access Memory",
             "Which search engine is owned by Microsoft? ": "Bing",
             "What is the name of Apple's macOS terminal application? ": "Terminal",
             "Which version control system is widely used for software development? ": "Git",
             "What does API stand for? ": "Application Programming Interface",
             "Which programming language is known for data science and AI? ": "Python",
             "What company developed the first graphical web browser? ": "Netscape",
             "Which database language is used to manage relational databases? ": "SQL",
             "What does SSD stand for in computing? ": "Solid State Drive"
             }
total = 0
official_limit = 0
user_max_attempts = 5

shuffled_questions = list(questions.items())
random.shuffle(shuffled_questions)

for question, answer in shuffled_questions:
    user_answer_input = input(question).strip().lower()
    if user_answer_input == answer.lower():
        print("Correct!")
        total += 10
    else:
        print(f"Incorrect! The correct answer is {answer}.")
        user_max_attempts -= 1
        print(f"{user_max_attempts} attempts left!")

    if official_limit >= user_max_attempts:
        print("Sorry! You have used all your attempts! Game Over!")
        break
      
print(f"Thank you for your time to play our quiz game. You have attained {total} points!")


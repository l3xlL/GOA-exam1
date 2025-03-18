import random

def magic_8_ball():
    answers = [
        "yes",
        "no",
        "maybe",
        "definitely not",
        "ask again later",
        "cannot predict now",
        "most likely",
        "don't count on it"
    ]
    
    question = input("Ask a question: ")
    
    answer = random.choice(answers)
    
    print(f"You asked: {question}")
    print("The magic 8 ball says:", answer)


magic_8_ball()
import random

def magic_8_ball():
    answers = [
        "yes",
        "no",
        "maybe",
        "definitely not",
        "ask again later",
        "most likely"
    ]
    
    question = input("ask a question: ")
    
    answer = random.choice(answers)
    
    print("the magic 8 ball says:", answer)


magic_8_ball()
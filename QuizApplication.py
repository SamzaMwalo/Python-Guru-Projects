"""
How It Works:
Asks questions, takes users answers, calculates score, and show the final result.
"""

# Quiz Application
questions = [
    {
            "question" : "Whats the capital of Kenya?",
            "options" : ["a. Nakuru", "b. Nairobi", "c. Kisumu", "d. Mombasa"],
            "answer" : "b"
    },
    {
        "question" : "Which language is used for data analysis?",
        "options" : ["a. CSS", "b. HTML", "c. Python", "d. Java"],
        "answer" : "c"
    },
    {
        "question" : "Calculate 10 * 10.",
        "options" : ["a. 100", "b.  20", "c. 1010", "d. 1001"],
        "answer" : "a"
    }
]
score = 0
for q in questions:
    print("\n" + q["question"])
    for option in q["options"] :
        print (option)
    user_answer = input("Enter your answer (a/b/c/d):") .upper()
    if user_answer == q["answer"]:
        print("Correct ⭐")
        score =+ 1
    else:
        print("Wrong X")
print("\nFinal Score: ", score, "/", len(questions))

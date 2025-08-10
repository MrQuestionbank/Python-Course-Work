QuestionBank = [
    {
        "question": "What will be the output of the following code?\nprint(type([]) is list)",
        "options": ["a) True", "b) False", "c) list", "d) None"],
        "answer": "a"
    },
    {
        "question": "Which of the following is used to create an empty set in Python?",
        "options": ["a) {}", "b) set()", "c) []", "d) emptyset()"],
        "answer": "b"
    },
    {
        "question": "What will be the output of bool(0) in Python?",
        "options": ["a) 0", "b) False", "c) True", "d) None"],
        "answer": "b"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["a) define", "b) function", "c) def", "d) func"],
        "answer": "c"
    },
    {
        "question": "What will len(\"Python\"[::-1]) return?",
        "options": ["a) 5", "b) 6", "c) Error", "d) None"],
        "answer": "b"
    },
    {
        "question": "Which of the following is mutable in Python?",
        "options": ["a) String", "b) Tuple", "c) List", "d) Integer"],
        "answer": "c"
    },
    {
        "question": "What is the output of 3 * 'ab'?",
        "options": ["a) ababab", "b) ab3", "c) ab ab ab", "d) Error"],
        "answer": "a"
    },
    {
        "question": "Which of the following removes the last element from a list?",
        "options": ["a) list.remove()", "b) list.pop()", "c) list.delete()", "d) list.discard()"],
        "answer": "b"
    },
    {
        "question": "What is the output of bool(\"False\")?",
        "options": ["a) True", "b) False", "c) 'False'", "d) None"],
        "answer": "a"
    },
    {
        "question": "What will be printed by the code below?\n\nx = [1, 2, 3]\nprint(x * 2)",
        "options": ["a) [1, 2, 3, 1, 2, 3]", "b) [2, 4, 6]", "c) Error", "d) [1, 2, 3, 2]"],
        "answer": "a"
    }
]

Total = 0 
for i in QuestionBank: 
    print(i["question"])
    for o in i["options"] : 
        print(o)
    answer = input("Enter your answer (a/b/c/d) : ").lower()
    if answer == i["answer"]: 
        print("✅ Correct !")
        Total += 1
    else: 
        print(f"❌ Wrong ! The Correct answer is : {i['answer']}")
print(f'Your score is {Total} out of 10.')



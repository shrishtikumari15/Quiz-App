questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "Leo Tolstoy"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    }
]

def run_quiz():
    score = 0
    for question in questions:
        print(question["question"])
        for idx, option in enumerate(question["options"]):
            print(f"{idx + 1}. {option}")
        try:
            answer = int(input("Enter your answer (1-4): "))
            if question["options"][answer - 1] == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 4.")
        print()

    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    run_quiz()

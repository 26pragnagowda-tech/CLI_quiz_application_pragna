import json
import random
import os


def load_questions():
    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print("Error: questions.json file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []


def run_quiz(questions):
    score = 0
    total = len(questions)

    random.shuffle(questions)

    print("\n===== CLI QUIZ APPLICATION =====")
    print("Answer the following questions.\n")

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")

        for option, text in question["options"].items():
            print(f"{option}. {text}")

        while True:
            answer = input("Enter your answer (A/B/C/D): ").strip().upper()

            if answer in question["options"]:
                break
            else:
                print("Invalid answer! Please enter A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print(
                f"Wrong answer! Correct answer: "
                f"{question['answer']}"
            )

    percentage = (score / total) * 100 if total > 0 else 0

    print("\n===== QUIZ RESULT =====")
    print(f"Total Questions: {total}")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {total - score}")
    print(f"Final Score: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 50:
        print("Good job! Keep practicing.")
    else:
        print("Keep learning and try again!")


def main():
    questions = load_questions()

    if questions:
        run_quiz(questions)
    else:
        print("No questions available.")


if __name__ == "__main__":
    main()

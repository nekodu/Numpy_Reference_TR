import numpy as np

def numpy_quiz():
    # Create a NumPy array
    array = np.array([1, 2, 3, 4, 5])

    # Question 1: What is the shape of the array?
    shape_question = "What is the shape of the array?"
    shape_options = ["(5,)", "(1, 5)", "(5, 1)", "(1, 1, 5)"]
    shape_answer = "(5,)"

    # Question 2: What is the result of multiplying the array by 3?
    multiplication_question = "What is the result of multiplying the array by 3?"
    multiplication_options = ["[3, 6, 9, 12, 15]", "[1, 6, 9, 12, 15]", "[1,  3, 6, 9, 12, 15]", "[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]"]
    multiplication_answer = "[3, 6, 9, 12, 15]"

    # Question 3: What is the element at index 2 of the array after setting it to 10?
    modification_question = "What is the element at index 2 of the array after setting it to 10?"
    modification_options = ["10", "3", "2", "4"]
    modification_answer = "10"

    # Question 4: What is the size of the array?
    size_question = "What is the size of the array?"
    size_options = ["5", "15", "1", "25"]
    size_answer = "5"

    # Question 5: What is the shape of a reshaped array with dimensions (1, 5)?
    reshape_question = "What is the shape of a reshaped array with dimensions (1, 5)?"
    reshape_options = ["(5,)", "(1, 5)", "(5, 1)", "(1, 1, 5)"]
    reshape_answer = "(1, 5)"

    # Define questions and options as a dictionary
    questions = {
        shape_question: {"options": shape_options, "answer": shape_answer},
        multiplication_question: {"options": multiplication_options, "answer": multiplication_answer},
        modification_question: {"options": modification_options, "answer": modification_answer},
        size_question: {"options": size_options, "answer": size_answer},
        reshape_question: {"options": reshape_options, "answer": reshape_answer}
    }

    # Quiz loop
    score = 0
    total_questions = len(questions)
    for question, data in questions.items():
        print(question)
        for i, option in enumerate(data["options"], start=1):
            print(f"{i}. {option}")
        user_answer = input("Enter your answer (1-4): ").strip()
        if user_answer == data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer is {data['answer']}\n")

    print(f"Quiz completed!\nYour score: {score}/{total_questions}")

# Run the quiz
numpy_quiz()
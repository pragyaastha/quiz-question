import time

def ask_question(question, options, correct_option, hint, difficulty):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    if hint:
        print("Hint: " + hint)

    start_time = time.time()
    user_answer = input("Enter the number of your answer (or 'h' for a hint): ")
    end_time = time.time()
    
    if user_answer.lower() == 'h':
        print("Hint: " + hint)
        user_answer = input("Enter the number of your answer: ")
    
    time_taken = end_time - start_time

    is_correct = user_answer == str(correct_option)
    if not is_correct:
        print(f"Incorrect! The correct answer was {correct_option}. {options[correct_option - 1]}")
    return is_correct, time_taken

def run_quiz(questions):
    score = 0
    correct_answers = 0
    total_time = 0

    for question_data in questions:
        question, options, correct_option, hint, difficulty = question_data
        correct, time_taken = ask_question(question, options, correct_option, hint, difficulty)
        total_time += time_taken

        if correct:
            print("Correct!")
            score += difficulty * 10  # More points for higher difficulty
            correct_answers += 1

    print(f"\nYour final score is {score} out of {len(questions) * 10 * 3}")  # Assuming max difficulty is 3
    print(f"You answered {correct_answers} out of {len(questions)} questions correctly.")
    print(f"Total time taken: {total_time:.2f} seconds")

def choose_category():
    categories = ["General Knowledge", "Science", "Literature", "Geography"]
    print("Choose a category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    choice = int(input("Enter the number of your choice: "))
    return categories[choice - 1]

def choose_difficulty():
    difficulties = ["Easy", "Medium", "Hard"]
    print("Choose a difficulty level:")
    for i, difficulty in enumerate(difficulties, 4):
        print(f"{i}. {difficulty}")
    
    choice = int(input("Enter the number of your choice: "))
    return choice  # Returning the index as the difficulty level (1 for Easy, 2 for Medium, 3 for Hard)

def main():
    questions = {
        "General Knowledge": [
            ("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2, "It's known as the City of Light.", 1),
            ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "Jane Austen", "J.K. Rowling"], 1, "The author shares a name with a famous bird.", 2),
            ("In which year did the Titanic sink?", ["1912", "1914", "1916", "1918"], 1, "It happened just before World War I.", 2),
            ("Which artist painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], 3, "The artist was also an inventor.", 1),
            ("What is the smallest country in the world?", ["Monaco", "Nauru", "San Marino", "Vatican City"], 4, "It's located within a city.", 3)
        ],
        "Science": [
            ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 2, "It's named after the Roman god of war.", 1),
            ("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Iron", "Hydrogen"], 1, "It's essential for respiration.", 1),
            ("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"], 2, "It's responsible for energy production.", 2),
            ("What is the chemical formula for water?", ["H2O", "CO2", "O2", "H2O2"], 1, "It's composed of two hydrogen atoms and one oxygen atom.", 1),
            ("Who developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], 2, "He had a famous equation: E=mc^2.", 3)
        ],
        "Literature": [
            ("Who wrote '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Philip K. Dick"], 1, "The author also wrote 'Animal Farm'.", 2),
            ("Which play is also known as 'The Scottish Play'?", ["Macbeth", "Hamlet", "Othello", "King Lear"], 1, "It's a tragedy by William Shakespeare.", 3),
            ("Who wrote 'Pride and Prejudice'?", ["Jane Austen", "Charlotte Bronte", "Emily Bronte", "Mary Shelley"], 1, "The author also wrote 'Sense and Sensibility'.", 2),
            ("Which novel begins with 'Call me Ishmael'?", ["Moby Dick", "The Great Gatsby", "1984", "Brave New World"], 1, "It's about a man's obsession with a white whale.", 3),
            ("Who wrote 'The Great Gatsby'?", ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "T.S. Eliot"], 1, "The author was part of the Lost Generation.", 2)
        ],
        "Geography": [
            ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 4, "It's named after a peaceful term.", 1),
            ("Which river is the longest in the world?", ["Nile", "Amazon", "Yangtze", "Mississippi"], 1, "It's located in Africa.", 3),
            ("What is the capital of Japan?", ["Tokyo", "Kyoto", "Osaka", "Nagoya"], 1, "It's a bustling metropolis.", 1),
            ("Which continent is known as the 'Dark Continent'?", ["Asia", "Africa", "South America", "Australia"], 2, "It's the second largest continent.", 2),
            ("Which country has the most natural lakes?", ["Canada", "USA", "Russia", "Brazil"], 1, "It's known for its vast wilderness.", 3)
        ]
    }

    print("Welcome to the Advanced Quiz Game!")
    category = choose_category()
    difficulty = choose_difficulty()
    
    selected_questions = [q for q in questions[category] if q[-1] == difficulty]

    if not selected_questions:
        print("No questions available for this difficulty level. Try another.")
        return
    
    run_quiz(selected_questions)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()

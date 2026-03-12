def kbc_game():
    print("🎉 Welcome to Kaun Banega Crorepati 🎉")
    print("--------------------------------------")

    questions = [
        {
            "question": "1. Who is the Prime Minister of India?",
            "options": ["A. Narendra Modi", "B. Rahul Gandhi", "C. Arvind Kejriwal", "D. Yogi Adityanath"],
            "answer": "A",
            "money": 1000
        },
        {
            "question": "2. What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C",
            "money": 5000
        },
        {
            "question": "3. Which language is used for AI and ML mostly?",
            "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
            "answer": "B",
            "money": 10000
        },
        {
            "question": "4. Who is known as the Father of Computer?",
            "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Elon Musk"],
            "answer": "A",
            "money": 20000
        }
    ]

    total_money = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            total_money = q["money"]
            print("✅ Correct Answer!")
            print("You won ₹", total_money)
        else:
            print("❌ Wrong Answer!")
            print("Game Over 😢")
            print("You won total ₹", total_money)
            break
    else:
        print("\n🎉 Congratulations! You won ₹", total_money)

kbc_game()

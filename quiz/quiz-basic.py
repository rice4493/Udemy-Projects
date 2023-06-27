import json

with open("quiz.json", 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["questions"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, ".", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_ans"]:
        score += 1
        result = "Correct answer!"
    else:
        result = "Wrong answer :("

    message = f"\n{index + 1}. {result}\nYour answer: {question['user_choice']}"
    f"Correct answer: {question['correct_ans']}"
    print(message)

print("\nYour score is ", score, "/", len(data))

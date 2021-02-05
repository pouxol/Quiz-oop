from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    quest = Question(question["text"], question["answer"])
    question_bank.append(quest)

quiz = QuizBrain(question_bank)

while quiz.still_hast_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score_number}/{len(question_bank)}")

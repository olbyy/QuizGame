from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random
question_bank = []
score = 0
is_playing = True

for i in question_data:
    question_bank.append(Question(i["category"], i["type"], i["question"], i["correct_answer"], i["incorrect_answers"]))
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score was {quiz.score}/{quiz.question_number}")
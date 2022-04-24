from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank += [Question(question["text"], question["answer"])]

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_have_question():
    quiz_brain.next_question()
    if not quiz_brain.check_answer():
        break
    print("")

print("You've completed the quiz")
print(f"Your final score was : {quiz_brain.score}/{len(quiz_brain.question_list)}")
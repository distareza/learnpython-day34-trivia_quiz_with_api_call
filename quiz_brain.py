class QuizBrain:
    question_number = 0
    score = 0
    user_answer = ""
    correct_answer = ""
    question_list = []

    def __init__(self, question_data):
        self.question_number = 0
        self.question_list = question_data

    def next_question(self):
        if not self.still_have_question():
            print("No more question")
            return False

        question = self.question_list[self.question_number]
        self.correct_answer = question.answer
        self.question_number += 1

        while True:
            self.user_answer = input(f"Q.{self.question_number}: {question.text} ? (True/False) :")
            if self.user_answer.lower() == "true" or self.user_answer.lower() == "false":
                break

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self):
        if self.user_answer.lower() == self.correct_answer.lower():
            self.score += 1
            print(f"You are right, Score : {self.score}/{self.question_number}")
            return True
        else:
            print(f"Sorry You are Lose, Score : {self.score}/{self.question_number}")
            return False

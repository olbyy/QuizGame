from data import question_data
class Question:
    def __init__(self, category, _type, question, correct_answer, incorrect_answer):
        self.category = category
        self._type = _type
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answer = incorrect_answer


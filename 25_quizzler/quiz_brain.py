from question_model import Question


class QuizBrain:
    """Quiz manager class"""

    def __init__(self, q_list: list[Question]):
        self.question_number = 0
        self.question_list = q_list
        self.current_answer = ""
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        item = self.question_list[self.question_number]
        self.current_answer = item.answer
        self.question_number += 1
        return f"Q.{self.question_number}: {item.text}"

    def check_answer(self, u_answer):
        if u_answer == self.current_answer:
            self.score += 1

        return u_answer == self.current_answer

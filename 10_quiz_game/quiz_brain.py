class QuizBrain:
    """Quiz manager class"""

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        answer = ""
        while answer not in ("True", "False"):
            answer = input(f"Q.{self.question_number}: {item.text} "
                           "(True/False)?: ").title()
        self.check_answer(answer, item.answer)

    def check_answer(self, u_answer, q_answer):
        if u_answer == q_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer is {q_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")

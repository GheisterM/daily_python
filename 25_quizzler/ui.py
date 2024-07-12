from tkinter import Tk, Label, Canvas, Button, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#32485C"
CORRECT_COLOR = "#29B677"
INCORRECT_COLOR = "#F1857A"

SCORE_FONT = ("arial", 10, "bold")
QUESTION_FONT = ("arial", 20, "italic")

TRUE_IMG_PATH = "25_quizzler/images/true.png"
FALSE_IMG_PATH = "25_quizzler/images/false.png"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.reset = None

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20)

        self.score_label = Label(text="", font=SCORE_FONT)
        self.score_label.config(fg="white", bg=THEME_COLOR, pady=20)
        self.score_label.grid(column=1, row=0)
        self.update_score()

        self.q_canvas = Canvas(width=300, height=250, bg="white")
        self.q_canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.q_text = self.q_canvas.create_text(
            150,
            125,
            width=270,
            text="Question goes here",
            fill=THEME_COLOR,
            font=QUESTION_FONT
        )

        true_img = PhotoImage(file=TRUE_IMG_PATH, height=97, width=100)
        self.true_button = Button(
            image=true_img,
            highlightthickness=0,
            command=self.select_true
        )
        self.true_button.grid(column=0, row=2, pady=20)

        false_img = PhotoImage(file=FALSE_IMG_PATH)
        self.false_button = Button(
            image=false_img,
            highlightthickness=0,
            command=self.select_false
        )
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_question()

        self.window.mainloop()

    def update_score(self, score: int = 0):
        self.score_label.config(text=f"Score: {score}")

    def get_question(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        question = self.quiz.next_question()
        self.q_canvas.config(bg="white")
        self.q_canvas.itemconfig(
            self.q_text,
            text=question,
            fill=THEME_COLOR
        )

    def game_over(self):
        message = "You completed the quiz!\nYour final score was: {}/{}."
        message = message.format(self.quiz.score, self.quiz.question_number)
        self.q_canvas.config(bg="white")
        self.q_canvas.itemconfig(
            self.q_text,
            text=message,
            fill=THEME_COLOR
        )

    def give_results(self, correct: bool):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        color = CORRECT_COLOR if correct else INCORRECT_COLOR
        self.q_canvas.config(bg=color)
        self.q_canvas.itemconfig(self.q_text, fill="white")
        self.update_score(self.quiz.score)
        if self.quiz.still_has_questions():
            self.reset = self.window.after(1000, self.get_question)
        else:
            self.reset = self.window.after(1000, self.game_over)

    def select_true(self):
        result = self.quiz.check_answer("True")
        self.give_results(result)

    def select_false(self):
        result = self.quiz.check_answer("False")
        self.give_results(result)

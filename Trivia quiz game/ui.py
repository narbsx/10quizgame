from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.true = PhotoImage(file="images/true.png")
        self.false = PhotoImage(file="images/false.png")
        self.score_text = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_text.config(padx=20, pady=20)
        self.score_text.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=260,
            text="",
            font="Arial 20 italic",
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.true_button = Button(image=self.true, highlightthickness=0, command=self.true_pressed)
        self.true_button.config(padx=20, pady=20, bd=0)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false, highlightthickness=0, command=self.false_pressed)
        self.false_button.config(padx=20, pady=20, bd=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_text.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached the end of quiz, your final score is {self.quiz.score}.")
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz_brain = quiz_brain
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0/10', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question text ", fill=THEME_COLOR, width=280,
                                                     font=("Arial", 20, "italic"))
        self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.button_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.button_false)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def button_true(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def button_false(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():

            self.score_label.config(text=f'Score: {self.quiz_brain.score}/10')
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

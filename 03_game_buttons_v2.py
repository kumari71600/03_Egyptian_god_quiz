from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.quiz_frame = Frame(padx=10, pady=10)
        self.quiz_frame.grid()

        self.push_me_button = Button(self.quiz_frame, text="Push me",
                                     command=self.to_quiz)
        self.push_me_button.grid(row=1)

    def to_quiz(self):

        # retrieve # of questions
        num_questions = 5

        root.withdraw()
        Quiz(self, num_questions)

        self.quiz_frame = Frame(self.quiz_frame)
        self.quiz_frame.grid(row=3)

        self.mystery_box_label = Label(self.quiz_frame, text="xxxxxx",
                                       font="Arial 16 bold")
        self.mystery_box_label.grid(row=0)

        # Buttons frame ( row 3)

        self.quiz_frame = Frame(self.quiz_frame)
        self.quiz_frame.grid(row=3)

        # Button Font
        button_font = "Oswald 12 bold"

        # 10 Button
        self.low_quiz_button = Button(self.quiz_frame, text="Low ($5)",
                                        font=button_font,
                                        command=lambda: self.to_quiz(1))
        self.low_quiz_button.grid(row=0, column=0, pady=10)

        # 20 Button
        self.med_quiz_button = Button(self.quiz_frame, text="Medium (10$)",
                                        font=button_font,
                                        command=lambda: self.to_quiz(2))
        self.med_quiz_button.grid(row=0, column=1, pady=10, padx=5)

        # 30 Button
        self.high_quiz_button = Button(self.quiz_frame, text="High (15$)",
                                         font=button_font,
                                         command=lambda: self.to_quiz(3))
        self.high_quiz_button.grid(row=0, column=2, pady=10, padx=5)


    def to_quiz(self):
        Game(self)





class Quiz:
    def __init__(self, partner, num_questions):
        print(num_questions)

        # GUI Setup
        self.quiz_box = Toplevel()

        # If users press cross at top, game quits
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.quiz_frame, wrap=300, justify=LEFT,
                                        text= "Press Next for your first question",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes go here (row 2)
        self.quiz_frame = Frame(self.quiz_frame)
        self.quiz_frame.grid(row=2, pady=10)




    def to_quit(self):
        root.destroy()













# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Egyptian gods quiz")
    play = Start(root)
    root.mainloop()
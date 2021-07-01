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


# class Quiz:

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
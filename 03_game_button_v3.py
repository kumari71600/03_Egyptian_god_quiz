from tkinter import *


class Start:
    def __init__(self, partner,):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg="#D4E1F5")
        self.start_frame.grid()

        # background
        background = "#D4E1F5"

        # God Quiz Heading (row 0)
        self.egyptian_god_label = Label(self.start_frame, text="Egyptian God Quiz",
                                       font="Arial 16 bold", bg=background)
        self.egyptian_god_label.grid(row=0)

        # Initial instructions (row 1)
        self.god_instructions_label = Label(self.start_frame, text=" choose the amount of questions "
                                                                 "you would like to answer",
                                          font="Arial 8 italic", fg="black", bg=background)
        self.god_instructions_label.grid(row=1)

        # to_quiz button frame
        self.to_quiz_frame = Frame(self.start_frame, bg=background)
        self.to_quiz_frame.grid(row=2)

        # Buttons frame ( row 3)
        self.level_frame = Frame(self.start_frame, bg=background)
        self.level_frame.grid(row=3)

        # Button Font
        button_font = "Oswald 12 bold"

        # Low Questions Button
        self.low_level_button = Button(self.level_frame, text="10",
                                        font=button_font, bg="#00FF00",
                                        command=lambda: self.to_quiz(1))
        self.low_level_button.grid(row=5, column=0, pady=10, padx=5)

        # Medium Questions Button
        self.med_level_button = Button(self.level_frame, text="20",
                                        font=button_font, bg="#FFFF33",
                                        command=lambda: self.to_quiz(2))
        self.med_level_button.grid(row=5, column=1, pady=10, padx=5)

        # High Questions Button
        self.high_level_button = Button(self.level_frame, text="30",
                                         font=button_font, bg="#FF0000",
                                         command=lambda: self.to_quiz(3))
        self.high_level_button.grid(row=5, column=2, pady=10, padx=5)

        # Button frame for help and statistics (row 5)
        self.start_help_frame = Frame(self.start_frame, bg="#D4E1F5")
        self.start_help_frame.grid(row=5)

        # To quiz button
    def to_quiz(self,):
        Game(self,)




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
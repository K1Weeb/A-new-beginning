from tkinter import *
import random


class Start:
    def __init__(self, parent):
        
        # initialize starting frame
        self.main_frame = Frame(padx=10, pady=10, bg="#0A1428")
        self.main_frame.grid()

        # added labels which will contain text
        self.text_label = Label(self.main_frame, font="arial 11", bg="#0A1428", text="Welcome to the League of Legends", padx=10, pady=10, fg="#C89B3C")
        self.text_label.grid(row=0)

        # make a difficulty selection label and frame difficulties
        self.difficulty_label = Label(self.main_frame, bg="#0A1428", font="arial 14 bold", fg="#C89B3C", text="SELECT A DIFFICULTY", padx=10, pady=10, justify=CENTER)
        self.difficulty_label.grid(row=1)

        self.difficulty_frame = Frame(self.main_frame, padx=10, pady=10, bg="#0A1428")
        self.difficulty_frame.grid(row=2)

        self.easy_button = Button(self.difficulty_frame, text="EASY", font="arial 9 bold", bg="#0A1428", fg="#C89B3C", relief=GROOVE)
        self.easy_button.grid(row=0, column=0, padx=10, pady=10)

        self.medium_button = Button(self.difficulty_frame, text="MEDIUM", font="arial 9 bold", bg="#0A1428", fg="#C89B3C", relief=GROOVE)
        self.medium_button.grid(row=0, column=1, padx=10, pady=10)

        self.hard_button = Button(self.difficulty_frame, text="HARD", font="arial 9 bold", bg="#0A1428", fg="#C89B3C", relief=GROOVE)
        self.hard_button.grid(row=0, column=2, padx=10, pady=10)

        # make a frame for help and quit buttons
        self.hq_frame = Frame(self.main_frame, padx=10, pady=10, bg="#0A1428")
        self.hq_frame.grid(row=3)

        self.help_button = Button(self.hq_frame, text="HELP", font="arial 10 bold", bg="#DED221")
        self.help_button.grid(row=0, column=0, padx=10, pady=10)

        self.quit_button = Button(self.hq_frame, text="QUIT", font="arial 10 bold", bg="#ab1d17")
        self.quit_button.grid(row=0, column=1, padx=10, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("A New Beginning")

    # adjust starting window size (widthxheight+abscissa+ordinate)
    # root.geometry("500x100+400+300")

    # Set the window icon
    root.iconphoto(False, PhotoImage(file="images/icon.png"))

    # makes window spawn at center
    root.eval('tk::PlaceWindow . center')


    something = Start(root)
    root.mainloop()
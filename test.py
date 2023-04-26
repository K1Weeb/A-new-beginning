from tkinter import *
import random


class Start:
    def __init__(self, parent):
        
        # initialize starting frame
        self.main_frame = Frame(padx=10, pady=10, height=100, width=100)
        self.main_frame.grid()

        # added labels which will contain text
        self.text_label = Label(self.main_frame, font="arial 11", text="I don't remember sh*t", padx=10, pady=10)
        self.text_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("A New Beginning")

    # adjust window size (widthxheight+abscissa+ordinate)
    root.geometry("500x100+400+300")

    something = Start(root)
    root.mainloop()
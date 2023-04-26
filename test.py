from tkinter import *
import random


class Start:
    def __init__(self, parent):
        print("hello world")
        self.main_frame = Frame(padx=10, pady=10, height=100, width=100)
        self.main_frame.grid()

        self.text_label = Label(self.main_frame, text="I don't remember sh*t", padx=10, pady=10)
        self.text_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("A New Beginning")
    root.geometry("500x100")
    something = Start(root)
    root.mainloop()
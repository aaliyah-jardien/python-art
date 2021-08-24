from tkinter import *

# WINDOW FEATURES
window = Tk()
window.geometry("500x300")
window.title("Subtle art of GNF's")


# LABELS
head = Label(window, text="Should I give AF?", font="arial 20 bold")
head.place(x=100, y=25)

ques = Label(window, text="Does it affect me?")
ques.place(x=170, y=120)

window.mainloop()

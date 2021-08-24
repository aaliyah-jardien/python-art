from tkinter import *

# WINDOW FEATURES
window = Tk()
window.geometry("500x300")
window.title("Subtle art of GNF's")

# LABELS
head = Label(window, text="Should I give AF?", font="arial 20 bold")
head.place(x=100, y=25)

ques = Label(window, text="Does it annoy me?")
ques.place(x=170, y=120)

# FUNCTIONS🙂
def yah():
    if button.get == "YES":
        open yes_1
    else button.get == "NO":
        open no_1

# def on_button():
    # if entry.get() == "Screen""screen":
    #     slabel = Label(window, text="Screen was entered")
    #     slabel.pack()
    # else:
    #     tlabel = Label(window, text="")
    #     tlabel.pack()
    #
# BUTTONS
yes = Button(window, text="YES", command="yah")
yes.place(x=150, y=180)

no = Button(window, text="NO", command="nah")
no.place(x=300, y=180)

# button = Button(window, text="Enter", command=on_button)
# button.pack()


window.mainloop()

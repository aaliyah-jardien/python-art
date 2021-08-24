from tkinter import *

root = Tk()
root.geometry("300x300")

# functions
choice=None
def one():
    global choice
    choice='Choice 1'
def two():
    global choice
    choice='Choice 2'
def start():
    global choice
    if choice=='Choice 1':
    elif choice=='Choice 2':
    else:
        #do something else since they didn't press either

# butons
Choice_1_Button=Button(root, text='Choice 1', command=one) #what should it do?
Choice_2_Button=Button(root, text='Choice 2', command=two)
Start_Button=Button(root, text='Start', command=start) #and what about this?

root.mainloop()

# If you want to use radio buttons, it will make it easier:
#
# def start(choice):
#     if choice=='Choice 1':
#         foo1()
#     elif choice=='Choice 2':
#         foo2()
#     else:
#         #do something else since they didn't press either
# var=StringVar(root)
# var.set(None)
# Radiobutton(root, text='Choice 1', value='Choice 1', variable=var).pack()
# Radiobutton(root, text='Choice 2', value='Choice 2', variable=var).pack()
# Button(self.frame, text='Start', command=lambda: start(var.get())).pack()

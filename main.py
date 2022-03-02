
from stack import Stack
from tkinter import *
from tkinter import ttk, messagebox, Canvas

myStack = Stack(5)

root = Tk()
# root.geometry("600x450")
frame = ttk.Frame(root, padding=10)
frame.grid()
# root.title="Candy Dispenser"
canvas = Canvas(frame, background="floral white")
canvas.grid(column=0, row=0, columnspan=10, rowspan=10)

# start values
x0 = 123
x1 = 217
y0 = 257
y1 = 237
step = 25

# canvas.create_line(10,10,370,260)
canvas.create_line(120, 10, 120, 260)
canvas.create_line(120, 260, 220, 260)
canvas.create_line(220, 260, 220, 10)

myTags = []


def _push():
    try:
        tag = "C" + str(myStack.top+1)
        myStack.push(tag)
        canvas.create_rectangle(x0, 257-(step*myStack.top+1), x1,
                                237-(step*myStack.top+1), fill="dodgerblue", tags=tag)
        myTags.append(tag)
    except:
        messagebox.showerror(title='Error', message="Stack Full")


def _pop():
    try:
        canvas.delete(myTags.pop())
        myStack.pop()
    except:
        messagebox.showerror(title='Error', message="Stack is empty")


def _peek():
    try:
        value = myStack.peek()
    except:
        messagebox.showerror(title='Error', message="Stack Empty")
    else:
        messagebox.showinfo(title='Peek', message="Top Value is " + str(value))


ttk.Label(frame, text="Candy Dispenser").grid(column=12, row=0)
ttk.Button(frame, text="Push", width=10, command=_push).grid(column=12, row=1)
ttk.Button(frame, text="Pop", width=10, command=_pop).grid(column=12, row=2)
ttk.Button(frame, text="Peek", width=10, command=_peek).grid(column=12, row=3)

root.mainloop()

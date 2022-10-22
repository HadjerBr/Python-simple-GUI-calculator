from ast import Delete
import tkinter
from tkinter import *

equation = ""

def click(n):
    global equation
    if n == "*":
        e.insert(INSERT, "x")
    else:
        e.insert(INSERT, str(n))
    equation += str(n)

def clear():
    global equation
    e.delete('1.0', END)
    equation = ""

def sonuc():
    global equation
    e.delete('1.0', END)
    try:
        result = eval(equation)
        e.insert(INSERT, str(result))
    except:
        e.insert(INSERT, "ERROR")


win = Tk()
win.iconbitmap("calc1.ico")
win.title("CALCULATOR")
win.geometry("530x532")
win.configure(background="light blue")
win.resizable(0, 0)

e = Text(win, height=2, width=60, bg="white", spacing1=20, spacing3=20, font=("arial 10 bold"))
e.grid(row=0, column=0, columnspan=4, padx = 10, pady = 53)

c = Button(win, width=18, text="C", fg="red", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: clear()) # we can not pass a parameter to buttons that is why we use lambda
c.grid(row=2, column=0)
right = Button(win, width=18, text=")", fg="#0492C2", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(")"))
right.grid(row=6, column=1)
mod = Button(win, width=18, text="%", fg="#0492C2", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click("%"))
mod.grid(row=2, column=2)
div = Button(win, width=18, text="/", fg="#0492C2", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click("/"))
div.grid(row=2, column=3)

seven = Button(win, width=18, text="7", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(7))
seven.grid(row=3, column=0)
eight = Button(win, width=18, text="8", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(8))
eight.grid(row=3, column=1)
nine = Button(win, width=18, text="9", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(9))
nine.grid(row=3, column=2)
time = Button(win, width=18, text="x", fg="#0492C2", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click("*"))
time.grid(row=3, column=3)

four = Button(win, width=18, text="4", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(4))
four.grid(row=4, column=0)
five = Button(win, width=18, text="5", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(5))
five.grid(row=4, column=1)
six = Button(win, width=18, text="6", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(6))
six.grid(row=4, column=2)
sub = Button(win, width=18, text="-", fg="#0492C2", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click("-"))
sub.grid(row=4, column=3)

one = Button(win, width=18, text="1", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(1))
one.grid(row=5, column=0)
two = Button(win, width=18, text="2", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(2))
two.grid(row=5, column=1)
three = Button(win, width=18, text="3", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE ,command= lambda: click(3) )
three.grid(row=5, column=2)
add = Button(win, width=18, text="+", fg="#0492C2", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click("+"))
add.grid(row=5, column=3 )

left= Button(win, width=18, text="(", fg="#0492C2" , bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE, command = lambda: click("("))
left.grid(row=6, column=0)
zero = Button(win, width=18, text="0", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click(0))
zero.grid(row=2, column=1)
point = Button(win, width=18, text=".", bg= "white", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: click("."))
point.grid(row=6, column=2)
equal = Button(win, width=18, text="=", fg="white", bg= "#0492C2", pady=20, activebackground="light blue", borderwidth=1, relief=GROOVE  ,command= lambda: sonuc())
equal.grid(row=6, column=3)
win.mainloop()
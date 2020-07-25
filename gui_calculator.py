from tkinter import *

root = Tk()
root.title("Calculator")

Screen = Entry(root, width = 35, borderwidth = 5)
Screen.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

def button_input(number):
    # Screen.delete(0, END)
    current = Screen.get()
    Screen.delete(0, END)
    Screen.insert(0, str(current) + str(number))
    # Screen.insert (0, number)

def button_add():
    first_number = Screen.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    Screen.delete(0, END)

def button_subtract():
    first_number = Screen.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    Screen.delete(0, END)

def button_multiply():
    first_number = Screen.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    Screen.delete(0, END)

def button_divide():
    first_number = Screen.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    Screen.delete(0, END)


def button_equal():
    second_number = int(Screen.get())
    Screen.delete(0, END)
    if math == "addition":
        Screen.insert(0, f_num + second_number)
    if math == "subtraction":
        Screen.insert(0, f_num - second_number)
    if math == "multiplication":
        Screen.insert(0, f_num * second_number)
    if math == "division":
        Screen.insert(0, f_num / second_number)
    

def clear():
    Screen.delete(0, END)


one = Button(root, text = "1", padx = 30, pady = 30, command = lambda: button_input(1))
two = Button(root, text = "2", padx = 30, pady = 30, command = lambda: button_input(2))
three = Button(root, text = "3", padx = 30, pady = 30, command = lambda: button_input(3))
four = Button(root, text = "4", padx = 30, pady = 30, command = lambda: button_input(4))
five = Button(root, text = "5", padx = 30, pady = 30, command = lambda: button_input(5))
six = Button(root, text = "6", padx = 30, pady = 30, command = lambda: button_input(6))
seven = Button(root, text = "7", padx = 30, pady = 30, command = lambda: button_input(7))
eight = Button(root, text = "8", padx = 30, pady = 30, command = lambda: button_input(8))
nine = Button(root, text = "9", padx = 30, pady = 30, command = lambda: button_input(9))
zero = Button(root, text = "0", padx = 30, pady = 30, command = lambda: button_input(0))
add = Button(root, text = "+", padx = 29, pady = 30, command = button_add)
subtract = Button(root, text = "-", padx = 29, pady = 30, command = button_subtract)
multiply = Button(root, text = "*", padx = 29, pady = 30, command = button_multiply)
divide = Button(root, text = "/", padx = 29, pady = 30, command = button_divide)
equals = Button(root, text = "=", padx = 29, pady = 30, command = button_equal)
clear = Button(root, text = "CLEAR", padx = 16, pady = 30, command = clear)
delete = Button(root, text = "DEL", padx = 22, pady = 30, command = button_input)


zero.grid(row = 4, column = 1)
clear.grid(row = 4, column = 0)
# delete.grid(row = 4, column = 2)

one.grid(row = 3, column = 0)
two.grid(row = 3, column = 1)
three.grid(row = 3, column = 2)

four.grid(row = 2, column = 0)
five.grid(row = 2, column = 1)
six.grid(row = 2, column = 2)

seven.grid(row = 1, column = 0)
eight.grid(row = 1, column = 1)
nine.grid(row = 1, column = 2)

add.grid(row = 1, column = 3)
subtract.grid(row = 2, column = 3)
multiply.grid(row = 3, column = 3)
divide.grid(row = 4, column = 3)

equals.grid(row = 4, column = 2)

root.mainloop()
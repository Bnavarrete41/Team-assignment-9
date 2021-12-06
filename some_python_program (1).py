# Program description goes here
# Updated on: 11/30/2021
# Updated by: Brandon Navarrete/ Alberto Benavides
# This program is supposed to make a calculator and be able to work and function properly as well.
#
# Document what the following lines of code do here:
# This is the start of the program which will be showing how it will start and also how it functions.
# These lines will be the beginning making sure that the calculator will work correctly.
from tkinter import *

root = Tk()

root.title("Simple Calculator")

# Document what the following lines of code do here:
# This area of the code will be showing the amount of columns which the calculator will have and also
# how long and wide the calculator will be as well which shows the grid and entry of it.
# Also the e for Entry will also be showing how it can type on the grid as well.
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Document what the following lines of code do here:
# What this does is it allows you to click on numbers and also delete them if they are not the correct ones
# This also allows for the program to know what the numbers are as well that can be inputted.
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Document what the following lines of code do here:
# This allows for numbers to be cleared whenever something is not correct which you inputted in the calculator.
def button_clear():
    e.delete(0, END)

# Document what the following lines of code do here:
# This is the number generator where if the user inputs a number they will be able to see it
# Also it shows how when the number goes back to 0 then the program will end.
def button_operator(operator):
    first_number = e.get()
    global f_num
    global num_operator
    f_num = int(first_number)
    num_operator = operator
    e.delete(0, END)

# Document what the following lines of code do here

# you might want to consider adding documentation on a line by line basis since
# this is a critical function for the program
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if num_operator == '+':
        e.insert(0, f_num + int(second_number)) # This text will span the first column
    elif num_operator == '*':
        e.insert(0, f_num * int(second_number)) # This text will span the second column
    elif num_operator == '/':
        e.insert(0, f_num / int(second_number)) # This text will span the third column
    elif num_operator == '-':
        e.insert(0, f_num - int(second_number)) # This text will span the fourth column
    else:
        e.insert(0, "Invalid!!!") # This  will say invalid if there is a fifth column

# Document what the following lines of code do here
#
# NOTE: We did not cover Lambda functins in class. A Lambda Function 
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function 
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the 
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression. 


# These lines will be showing that each of the buttons which will be able to be clicked on and
# Also this will also allow the user to interact with each button in the form of button_click and the max amount
# of buttons will be 1-9 and 0
button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Document what the following lines of code do here

# See the description of a Lambda function above
# What this does is that it allows for the buttons divide, multiply, and subtraction to be added to the
# buttons that are able to be interacted with as well.
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# Document what the following lines of code do here

# these allow for the grids to be able to give the columns. For each of them the numbers 1-3 will be in one
# grid and column as well. This also keeps going with the rest from all of the following codes bellow as well.
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Document what the following line of code do here
# This allows for the entire program to keep running without it ending because since it is a
# calculator then this allows for the program to keep going as well.
root.mainloop()
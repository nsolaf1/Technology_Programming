from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
 

def clear():
    global expression 
    expression = "" 
    equation.set("") 
    

if __name__ == "__main__":
    
    gui = Tk()
    
    gui.configure(background="light green")
    gui.title("Calc")
    gui.geometry("270x150")
    
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    
    expression_field.grid(columnspan=4,ipadx=70)
    
    button1 = Button(gui, text="1", fg="black", bg="red", height=1, width=7, command=lambda:press(1))
    button1.grid(row=2, column=0)
    
    button2 = Button(gui, text="2", fg="black", bg="red", height=1, width=7, command=lambda:press(2))
    button2.grid(row=2, column=1)
    
    button3 = Button(gui, text="3", fg="black", bg="red", height=1, width=7, command=lambda:press(3))
    button3.grid(row=2, column=2)
    
    plus = Button(gui, text="+", fg="black", bg='red', height= 1, width=7 ,command=lambda:press("+"))
    plus.grid(row=2, column=4)
    equal = Button(gui, text="=", fg="black", bg='red', height= 1, width=7 ,command=equalpress)
    equal.grid(row=3, column=4)
    
    
gui.mainloop()



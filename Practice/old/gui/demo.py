from tkinter import  Tk, Label, Button

main = Tk()

text = Label(main, text="Hello World!!!")
text.pack()

button = Button(main, text="Click Me", width=30, height=2, command=main.destroy)
button.pack()

main.mainloop()
            
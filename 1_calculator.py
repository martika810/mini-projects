from tkinter import *


def create_calculator_gui():
    root = Tk()
    root.title("My calculator")
    create_result_display(root)
    create_buttons(root)
    root.mainloop()
    return root

def create_result_display(gui):
    result_display = Text(gui, state='disabled', width=30, height=3,background="white", foreground="blue")

    # position screen in window
    result_display.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
    result_display.configure(state='normal')

def create_buttons(gui, write= True, width=7):
    button1= Button(gui, text='1', width=width)
    button1.grid(row=1, column=0)
    button2= Button(gui, text='2', width=width)
    button2.grid(row=1, column=1)
    button3= Button(gui, text='3', width=width)
    button3.grid(row=1, column=2)
    button4= Button(gui, text='4', width=width)
    button4.grid(row=2, column=0)
    button5= Button(gui, text='5', width=width)
    button5.grid(row=2, column=1)
    button6= Button(gui, text='6', width=width)
    button6.grid(row=2, column=2)
    button7= Button(gui, text='7', width=width)
    button7.grid(row=3, column=0)
    button8= Button(gui, text='8', width=width)
    button8.grid(row=3, column=1)
    button9= Button(gui, text='9', width=width)
    button9.grid(row=3, column=2)
    button0= Button(gui, text='0', width=width)
    button0.grid(row=4, column=1)
    buttonEquals= Button(gui, text='=', width=width)
    buttonEquals.grid(row=4, column=2)

    buttonClear= Button(gui, text='Clear', width=width)
    buttonClear.grid(row=1, column=4)
    buttonPlus= Button(gui, text='+', width=width)
    buttonPlus.grid(row=2, column=4)
    buttonMinus= Button(gui, text='-', width=width)
    buttonMinus.grid(row=3, column=4)
    buttonMultiply= Button(gui, text='*', width=width)
    buttonMultiply.grid(row=4, column=4)
    buttonDivide= Button(gui, text='/', width=width)
    buttonDivide.grid(row=5, column=4)



gui = create_calculator_gui()
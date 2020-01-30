from tkinter import *


def create_result_display(gui):
    display_text = StringVar()
    result_display = Label(gui, state='disabled', width=30, height=3,background="white", foreground="blue", textvariable=display_text)
    # position screen in window
    result_display.grid(row=0,column=0, columnspan=4,padx=5,pady=5)
    result_display.configure(state='normal')
    return display_text

def create_buttons(gui, write= True, width=7):
    button1= Button(gui, text='1', width=width, command = lambda : update_top_display_with('1'))
    button1.grid(row=1, column=0)
    button2= Button(gui, text='2', width=width, command = lambda : update_top_display_with('2'))
    button2.grid(row=1, column=1)
    button3= Button(gui, text='3', width=width, command = lambda : update_top_display_with('3'))
    button3.grid(row=1, column=2)
    button4= Button(gui, text='4', width=width, command = lambda : update_top_display_with('4'))
    button4.grid(row=2, column=0)
    button5= Button(gui, text='5', width=width, command = lambda : update_top_display_with('5'))
    button5.grid(row=2, column=1)
    button6= Button(gui, text='6', width=width, command = lambda : update_top_display_with('6'))
    button6.grid(row=2, column=2)
    button7= Button(gui, text='7', width=width, command = lambda : update_top_display_with('7'))
    button7.grid(row=3, column=0)
    button8= Button(gui, text='8', width=width, command = lambda : update_top_display_with('8'))
    button8.grid(row=3, column=1)
    button9= Button(gui, text='9', width=width, command = lambda : update_top_display_with('9'))
    button9.grid(row=3, column=2)
    button0= Button(gui, text='0', width=width, command = lambda : update_top_display_with('0'))
    button0.grid(row=4, column=1)
    buttonEquals= Button(gui, text='=', width=width, command = lambda : update_top_display_with_total())
    buttonEquals.grid(row=4, column=2)

    buttonClear= Button(gui, text='Clear', width=width, command = lambda : clear_top_display())
    buttonClear.grid(row=1, column=4)
    buttonPlus= Button(gui, text='+', width=width, command = lambda: update_top_display_with(' + '))
    buttonPlus.grid(row=2, column=4)
    buttonMinus= Button(gui, text='-', width=width, command = lambda: update_top_display_with(' - '))
    buttonMinus.grid(row=3, column=4)
    buttonMultiply= Button(gui, text='*', width=width, command = lambda: update_top_display_with(' * '))
    buttonMultiply.grid(row=4, column=4)
    buttonDivide= Button(gui, text='/', width=width, command = lambda: update_top_display_with(' / '))
    buttonDivide.grid(row=5, column=4)


def update_top_display_with(text):
    global top_display_text
    current_value = top_display_text.get()
    if(current_value == str(0)):
        top_display_text.set(text)
    else:
        top_display_text.set(current_value + text)

def clear_top_display():
    global top_display_text
    top_display_text.set('0')

def update_top_display_with_total():
    global top_display_text
    current_value = top_display_text.get()
    result = 0
    first_number = int(current_value.split(' ')[0])
    operation = current_value.split(' ')[1]
    second_number = int(current_value.split(' ')[2])

    if(operation == '+'):
        result = first_number + second_number
    if(operation == '-'):
        result = first_number - second_number
    if(operation == '*'):
        result = first_number * second_number
    if(operation =='/'):
        result = first_number / second_number
    top_display_text.set(str(result))



root = Tk()
root.title("My calculator")
total_value = 0
top_display_text = create_result_display(root)
top_display_text.set(total_value)
create_buttons(root)
root.mainloop()
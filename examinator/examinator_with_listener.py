from tkinter import *

questions = ['Is a TV watched by a radio?',
    'Is a TV watched by a radio?',
    'Is a feather heavier than a brick?',
    'Are lemons sweet?',
    'Do fridges punch?',
    'Is butter sweeter than honey?',
    'Can petrol love someone?',
    'Is fire hotter than frost?',
    'Do trees have walls?',
    'Can a horse be brown?']

answer = ['No','Yes','No','No','No', 'No','No','No', 'No', 'Yes']

def create_interface(gui):
    global questions
    question_text = StringVar()
    question_text.set(questions[0])
    Label(gui, textvariable=question_text).grid(row=0, sticky=W)
    var1 = IntVar()
    Checkbutton(gui, text="Yes", variable=var1).grid(row=1, sticky=W)
    var2 = IntVar()
    Checkbutton(gui, text="No", variable=var2).grid(row=2, sticky=W)
    Button(gui, text='Next').grid(row=3, sticky=W, pady=4)

def update_exam_results():
    print('')

root = Tk()
root.title("My Examinator")
create_interface(root)
root.mainloop()
import tkinter as tk
from tkinter import ttk

def update_numeric_label():
    label_numeric.config(text=f'Value: {number_spinbox.get()}')

def update_subject_label():
    label_subject.config(text=f'Subject: {subject_spinbox.get()}')

window = tk.Tk()
window.title('Tkinter Spinbox Widget')
window.geometry('300x200')

# Numeric Spinbox
number_spinbox = ttk.Spinbox(window, from_=0, to=100, increment=0.1, font='Calibri 14')
number_spinbox.pack(pady=5)
number_spinbox.bind("<<Increment>>", lambda e: update_numeric_label())
number_spinbox.bind("<<Decrement>>", lambda e: update_numeric_label())
number_spinbox.bind("<KeyRelease>", lambda e: update_numeric_label())

label_numeric = ttk.Label(window, text='Value: 0')
label_numeric.pack()

# Subject Spinbox
subjects = ['Maths', 'English', 'Science', 'Computing', 'Latin', 'Arabic', 'Social Studies', 'Sports Science']
subject_spinbox = ttk.Spinbox(window, values=subjects, font='Calibri 14')
subject_spinbox.pack(pady=5)
subject_spinbox.bind("<<Increment>>", lambda e: update_subject_label())
subject_spinbox.bind("<<Decrement>>", lambda e: update_subject_label())
subject_spinbox.bind("<KeyRelease>", lambda e: update_subject_label())

label_subject = ttk.Label(window, text=f'Subject: {subjects[0]}')
label_subject.pack()

window.mainloop()

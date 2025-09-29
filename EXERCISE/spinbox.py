import tkinter as tk
from tkinter import ttk


def get_grade():
    percent_input = percent_int.get()
    grade_output = percent_input * 2  # dummy calculation
    
    fname = fname_string.get()
    lname = lname_string.get()
    gender = gender_string.get()
    
    output_string.set(f"{fname} {lname} ({gender}) -> Grade: {grade_output}")


# window
window = tk.Tk()
window.title('Grading System')
window.geometry('350x250')

# title
title_label = ttk.Label(master=window, text='What is your Grade?', font='Calibri 16 bold')
title_label.pack()

# frames
fname_frame = ttk.Frame(master=window)
lname_frame = ttk.Frame(master=window)
gender_frame = ttk.Frame(master=window)
percent_frame = ttk.Frame(master=window)
button_frame = ttk.Frame(master=window)

# Labels
fname_label = ttk.Label(master=fname_frame, text='First Name:', font='Calibri 12 bold')
fname_label.pack(side='left', padx=5)

lname_label = ttk.Label(master=lname_frame, text='Last Name:', font='Calibri 12 bold')
lname_label.pack(side='left', padx=5)

gender_label = ttk.Label(master=gender_frame, text='Gender:', font='Calibri 12 bold')
gender_label.pack(side='left', padx=5)

percent_label = ttk.Label(master=percent_frame, text='Mark(%):', font='Calibri 12 bold')
percent_label.pack(side='left', padx=5)

# Input boxes
fname_string = tk.StringVar()
entry_fname = ttk.Entry(master=fname_frame, textvariable=fname_string)
entry_fname.pack(side='right', padx=5)

lname_string = tk.StringVar()
entry_lname = ttk.Entry(master=lname_frame, textvariable=lname_string)
entry_lname.pack(side='right', padx=5)

# Gender input (Radio buttons)
gender_string = tk.StringVar(value="Not specified")
radio_male = ttk.Radiobutton(master=gender_frame, text="Male", value="Male", variable=gender_string)
radio_female = ttk.Radiobutton(master=gender_frame, text="Female", value="Female", variable=gender_string)
radio_male.pack(side='left', padx=5)
radio_female.pack(side='left', padx=5)

# Spinbox for percent input
percent_int = tk.IntVar(value=0)
spinbox_percent = tk.Spinbox(master=percent_frame, from_=0, to=100, textvariable=percent_int, width=5)
spinbox_percent.pack(side='right', padx=5)

# button – When pressed runs the function that calculates the Grade
button = ttk.Button(master=button_frame, text='Submit', command=get_grade)
button.pack(side='right')

# Pack frames
fname_frame.pack(pady=5)
lname_frame.pack(pady=5)
gender_frame.pack(pady=5)
percent_frame.pack(pady=5)
button_frame.pack(pady=5)

# output
output_string = tk.StringVar() 
output_label = ttk.Label(master=window, text='Output', font='Calibri 14', textvariable=output_string)
output_label.pack()

# run app
window.mainloop()

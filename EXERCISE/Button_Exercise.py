import tkinter as tk
from tkinter import ttk
# Create window
window = tk.Tk()
window.title('Tkinter Text Entry Widget')
window.geometry('400x400')
# Entry widget with customizations
string_var = tk.StringVar()
Text_entry = ttk.Entry(
   master=window,
   textvariable=string_var,
   font='Calibri 24 bold',
   foreground='blue',        # EXERCISE 2: change color
   show='*',                 # EXERCISE 2: mask input like password
   justify='center'          # EXERCISE 2: align center
)
Text_entry.pack()
# Function for EXERCISE 3: add button + display edited text
def submit_text():
   user_input = string_var.get()
   edited_text = user_input + "_Edited"
   output_string.set(edited_text)
# Output label
output_string = tk.StringVar()
output_label = ttk.Label(master=window, textvariable=output_string)
output_label.pack()
# Button to submit input
submit_button = ttk.Button(master=window, text="Submit", command=submit_text)
submit_button.pack()
# Run
window.mainloop()
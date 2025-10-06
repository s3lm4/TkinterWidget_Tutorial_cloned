++import tkinter as tk

# Create the Tkinter window
window = tk.Tk()
window.title('Tkinter Text Entry Widget')
window.geometry('400x400')

# Create the StringVar for the entry widget
string_var = tk.StringVar()

# Create the Entry widget with text color, password masking, and center alignment
Text_entry = tk.Entry(window, textvariable=string_var, font='Calibri 24 bold', fg='blue', show='*', justify='center')
Text_entry.pack(pady=20)

# Function to submit input and display it with "_Edited"
def submit_input():
    user_input = string_var.get() + "_Edited"
    label.config(text=user_input)

# Create a Button to submit the input
submit_button = tk.Button(window, text="Submit", command=submit_input)
submit_button.pack(pady=10)

# Create a Label to display the edited text
label = tk.Label(window, font='Calibri 18 bold')
label.pack()

# Run the Tkinter event loop
window.mainloop()


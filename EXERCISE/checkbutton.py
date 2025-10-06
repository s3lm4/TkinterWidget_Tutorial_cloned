import tkinter as tk
from tkinter import ttk

# Create main window
window = tk.Tk()
window.title('Tkinter Checkbutton Widget')
window.geometry('400x400')

# Variable to track checkbutton state
bool_var = tk.BooleanVar()

# Function to update label based on checkbutton state
def update_label():
    if bool_var.get():
        label.config(text='I am very HAPPY for you!')
    else:
        label.config(text='I am sorry, BETTER days are ahead!')

# Checkbutton with command to call update_label when toggled
checkbutton = ttk.Checkbutton(window, text='Are you okay?', variable=bool_var,
                              onvalue=True, offvalue=False, command=update_label)
checkbutton.pack(pady=20)

# Label initialized with offvalue message
label = ttk.Label(window, text='I am sorry, BETTER days are ahead!')
label.pack()

# Run the application
window.mainloop()

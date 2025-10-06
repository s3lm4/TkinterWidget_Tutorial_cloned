import tkinter as tk
from tkinter import ttk

# Create the Tkinter window
window = tk.Tk()
window.title('Tkinter Radiobutton Widget')
window.geometry('400x400')

# Frame for Radiobuttons
radiobutton_frame = tk.Frame(window)

# Variable to hold the selected Radiobutton value
int_var = tk.IntVar()

# Function to confirm which button has been pressed and update the label
def confirm_selection():
    selected_value = int_var.get()
    if selected_value == 1:
        output_label.config(text='You selected: This is One')
    elif selected_value == 2:
        output_label.config(text='You selected: This is Two')
    else:
        output_label.config(text='No selection made')

# Create Radiobuttons with a command to call confirm_selection on selection
Int_radiobutton_1 = ttk.Radiobutton(
    radiobutton_frame, 
    value=1, 
    variable=int_var, 
    text='This is One', 
    command=confirm_selection
)
Int_radiobutton_2 = ttk.Radiobutton(
    radiobutton_frame, 
    value=2, 
    variable=int_var, 
    text='This is Two', 
    command=confirm_selection
)

# Label to display output
output_label = ttk.Label(
    master=window,
    text='This is my Label',
    font=('Helvetica', 20, 'bold'),
    foreground='blue',
    justify='center'
)

# Pack elements
radiobutton_frame.pack(pady=10)
Int_radiobutton_1.pack(anchor='w')
Int_radiobutton_2.pack(anchor='w')
output_label.pack(pady=20)

# Run the main window loop
window.mainloop()

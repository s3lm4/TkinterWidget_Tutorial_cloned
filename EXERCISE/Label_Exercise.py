# Ike Testing
import tkinter as tk
from tkinter import ttk

# This function will update the label text by appending "_Edited"
def set_label():
    current_text = output_label.cget("text")  # Get current text
    output_label.config(text=current_text + "_Edited")  # Append "_Edited" and update label

# Create Tkinter Window
window = tk.Tk()
window.title('Tkinter Label Widget')
window.geometry('400x400')

output_label = ttk.Label(
    master=window,
    text='This is my Label',
    font=('Helvetica', 20, 'bold'),   # Font and size
    foreground='blue',                 # Text color
    justify='center'                   # Center align
)
output_label.pack(pady=20)

# Create a Button to trigger the set_label function
edit_button = ttk.Button(master=window, text="Edit Label", command=set_label)
edit_button.pack(pady=10)

# Run the program to generate window with all packed elements for user interaction
window.mainloop()

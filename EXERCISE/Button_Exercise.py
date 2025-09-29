import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title('Tkinter Text Entry Widget')
window.geometry('400x300')

# Output label
output_string = tk.StringVar()
output_label = ttk.Label(window, textvariable=output_string)
output_label.pack(pady=10)

# Function to confirm which button is pressed
def button1_pressed():
    output_string.set("Option 1 pressed!")

def button2_pressed():
    output_string.set("Option 2 pressed!")

# LabelFrame with two buttons
choice_frame = ttk.LabelFrame(window, text="My Choice")
choice_frame.pack(pady=20, padx=20, fill="x")

button1 = ttk.Button(choice_frame, text="Option 1", command=button1_pressed)
button1.pack(side="left", padx=10, pady=10)

button2 = ttk.Button(choice_frame, text="Option 2", command=button2_pressed)
button2.pack(side="left", padx=10, pady=10)

# Run
window.mainloop()

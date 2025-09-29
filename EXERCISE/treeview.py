import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Tkinter Treeview")

treeview = ttk.Treeview(columns=("Salary","Bonus"))

treeview.heading("#0", text="Employee")
treeview.heading("Salary", text="Salary")
treeview.heading("Bonus", text="Bonus")

level1 = treeview.insert('', tk.END, text="San Jose")


treeview.insert(level1, tk.END, text="John Doe", values=(f"${100000: ,}",f"${8000: ,}"))
treeview.insert(level1, tk.END, text="Jane Doe", values=(f"${120000: ,}",f"${9000: ,}"))

treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
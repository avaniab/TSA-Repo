import tkinter as tk
from tkinter import messagebox

def on_button_click():
    name = name_entry.get().strip()
    if not name:
        messagebox.showinfo("Hello!", "Please enter your name first 🙂")
    else:
        messagebox.showinfo("Hello!", f"Nice to meet you, {name}!")
root = tk.Tk()
root.title("Basic Python GUI")
root.geometry("600x300")  # w vs h in pixles

label = tk.Label(root, text="Enter your name:") #label
label.pack(pady=(10, 5))  # top/bottom padding


name_entry = tk.Entry(root)# Create and place a text entry box
name_entry.pack(pady=5)


greet_button = tk.Button(root, text="Greet me", command=on_button_click) # Create and place a button
greet_button.pack(pady=5)


quit_button = tk.Button(root, text="Quit", command=root.destroy)# a quit button
quit_button.pack(pady=5)


root.mainloop()

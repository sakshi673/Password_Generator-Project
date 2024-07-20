import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    length = length_entry.get()
    try:
        length = int(length)
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length")
        return
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    generated_password = ''.join(random.choice(all_characters) for i in range(length))
    
    password_var.set(generated_password)
window = tk.Tk()
window.title("Password Generator")
tk.Label(window, text="Password Length:").pack(pady=10)
length_entry = tk.Entry(window, width=30)
length_entry.pack()
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
password_var = tk.StringVar()
password_label = tk.Label(window, textvariable=password_var, font=("Arial", 12), wraplength=600)
password_label.pack(pady=10)
window.mainloop()
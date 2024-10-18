# Required installations (ensure these are executed in your terminal):
# brew install python-tk@3.9
# pip install pyperclip
# Or download manually:
# curl https://files.pythonhosted.org/packages/a7/2c/4c64579f847bd5d539803c8b909e54ba087a79d01bb3aba433a95879a6c5/pyperclip-1.8.2.tar.gz > pyperclip.tar.gz
# tar -xzvf pyperclip.tar.gz
# cd pyperclip-1.8.2
# python3 setup.py install

# Pyperclip is a cross-platform Python module for clipboard functions.

import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# Create the main window
gui = Tk()
gui.title('Password Generator')
gui.geometry('300x250')
gui.resizable(0, 0)

def process():
    """Generate a random password based on user-defined length."""
    try:
        length = int(string_pass.get())
        if length < 4:
            raise ValueError("Password length must be at least 4 characters.")
        
        # Character sets
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = '0123456789'
        special = '@#$%&*'
        
        # Combine all characters
        all_characters = lower + upper + num + special
        
        # Generate password
        password = ''.join(random.sample(all_characters, length))
        
        # Display the generated password
        messagebox.showinfo('Generated Password', 
                            f'Your password: {password}\n\nPassword copied to clipboard.')
        pyperclip.copy(password)  # Copy to clipboard
    except ValueError as ve:
        messagebox.showerror('Input Error', str(ve))

# GUI Components
label = Label(gui, text="Password Length", font=("Helvetica", 12))
label.pack(pady=10)

string_pass = StringVar()
txt = Entry(gui, textvariable=string_pass, width=5, font=("Helvetica", 12))
txt.pack(pady=5)

btn = Button(gui, text="Generate Password", command=process, font=("Helvetica", 12))
btn.pack(pady=20)

# Run the GUI main loop
gui.mainloop()

import tkinter as tk
from tkinter import messagebox
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random


def generate_password():
    try:
        num_capitals = int(capital_entry.get())
        num_lowers = int(lower_entry.get())
        num_numbers = int(number_entry.get())
        num_specials = int(special_entry.get())
    except ValueError:
        messagebox.showinfo("Input error", "Invalid input!")
        # result_label.config(text="Invalid input")
        return

    password = ''
    for _ in range(num_capitals):
        password += random.choice(ascii_uppercase)

    for _ in range(num_lowers):
        password += random.choice(ascii_lowercase)

    for _ in range(num_numbers):
        password += random.choice(digits)

    for _ in range(num_specials):
        password += random.choice(punctuation)

    # fill the rest with random characters
    while len(password) < 8:  # minimum length is 8
        password += random.choice(ascii_uppercase + ascii_lowercase + digits + punctuation)

    # shuffle the password to avoid the first characters being always the same
    password = list(password)
    random.shuffle(password)

    # result_label.config(text=''.join(password))
    result_entry.delete(0, tk.END)  # clear existing text in the entry field
    result_entry['fg'] = 'black'  # Set to black color
    result_entry.insert(0, ''.join(password))  # insert the generated password


    # description_label modifier
    total_chars_msg = ("Your new " + str(int(num_capitals) + int(num_lowers) + int(num_numbers) + int(num_specials)) + " characters length password is:")
    description_label.configure(text=total_chars_msg)

def copy_password():
    try:
        root.clipboard_clear()  # clear the clipboard
        root.clipboard_append(result_entry.get())  # append the password to the clipboard
        result_entry['fg'] = 'blue'
    except AttributeError:  # if this is run before the GUI has been fully initialized
        pass

def copy():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    result_entry['fg'] = 'blue'  # Change to blue color

def cut():
    copy()
    result_entry.delete(0, tk.END)

def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)


root = tk.Tk()
root.iconbitmap('./pwdgen.ico') # Application icon
root.title("Password Generator")
screen_width = root.winfo_screenwidth() # Screen width resolution
screen_height = root.winfo_screenheight() # Screen height resolution
window_min_x = 280 # Window minimum width
window_min_y = 330 # Window minimum height
window_max_x = 350 # Window maximum width
window_max_y = 400 # Window maximum height
screen_string = str(window_min_x) + 'x' + str(window_min_y) + '+' + str(int((screen_width - window_min_x)/2)) + '+' + str(int((screen_height - window_min_y)/4))
root.geometry(screen_string)
root.minsize(window_min_x, window_min_y)
root.maxsize(window_max_x, window_max_y)

message_label = tk.Label(root, text="Change the number of each kind of\n characters you want, or accept default values")
message_label.pack()

capital_label = tk.Label(root, text="Number of capital letters:")
capital_label.pack()
capital_entry = tk.Entry(root)
capital_entry.insert(0, "2")
capital_entry.pack()

lower_label = tk.Label(root, text="Number of lowercase letters:")
lower_label.pack()
lower_entry = tk.Entry(root)
lower_entry.insert(0, "3")
lower_entry.pack()

number_label = tk.Label(root, text="Number of numbers:")
number_label.pack()
number_entry = tk.Entry(root)
number_entry.insert(0, "2")
number_entry.pack()

special_label = tk.Label(root, text="Number of special characters:")
special_label.pack()
special_entry = tk.Entry(root)
special_entry.insert(0, "1")
special_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=5)

description_label = tk.Label(root, text="Press the button to generate a password")
description_label.pack()

result_entry = tk.Entry(root, width=40)  # field to display the generated password
result_entry.pack(pady=5)

copy_button = tk.Button(root, text="Copy password", command=copy_password)
copy_button.pack()

popup_menu = tk.Menu(root, tearoff=0)  # Create a right-click menu
popup_menu.add_command(label="Cut", command=cut)
popup_menu.add_command(label="Copy", command=copy)
result_entry.bind("<Button-3>", show_popup_menu)  # Bind the right-click event to show the popup menu

root.mainloop()

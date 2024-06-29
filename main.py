from random import choice, randint, shuffle
import pyperclip
from tkinter import messagebox  # Import messagebox to show alert dialogs
from customtkinter import *
import os

set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379777"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                              f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            os.system("data.txt")  # Open the file with the saved passwords


        # ---------------------------- UI SETUP ------------------------------- #
window = CTk()

window.title("Password Manager")
window.configure(padx=40, pady=40)

# Canvas for the logo
app_name = CTkLabel(window, text="🔒", font=(FONT_NAME, 150), text_color=RED)
app_name.grid(row=0, column=0, pady=15, columnspan=3)

# Labels
website_label = CTkLabel(window, text="Website:", font=(FONT_NAME, 14))
website_label.grid(column=0, row=1, pady=5)

email_label = CTkLabel(window, text="Email/Username:", font=(FONT_NAME, 14))
email_label.grid(column=0, row=2, pady=5)

password_label = CTkLabel(window, text="Password:", font=(FONT_NAME, 14))
password_label.grid(column=0, row=3, pady=5)

# Entries
website_entry = CTkEntry(window, width=270, font=(FONT_NAME, 14))
website_entry.grid(column=1, row=1, columnspan=2, pady=5)
website_entry.focus()  # Set focus to the website entry field

email_entry = CTkEntry(window, width=270, font=(FONT_NAME, 14))
email_entry.grid(column=1, row=2, columnspan=2, pady=5)
email_entry.insert(0, "sergey.tserkonyuk@gmail.com")  # Pre-fill the email entry field

password_entry = CTkEntry(window, width=150, font=(FONT_NAME, 14))
password_entry.grid(column=1, row=3, pady=5, padx=5)

# Buttons
generate_password_button = CTkButton(window, text="Generate Password", command=generate_password,font=(FONT_NAME, 14))
generate_password_button.grid(column=2, row=3, pady=5, padx=5, sticky="W")

add_button = CTkButton(window, text="Add", width=250, command=save_password, fg_color=GREEN, font=(FONT_NAME, 16))
add_button.grid(column=0, row=4, columnspan=3, pady=25, padx=20)

window.mainloop()

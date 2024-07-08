from random import choice, randint, shuffle
import pyperclip
from tkinter import messagebox  # Import messagebox to show alert dialogs
from customtkinter import *
import os
import json

set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
PINK = "#e2979c"
NAVY = "#8c95c5"
GREEN = "#379777"
YELLOW = "#f2d0b9"
BROWN = "#7f5539"
BLACK = "#000000"
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

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        if website in data:
            overwrite = messagebox.askyesno(title="Warning", message=f"You already have a password for {website}. Do you want to change it?")
            if overwrite:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                messagebox.showinfo(title="Password saved", message="Your password has been saved!🔒")
            else:
                return
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            messagebox.showinfo(title="Password saved", message="Your password has been saved!🔒")

        website_entry.delete(0, END)
        password_entry.delete(0, END)

        # ---------------------------- UI SETUP ------------------------------- #


def open_list():
    if os.path.exists('data.json'):
        os.system('data.json')
    else:
        messagebox.showwarning(title="Error", message="No Data File Found")

def search_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showwarning(title=website, message=f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showwarning(title="Error", message=f"No details for the {website} exists")


window = CTk()

window.title("Password Manager")
window.configure(padx=40, pady=40)

# Canvas for the logo
app_name = CTkLabel(window, text="🔒", font=(FONT_NAME, 150), text_color=NAVY)
app_name.grid(row=0, column=0, pady=15, columnspan=3)

# Labels
website_label = CTkLabel(window, text="Website:", font=(FONT_NAME, 14))
website_label.grid(column=0, row=1, padx=(0, 10), pady=5)

email_label = CTkLabel(window, text="Email/Username:", font=(FONT_NAME, 14))
email_label.grid(column=0, row=2, padx=(0, 10), pady=5)

password_label = CTkLabel(window, text="Password:", font=(FONT_NAME, 14))
password_label.grid(column=0, row=3, padx=(0, 10), pady=5)

# Entries
website_entry = CTkEntry(window, 200, font=(FONT_NAME, 14))
website_entry.grid(column=1, row=1, pady=5)
website_entry.focus()  # Set focus to the website entry field

email_entry = CTkEntry(window, width=350, font=(FONT_NAME, 14))
email_entry.grid(column=1, row=2, columnspan=2, pady=5)
email_entry.insert(0, "sergey.tserkonyuk@gmail.com")  # Pre-fill the email entry field

password_entry = CTkEntry(window, width=200, font=(FONT_NAME, 14))
password_entry.grid(column=1, row=3, pady=5)

# Buttons
generate_password_button = CTkButton(window, text="Generate Password", width=100, command=generate_password,
                                     font=(FONT_NAME, 14))
generate_password_button.grid(column=2, row=3, pady=5, padx=(10, 0), sticky="W")

add_button = CTkButton(window, text="Add", width=300, command=save_password, fg_color=GREEN, font=(FONT_NAME, 16))
add_button.grid(column=1, row=4, columnspan=3, pady=5, padx=(10, 0))

search_button = CTkButton(window, text="Search", width=100, command=search_password, font=(FONT_NAME, 14),
                          fg_color=YELLOW, text_color=BROWN, hover_color=NAVY)
search_button.grid(column=2, row=1, pady=5, padx=(10, 0))

open_list_button = CTkButton(window, text="Open List", width=100, command=open_list, font=(FONT_NAME, 14),
                             fg_color=NAVY, text_color=BLACK, hover_color=GREEN)
open_list_button.grid(column=0, row=4, pady=5, padx=(10, 0))

window.mainloop()

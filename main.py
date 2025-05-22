from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ------------------------------ PASSWORD GENERATOR ------------------------------ #
def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE FUNCTION ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave anything empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- SEARCH FUNCTION ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title = f"{website}", message= (f"Email: {data[website]["email"]} \n" f"Password: {data[website]["password"]}"))
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# --- Logo ---
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# --- Labels ---
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e", pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e", pady=5)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e", pady=5)

# --- Entry Fields ---
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, pady=5, sticky="w")
website_entry.focus()

search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(row=1, column=2, padx=5)

email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")
email_entry.insert(0, "@example.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, pady=5, sticky="w")

generate_password_button = Button(text="Generate Password", command=generate_password, width=14)
generate_password_button.grid(row=3, column=2, padx=5)

# --- Add Button ---
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()

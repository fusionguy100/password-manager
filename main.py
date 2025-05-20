from tkinter import *

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# --- Logo ---
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)  # No border
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# --- Labels ---
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e", pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e", pady=5)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e", pady=5)

# --- Entry fields ---
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=5)

# --- Buttons ---
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()

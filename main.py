from tkinter import *
from tkinter import messagebox

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
email_entry.insert(0, "@example.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=5)



# --- Buttons ---
def save():
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showerror(title = "Error", message= "Please don't leave anything empty!")
        else:
            is_ok =  messagebox.askokcancel(title = website, message = f"These are the details entered: \n Email: {email}" f"\n Password: {password}\n Is it okay to save?")

            if is_ok:
                with open("data_file.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                    website_entry.delete(0,"end")
                    password_entry.delete(0,"end")


generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, pady=5)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)





window.mainloop()

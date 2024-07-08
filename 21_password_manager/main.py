from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

LOGO_PATH = "21_password_manager/logo.png"
SAVE_PATH = "21_password_manager/data.json"
SAVE_PROMPT = """These are the fields entered:
- Email/Username: {}
- Password: {}

Are you ok with this selection?
"""


def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = []

    password_list.extend([choice(letters) for _ in range(randint(8, 10))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if website == "" or email == "" or password == "":
        prompt = "Please, don't leave any fields empty."
        messagebox.showinfo(title="Oops", message=prompt)
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=SAVE_PROMPT.format(email, password)
        )
        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }

            try:
                file = open(SAVE_PATH)
            except FileNotFoundError:
                data = {}
            else:
                data = json.load(file)
                file.close()
            finally:
                data.update(new_data)

            with open(SAVE_PATH, mode="w") as file:
                json.dump(data, file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

            pyperclip.copy(password)
            messagebox.showinfo(
                title="Success",
                message="Password copied to clipboard"
            )


def search_website():
    website = website_entry.get().strip()
    if website != "":
        try:
            result = {}
            with open(SAVE_PATH) as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(
                title="Oops!",
                message="You haven't created any password yet"
            )
        else:
            if website in data:
                result = data[website]
                email = result["email"]
                password = result["password"]
                prompt = f"Email: {email}\nPassword: {password}"
                messagebox.showinfo(title=website, message=prompt)
            else:
                prompt = f"No password for {website} created yet."
                messagebox.showinfo(
                    title="No password",
                    message=prompt
                )
    else:
        messagebox.showinfo(
            title="Oops!",
            message="There's nothing to search"
        )


window = Tk()
window.title("Password Manager")
window.config(padx=45, pady=45)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=LOGO_PATH)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.config(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", command=search_website)
search_button.config(width=14)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_entry = Entry()
email_entry.config(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@email.com")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.config(width=38)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

from tkinter import Tk, Label, Entry, Button, END


def calculate():
    try:
        miles_value = float(miles.get())
        km["text"] = round(miles_value * 1.609, 2)
    except ValueError:
        pass


window = Tk()
window.title("Miles to Km converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)

miles = Entry(width=7)
miles.insert(END, string="0")
miles.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

label = Label(text="Is equal to ")
label.grid(column=0, row=1)

km = Label(text="0")
km.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()

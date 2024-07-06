from tkinter import Tk, Canvas, PhotoImage, Label, Button
# --------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
MAIN_FONT = (FONT_NAME, 25, "bold")
SECOND_FONT = (FONT_NAME, 12, "bold")
BUTTON_FONT = ("arial", 12, "bold")
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
IMAGE_LOC = "20_pomodoro_app/tomato.png"
CHECKMARK = "🗹"
reps = 0
timer = None

# --------------------------- TIMER RESET ----------------------------- #


def reset_timer():
    global timer
    global reps
    if timer is not None:
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text="00:00")
        headline.config(text="Timer", fg=GREEN)
        reps = 0
        repetitions.config(text="")
        timer = None


# ------------------------- TIMER MECHANISM --------------------------- #


def start_timer(from_button: bool = True):
    global reps

    if timer is None or not from_button:
        window.lift()
        reps += 1

        working_secs = WORK_MIN * 60
        short_break_secs = SHORT_BREAK_MIN * 60
        long_break_secs = LONG_BREAK_MIN * 60
        countdown_secs = working_secs

        if reps % 8 == 0:
            countdown_secs = long_break_secs
            headline.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            countdown_secs = short_break_secs
            headline.config(text="Break", fg=PINK)
        else:
            headline.config(text="Work", fg=GREEN)

        countdown(countdown_secs)


# ---------------------- COUNTDOWN MECHANISM -------------------------- #


def countdown(count):
    global timer
    count_min = str(count // 60).zfill(2)
    count_sec = str(count % 60).zfill(2)
    count_text = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        timer = window.after(100, countdown, count-1)
    else:
        start_timer(from_button=False)
        if reps % 2 == 0:
            reps_text = CHECKMARK * int(reps // 2)
            repetitions.config(text=reps_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro App")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file=IMAGE_LOC)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=MAIN_FONT
)
canvas.grid(column=1, row=1)

headline = Label(text="Timer", font=MAIN_FONT, fg=GREEN, bg=YELLOW)
headline.grid(column=1, row=0)

start_button = Button(
    text="Start",
    font=BUTTON_FONT,
    highlightthickness=0,
    command=start_timer
)
start_button.grid(column=0, row=2)

reset_button = Button(
    text="Reset",
    font=BUTTON_FONT,
    highlightthickness=0,
    command=reset_timer
)
reset_button.grid(column=2, row=2)

repetitions = Label(font=SECOND_FONT, fg=GREEN, bg=YELLOW)
repetitions.grid(column=1, row=3)

window.mainloop()

from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
FRONT_PATH = "22_flash_cards/images/card_front.png"
BACK_PATH = "22_flash_cards/images/card_back.png"
WRONG_PATH = "22_flash_cards/images/wrong.png"
RIGHT_PATH = "22_flash_cards/images/right.png"
LANG_FONT = ("arial", 40, "italic")
WORD_FONT = ("arial", 60, "bold")
DATA_PATH = "22_flash_cards/data/french_words.csv"
LEARN_PATH = "22_flash_cards/data/words_to_learn.csv"
LANG_DATA = (
    pandas.read_csv(DATA_PATH) if not os.path.exists(LEARN_PATH)
    else pandas.read_csv(LEARN_PATH)
)
data_json = LANG_DATA.to_dict('records')
current_data = {}
flip = None


def flip_card():
    card.itemconfig(card_side, image=back_image)
    secondary_lang = list(current_data.keys())[1]
    new_word = current_data[secondary_lang]
    card.itemconfig(lang_text, text=secondary_lang, fill="white")
    card.itemconfig(word_text, text=new_word, fill="white")
    window.after_cancel(flip)


def change_card():
    global current_data
    global flip
    if flip is not None:
        window.after_cancel(flip)
    card.itemconfig(card_side, image=front_image)
    current_data = random.choice(data_json)
    primary_lang = list(current_data.keys())[0]
    new_word = current_data[primary_lang]
    card.itemconfig(lang_text, text=primary_lang, fill="black")
    card.itemconfig(word_text, text=new_word, fill="black")
    flip = window.after(3000, flip_card)


def correct_answer():
    data_json.remove(current_data)
    data_frame = pandas.DataFrame.from_dict(data_json)
    data_frame.to_csv(LEARN_PATH, index=False)
    change_card()


window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526)
card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(column=0, row=0, columnspan=2)

front_image = PhotoImage(file=FRONT_PATH)
back_image = PhotoImage(file=BACK_PATH)
card_side = card.create_image(400, 263, image=front_image)

lang_text = card.create_text(400, 150, text="", font=LANG_FONT)
word_text = card.create_text(400, 263, text="", font=WORD_FONT)

wrong_image = PhotoImage(file=WRONG_PATH)
wrong_button = Button(image=wrong_image, command=change_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file=RIGHT_PATH)
right_button = Button(image=right_image, command=correct_answer)
right_button.grid(column=1, row=1)

change_card()

window.mainloop()

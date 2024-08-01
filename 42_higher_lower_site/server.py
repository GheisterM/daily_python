from flask import Flask
import random

rand_num = random.randint(0, 9)
app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:number>")
def guess(number: int):
    global rand_num
    text = "You found me!"
    text_color = "green"
    display_img = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
    additional = ""

    if number > rand_num:
        text = "Too high! Try again."
        text_color = "red"
        display_img = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    elif number < rand_num:
        text = "Too low! Try again."
        text_color = "blue"
        display_img = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    else:
        rand_num = random.randint(0, 9)
        additional = "<h1>Now, guess again a number between 0 and 9</h1>"

    return f'<h1 style="color: {text_color}">{text}</h1>' \
           f'<img src="{display_img}">{additional}'


if __name__ == "__main__":
    app.run(debug=True)

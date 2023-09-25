from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


# ---------------------------------------RANDOM WORDS---------------------------------#
def new_flash_words():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    random_french_words = current_card["French"]

    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{random_french_words}", fill="black")
    canvas.itemconfig(front_canvas, image=front_image)
    flip_timer = window.after(3000, flip_colour)


# ----------------------------------------KNOWN WORDS-----------------------------------#

def is_known():
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_flash_words()


# ----------------------------------------FLIP COLOUR-----------------------------------#
def flip_colour():
    eng_words = current_card["English"]
    canvas.itemconfig(front_canvas, image=back_image)
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=eng_words)
    canvas.itemconfig(front_canvas, image=back_image, padx=50, pady=5)


# ---------------------------------------UI SETUP------------------------------------#

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flasky")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")

front_canvas = canvas.create_image(400, 263, image=front_image)

back_image = PhotoImage(file="./images/card_back.png")

title_text = canvas.create_text(400, 125, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
flip_timer = window.after(3000, flip_colour)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_flash_words)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

new_flash_words()

window.mainloop()

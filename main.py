from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


# ---------------------------------------RANDOM WORDS---------------------------------#
def new_flash_words():
    random_dict = random.choice(to_learn)
    random_words = random_dict["French"]
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=f"{random_words}")


# ---------------------------------------UI SETUP------------------------------------#

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flasky")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

# back_image = PhotoImage(file="./images/card_back.png")
# canvas.create_image(400, 250, image=back_image)
# canvas.grid()

front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 125, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_flash_words)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=new_flash_words)
right_button.grid(row=1, column=1)

new_flash_words()

window.mainloop()

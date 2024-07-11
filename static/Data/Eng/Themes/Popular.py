import tkinter as tk
import random
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# Предложения на английском и русском
sentences = [
    ("Мне нравится смотреть фильмы.", "I like to watch movies."),
    ("Она говорит на трех языках.", "She speaks three languages."),
    ("Он талантливый музыкант.", "He is a talented musician."),
    ("Хочешь пойти на прогулку?", "Do you want to go for a walk?"),
    ("Мой любимый цвет - синий.", "My favorite color is blue."),
    ("Вчера мы поехали на пляж.", "We went to the beach yesterday."),
    ("Она отличная танцовщица.", "She is a great dancer."),
    ("У меня есть домашний кот.", "I have a pet cat."),
    ("Они живут в красивом доме.", "They live in a beautiful house."),
    ("Он очень хорошо играет на гитаре.", "He plays the guitar very well."),
    ("Я изучаю компьютерные науки.", "I'm studying computer science."),
    ("Ей нравится читать книги.", "She enjoys reading books."),
    ("У тебя есть братья или сестры?", "Do you have any siblings?"),
    ("Он работает инженером-программистом.", "He works as a software engineer."),
    ("Мои родители приезжают в гости.", "My parents are coming to visit."),
    ("Ей нравится играть в теннис.", "She likes to play tennis."),
    ("Я хочу научиться готовить.", "I want to learn how to cook."),
    ("Нам нужно купить продукты.", "We need to buy some groceries."),
    ("Он всегда приходит вовремя.", "He is always on time."),
    ("Она хороший друг.", "She is a good friend."),
    ("У тебя есть планы на выходные?", "Do you have any plans for the weekend?"),
    ("Я собираюсь навестить своих бабушку и дедушку.", "I'm going to visit my grandparents."),
    ("Она хочет стать врачом.", "She wants to become a doctor."),
    ("Мне нужно купить новый телефон.", "I need to buy a new phone."),
    ("Мы собираемся в путешествие на следующей неделе.", "We are going on a trip next week."),
    ("Он талантливый художник.", "He is a talented artist."),
    ("У нее красивый голос.", "She has a beautiful voice."),
    ("Тебе нравится ходить в походы?", "Do you like to go hiking?"),
    ("Я взволнована концертом сегодня вечером.", "I'm excited about the concert tonight."),
    ("Ей нравится играть в видеоигры.", "She enjoys playing video games."),
    ("У меня встреча в 15:00.", "I have a meeting at 3 PM."),
]

# Создание главного окна
root = tk.Tk()
root.title("Accelingvo")
root.state('zoomed')
root.geometry("1920x1080")
root.iconbitmap('Data/py.ico')

# Создание стиля для текста и кнопки
style = ttk.Style()
style.configure('English.TLabel', font=("Times New Roman", 24), foreground="#183b66", padding=8, background="#8fc6da")
style.configure('Russian.TLabel', font=("Times New Roman", 24), foreground="#183b66", padding=8, background="#8fc6da")
style.configure('Next.TButton', font=("Times New Roman", 32, "bold"), foreground="#183b66", padding=12, background="#8fc6da")
# Функция для показа случайных предложений
def show_random_sentences():
    random.shuffle(sentences)
    english_text.set("Russian:\n{}\n{}\n{}\n{}\n{}".format(
        sentences[0][0], sentences[1][0], sentences[2][0], sentences[3][0], sentences[4][0]))
    russian_text.set("English:\n{}\n{}\n{}\n{}\n{}".format(
        sentences[0][1], sentences[1][1], sentences[2][1], sentences[3][1], sentences[4][1]))

def close_window():
    root.destroy()
    os.system("python Data/Eng/themes.py")

# Создание текстовых меток
english_text = tk.StringVar()
russian_text = tk.StringVar()

image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)
back_button = ttk.Button(root, text="←", style="Next.TButton", command=close_window)
back_button.pack(side=BOTTOM, pady= 40)
next_button = ttk.Button(root, text="Next", command=show_random_sentences, style='Next.TButton')
next_button.pack(side=BOTTOM)
english_label = ttk.Label(root, textvariable=english_text, style='English.TLabel', justify=tk.LEFT)
english_label.pack(side=LEFT, fill=X, expand=True)
russian_label = ttk.Label(root, textvariable=russian_text, style='Russian.TLabel', justify=tk.LEFT)
russian_label.pack(side=RIGHT, fill=X, expand=True)
back_button.pack()
show_random_sentences()
root.mainloop()
import tkinter as tk
import random
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# Предложения на английском и русском
sentences = [
    ("I like to watch movies.", "Мне нравится смотреть фильмы."),
    ("She speaks three languages.", "Она говорит на трех языках."),
    ("He is a talented musician.", "Он талантливый музыкант."),
    ("Do you want to go for a walk?", "Хочешь пойти на прогулку?"),
    ("My favorite color is blue.", "Мой любимый цвет - синий."),
    ("We went to the beach yesterday.", "Вчера мы поехали на пляж."),
    ("She is a great dancer.", "Она отличная танцовщица."),
    ("I have a pet cat.", "У меня есть домашний кот."),
    ("They live in a beautiful house.", "Они живут в красивом доме."),
    ("He plays the guitar very well.", "Он очень хорошо играет на гитаре."),
    ("I'm studying computer science.", "Я изучаю компьютерные науки."),
    ("She enjoys reading books.", "Ей нравится читать книги."),
    ("Do you have any siblings?", "У тебя есть братья или сестры?"),
    ("He works as a software engineer.", "Он работает инженером-программистом."),
    ("My parents are coming to visit.", "Мои родители приезжают в гости."),
    ("She likes to play tennis.", "Ей нравится играть в теннис."),
    ("I want to learn how to cook.", "Я хочу научиться готовить."),
    ("We need to buy some groceries.", "Нам нужно купить продукты."),
    ("He is always on time.", "Он всегда приходит вовремя."),
    ("She is a good friend.", "Она хороший друг."),
    ("Do you have any plans for the weekend?", "У тебя есть планы на выходные?"),
    ("I'm going to visit my grandparents.", "Я собираюсь навестить своих бабушку и дедушку."),
    ("She wants to become a doctor.", "Она хочет стать врачом."),
    ("I need to buy a new phone.", "Мне нужно купить новый телефон."),
    ("We are going on a trip next week.", "Мы собираемся в путешествие на следующей неделе."),
    ("He is a talented artist.", "Он талантливый художник."),
    ("She has a beautiful voice.", "У нее красивый голос."),
    ("Do you like to go hiking?", "Тебе нравится ходить в походы?"),
    ("I'm excited about the concert tonight.", "Я взволнована концертом сегодня вечером."),
    ("She enjoys playing video games.", "Ей нравится играть в видеоигры."),
    ("I have a meeting at 3 PM.", "У меня встреча в 15:00."),
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
    english_text.set("Английский:\n{}\n{}\n{}\n{}\n{}".format(
        sentences[0][0], sentences[1][0], sentences[2][0], sentences[3][0], sentences[4][0]))
    russian_text.set("Русский:\n{}\n{}\n{}\n{}\n{}".format(
        sentences[0][1], sentences[1][1], sentences[2][1], sentences[3][1], sentences[4][1]))

def close_window():
    root.destroy()
    os.system("python Data/themes.py")

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
next_button = ttk.Button(root, text="Дальше", command=show_random_sentences, style='Next.TButton')
next_button.pack(side=BOTTOM)
english_label = ttk.Label(root, textvariable=english_text, style='English.TLabel', justify=tk.LEFT)
english_label.pack(side=LEFT, fill=X, expand=True)
russian_label = ttk.Label(root, textvariable=russian_text, style='Russian.TLabel', justify=tk.LEFT)
russian_label.pack(side=RIGHT, fill=X, expand=True)
back_button.pack()
show_random_sentences()
root.mainloop()
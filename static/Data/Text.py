import tkinter as tk
import random
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def close_window():
    window.destroy()
    os.system("python Data/main.py")

sentences = [
    "I love ice cream",  # Пример предложений на английском
    "Today is a beautiful day",
    "Can I help you?",
    "I have a cat",
    "What's your favorite color?",
    "It's raining outside",
    "How old are you?",
    "I like pizza",
    "Where do you live?",
    "Do you speak English?",
    "I am tired",
    "What time is it?",
    "I am hungry",
    "What's your name?",
    "I like to listen to music",
    "I like to play tennis",
    "How was your day?",
    "I'm going to the cinema tonight",
    "I enjoy reading books",
    "Have a nice day!"
]

translations = [
    "Я люблю мороженое",  # Примеры соответствующих переводов на русский
    "Сегодня прекрасный день",
    "Могу я вам помочь?",
    "У меня есть кошка",
    "Какой у вас любимый цвет?",
    "На улице идет дождь",
    "Сколько тебе лет?",
    "Я люблю пиццу",
    "Где вы живете?",
    "Вы говорите по-английски?",
    "Я устал",
    "Который час?",
    "Я голоден",
    "Как вас зовут?",
    "Мне нравится слушать музыку",
    "Мне нравится играть в теннис",
    "Как прошел ваш день?",
    "Сегодня вечером я иду в кино",
    "Мне нравится читать книги",
    "Хорошего дня!"
]

currentSentenceIndex = 0
currentSentence = ""
currentTranslation = ""

window = tk.Tk()
window.state('zoomed')
window.title("Accelingvo")
window.iconbitmap('Data/py.ico')
window.geometry("1920x1080")
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
style = ttk.Style()
style.configure("BW.TLabel", font=("Times New Roman", 32), foreground="#183b66", padding=8, background="#8fc6da")
style.configure("BW.TButton", font=("Times New Roman", 32, "bold"), foreground="#183b66", padding=12, background="#8fc6da")
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)


def showSentence():
    os.system("clear")
    sentence_label.config(text=currentSentence, font=("Roboto", 32))


def checkTranslation():
    translation = translation_entry.get()
    if translation == currentTranslation:
        result_label.config(text="Правильный перевод!", fg="green", font=("Roboto", 32))
    else:
        result_label.config(text="Неправильный перевод!", fg="red", font=("Roboto", 32))
    translation_entry.delete(0, tk.END)
    getNextSentence()


def getNextSentence():
    global currentSentenceIndex, currentSentence, currentTranslation
    currentSentenceIndex += 1
    if currentSentenceIndex >= len(sentences):
        currentSentenceIndex = 0
    currentSentence = sentences[currentSentenceIndex]
    currentTranslation = translations[currentSentenceIndex]
    showSentence()


random.seed()
currentSentenceIndex = random.randint(0, len(sentences) - 1)
currentSentence = sentences[currentSentenceIndex]
currentTranslation = translations[currentSentenceIndex]
sentence_label = ttk.Label(window, text=currentSentence, style="BW.TLabel")
sentence_label.pack(pady=100)
translation_entry = tk.Entry(window, fg="#000", font=("Roboto", 32))
translation_entry.pack()
check_button = ttk.Button(window, text="Проверить", command=checkTranslation, style="BW.TButton")
check_button.pack(pady=50)
result_label = Label(window, text="", font=("Roboto", 32))
result_label.pack()
next_button = ttk.Button(window, text="Следующее предложение", command=getNextSentence, style="BW.TButton")
next_button.pack(pady=50)
back_button = ttk.Button(window, text="←", command=close_window, style="BW.TButton")
back_button.pack(pady=10)
window.mainloop()
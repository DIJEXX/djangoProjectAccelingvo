import tkinter as tk
import random
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# Предложения на английском и русском
sentences = [
    ("I enjoy going to school every day.", "Мне нравится ходить в школу каждый день."),
    ("The school bell rang, signaling the end of class.", "Зазвонил школьный звонок, означая конец урока."),
    ("My favorite subject in school is math.", "Мой любимый предмет в школе — математика."),
    ("We have a field trip to the museum next week.", "На следующей неделе у нас экскурсия в музей."),
    ("The school library is a quiet place for studying.", "Школьная библиотека — тихое место для учебы."),
    ("I have a lot of friends in my school.", "У меня много друзей в школе."),
    ("She is the top student in our school.", "Она самая лучшая ученица в нашей школе."),
    ("The school playground is a fun place to play during recess.",
     "Школьная площадка — забавное место для игр во время перемен."),
    ("The school bus arrives at 7:30 AM every morning.", "Школьный автобус приезжает каждое утро в 7:30."),
    ("I always pack my lunch for school.", "Я всегда беру с собой обед в школу."),
    ("We have a science fair at school next month.", "В следующем месяце у нас будет научная ярмарка в школе."),
    ("The school cafeteria serves delicious food.", "Школьная столовая подает вкусную еду."),
    ("I need to study for my upcoming exams.", "Мне нужно готовиться к предстоящим экзаменам."),
    ("She joined the school choir and sings beautifully.", "Она вступила в школьный хор и поет красиво."),
    ("We have a basketball court in our school.", "У нашей школы есть баскетбольная площадка."),
    ("The school principal is a strict but fair person.", "Директор школы — строгий, но справедливый человек."),
    ("I'm looking forward to the school dance next week.", "С нетерпением жду школьного танца на следующей неделе."),
    ("I have a lot of homework to do after school.", "У меня много домашней работы после школы."),
    ("The school offers a wide range of extracurricular activities.",
     "В школе предлагается широкий спектр внеклассных мероприятий."),
    ("The school assembly was filled with enthusiastic students.",
     "Школьное собрание было наполнено восторженными учениками."),
    ("I'm part of the school debate team.", "Я являюсь частью школьной команды по дебатам."),
    ("The school has a well-equipped computer lab.", "В школе есть хорошо оборудованная компьютерная лаборатория."),
    ("She won the spelling bee competition at school.", "Она выиграла соревнование по правописанию в школе."),
    ("I'm a member of the school student council.", "Я являюсь членом школьного студенческого совета."),
    ("The school yearbook captures memories from the academic year.",
     "Школьный годовой сборник запечатлевает воспоминания за учебный год."),
    ("I have a locker where I keep my books at school.", "У меня есть шкафчик, где я храню свои книги в школе."),
    ("She is the captain of the school soccer team.", "Она капитан школьной футбольной команды."),
    ("The school orchestra is practicing for their upcoming concert.",
     "Школьный оркестр тренируется для предстоящего концерта."),
    ("I'm attending an after-school art club.", "Я посещаю внешкольный художественный кружок."),
    ("The school gymnasium is where we have physical education classes.",
     "Школьный спортзал — место, где мы проводим занятия по физической культуре."),
    ("She got an award for academic excellence at school.", "Она получила награду за успехи в учебе в школе."),
    ("I can't wait for summer break to be free from school.", "Не могу дождаться летних каникул, чтобы освободиться от школы."),
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
import tkinter as tk
import random
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# Предложения на английском и русском
sentences = [
    ("Мне нравится ходить в школу каждый день.", "I enjoy going to school every day."),
    ("Зазвонил школьный звонок, означая конец урока.", "The school bell rang, signaling the end of class."),
    ("Мой любимый предмет в школе — математика.", "My favorite subject in school is math."),
    ("На следующей неделе у нас экскурсия в музей.", "We have a field trip to the museum next week."),
    ("Школьная библиотека — тихое место для учебы.", "The school library is a quiet place for studying."),
    ("У меня много друзей в школе.", "I have a lot of friends in my school."),
    ("Она самая лучшая ученица в нашей школе.", "She is the top student in our school."),
    ("Школьная площадка — забавное место для игр во время перемен.", "The school playground is a fun place to play during recess."),
    ("Школьный автобус приезжает каждое утро в 7:30.", "The school bus arrives at 7:30 AM every morning."),
    ("Я всегда беру с собой обед в школу.", "I always pack my lunch for school."),
    ("В следующем месяце у нас будет научная ярмарка в школе.", "We have a science fair at school next month."),
    ("Школьная столовая подает вкусную еду.", "The school cafeteria serves delicious food."),
    ("Мне нужно готовиться к предстоящим экзаменам.", "I need to study for my upcoming exams."),
    ("Она вступила в школьный хор и поет красиво.", "She joined the school choir and sings beautifully."),
    ("У нашей школы есть баскетбольная площадка.", "We have a basketball court in our school."),
    ("Директор школы — строгий, но справедливый человек.", "The school principal is a strict but fair person."),
    ("С нетерпением жду школьного танца на следующей неделе.", "I'm looking forward to the school dance next week."),
    ("У меня много домашней работы после школы.", "I have a lot of homework to do after school."),
    ("В школе предлагается широкий спектр внеклассных мероприятий.", "The school offers a wide range of extracurricular activities."),
    ("Школьное собрание было наполнено восторженными учениками.", "The school assembly was filled with enthusiastic students."),
    ("Я являюсь частью школьной команды по дебатам.", "I'm part of the school debate team."),
    ("В школе есть хорошо оборудованная компьютерная лаборатория.", "The school has a well-equipped computer lab."),
    ("Она выиграла соревнование по правописанию в школе.", "She won the spelling bee competition at school."),
    ("Я являюсь членом школьного студенческого совета.", "I'm a member of the school student council."),
    ("Школьный годовой сборник запечатлевает воспоминания за учебный год.", "The school yearbook captures memories from the academic year."),
    ("У меня есть шкафчик, где я храню свои книги в школе.", "I have a locker where I keep my books at school."),
    ("Она капитан школьной футбольной команды.", "She is the captain of the school soccer team."),
    ("Школьный оркестр тренируется для предстоящего концерта.", "The school orchestra is practicing for their upcoming concert."),
    ("Я посещаю внешкольный художественный кружок.", "I'm attending an after-school art club."),
    ("Школьный спортзал — место, где мы проводим занятия по физической культуре.", "The school gymnasium is where we have physical education classes."),
    ("Она получила награду за успехи в учебе в школе.", "She got an award for academic excellence at school."),
    ("Не могу дождаться летних каникул, чтобы освободиться от школы.", "I can't wait for summer break to be free from school."),
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
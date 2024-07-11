import tkinter as tk
import random
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


sentences = [
("Family is the most important thing in my life.", "Семья - самое важное в моей жизни."),
("We are going to visit my grandparents this weekend.", "В эти выходные мы собираемся навестить моих бабушку и дедушку."),
("He has a big family with four siblings.", "У него большая семья из четырех братьев и сестер."),
("Family gatherings are always filled with laughter and joy.", "Семейные собрания всегда наполнены смехом и радостью."),
("She comes from a close-knit family.", "Она из семьи, где все близки друг другу."),
("I have fond memories of family vacations.", "У меня есть приятные воспоминания о семейных отпусках."),
("Family traditions are important to uphold.", "Семейные традиции важно сохранять."),
("My family has a tradition of having a big feast on holidays.", "У нашей семьи есть традиция устраивать большой праздничный пир."),
("She has a strong bond with her family.", "У нее крепкая связь со своей семьей."),
("I'm grateful for the love and support of my family.", "Я благодарен за любовь и поддержку своей семьи."),
("Having a loving family is a blessing.", "Иметь любящую семью - благословение."),
("She cherishes the time spent with her family.", "Она ценит время, проведенное с семьей."),
("Family reunions bring everyone together.", "Семейные воссоединения сближают всех."),
("She is a dedicated mother who always puts her family first.", "Она преданная мать, которая всегда ставит свою семью на первое место."),
("I'm proud to be a part of such a wonderful family.", "Я горжусь, что являюсь частью такой замечательной семьи."),
("Family support is crucial during difficult times.", "Семейная поддержка является важной в трудные времена."),
("She has a large extended family.", "У нее большая расширенная семья."),
("I have two loving parents who always support me.", "У меня двое любящих родителей, которые всегда меня поддерживают."),
("Family values play a significant role in shaping a person's character.", "Семейные ценности играют важную роль в формировании характера человека."),
("She enjoys spending quality time with her family.", "Ей нравится проводить качественное время со своей семьей."),
("Family is a source of strength and comfort.", "Семья - источник силы и утешения."),
("He is the head of the family.", "Он глава семьи."),
("I have a large family tree with many relatives.", "У меня большое семейное древо с множеством родственников."),
("She has a happy and loving family.", "У нее счастливая и любящая семья."),
("I'm looking forward to the family gathering next week.", "Я с нетерпением жду семейного собрания на следующей неделе."),
("Family bonds are unbreakable.", "Семейные связи нерушимы."),
("She has a big, noisy family, but she loves them all.", "У нее большая, шумная семья, но она всех их любит."),
("I enjoy family picnics in the park.", "Мне нравятся семейные пикники в парке."),
("She shares a close relationship with her siblings.", "У нее тесные отношения с братьями и сестрами."),
("Family is a place where you can always find love and acceptance.", "Семья - это место, где всегда можно найти любовь и принятие."),
("She has a beautiful family portrait hanging on the wall.", "У нее висит красивый семейный портрет на стене."),
]


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
back_button.pack(side=BOTTOM, pady=40)
next_button = ttk.Button(root, text="Дальше", command=show_random_sentences, style='Next.TButton')
next_button.pack(side=BOTTOM)
english_label = ttk.Label(root, textvariable=english_text, style='English.TLabel', justify=tk.LEFT)
english_label.pack(side=LEFT, fill=X, expand=True)
russian_label = ttk.Label(root, textvariable=russian_text, style='Russian.TLabel', justify=tk.LEFT)
russian_label.pack(side=RIGHT, fill=X, expand=True)
back_button.pack()
show_random_sentences()
root.mainloop()
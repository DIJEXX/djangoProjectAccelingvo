import tkinter as tk
import random
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


sentences = [
("Семья - самое важное в моей жизни.", "Family is the most important thing in my life."),
("В эти выходные мы собираемся навестить моих бабушку и дедушку.", "We are going to visit my grandparents this weekend."),
("У него большая семья из четырех братьев и сестер.", "He has a big family with four siblings."),
("Семейные собрания всегда наполнены смехом и радостью.", "Family gatherings are always filled with laughter and joy."),
("Она из семьи, где все близки друг другу.", "She comes from a close-knit family."),
("У меня есть приятные воспоминания о семейных отпусках.", "I have fond memories of family vacations."),
("Семейные традиции важно сохранять.", "Family traditions are important to uphold.",),
("У нашей семьи есть традиция устраивать большой праздничный пир.", "My family has a tradition of having a big feast on holidays."),
("У нее крепкая связь со своей семьей.", "She has a strong bond with her family."),
("Я благодарен за любовь и поддержку своей семьи.", "I'm grateful for the love and support of my family."),
("Иметь любящую семью - благословение.", "Having a loving family is a blessing."),
("Она ценит время, проведенное с семьей.", "She cherishes the time spent with her family."),
("Семейные воссоединения сближают всех.", "Family reunions bring everyone together."),
("Она преданная мать, которая всегда ставит свою семью на первое место.", "She is a dedicated mother who always puts her family first."),
("Я горжусь, что являюсь частью такой замечательной семьи.", "I'm proud to be a part of such a wonderful family."),
("Семейная поддержка является важной в трудные времена.", "Family support is crucial during difficult times."),
("У нее большая расширенная семья.", "She has a large extended family."),
("У меня двое любящих родителей, которые всегда меня поддерживают.", "I have two loving parents who always support me."),
("Семейные ценности играют важную роль в формировании характера человека.", "Family values play a significant role in shaping a person's character."),
("Ей нравится проводить качественное время со своей семьей.", "She enjoys spending quality time with her family."),
("Семья - источник силы и утешения.", "Family is a source of strength and comfort."),
("Он глава семьи.", "He is the head of the family."),
("У меня большое семейное древо с множеством родственников.", "I have a large family tree with many relatives."),
("У нее счастливая и любящая семья.", "She has a happy and loving family."),
("Я с нетерпением жду семейного собрания на следующей неделе.", "I'm looking forward to the family gathering next week."),
("Семейные связи нерушимы.", "Family bonds are unbreakable."),
("У нее большая, шумная семья, но она всех их любит.", "She has a big, noisy family, but she loves them all."),
("Мне нравятся семейные пикники в парке.", "I enjoy family picnics in the park."),
("У нее тесные отношения с братьями и сестрами.", "She shares a close relationship with her siblings."),
("Семья - это место, где всегда можно найти любовь и принятие.", "Family is a place where you can always find love and acceptance."),
("У нее висит красивый семейный портрет на стене.", "She has a beautiful family portrait hanging on the wall."),
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
back_button.pack(side=BOTTOM, pady=40)
next_button = ttk.Button(root, text="Next", command=show_random_sentences, style='Next.TButton')
next_button.pack(side=BOTTOM)
english_label = ttk.Label(root, textvariable=english_text, style='English.TLabel', justify=tk.LEFT)
english_label.pack(side=LEFT, fill=X, expand=True)
russian_label = ttk.Label(root, textvariable=russian_text, style='Russian.TLabel', justify=tk.LEFT)
russian_label.pack(side=RIGHT, fill=X, expand=True)
back_button.pack()
show_random_sentences()
root.mainloop()
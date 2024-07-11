import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def open_themes_window():
    main_window.destroy()
    os.system("python Data/themes.py")


def open_words_window():
    main_window.destroy()
    os.system("python Data/difficulty.py")


def open_text_window():
    main_window.destroy()
    os.system("python Data/text.py")


def open_sound_window():
    main_window.destroy()
    os.system("python Data/sound.py")

def close_main_window():
    main_window.destroy()
    os.system("python Data/registration.py")


main_window = Tk()
main_window.title("Accelingvo")
main_window.state('zoomed')
main_window.iconbitmap('Data/py.ico')
main_window.geometry("1920x1080")
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((main_window.winfo_screenwidth(), main_window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
style = ttk.Style()
style.configure("BW.TLabel", font=("Times New Roman", 32), foreground="#183b66", padding=8, background="#8fc6da")
style.configure("BW.TButton", font=("Times New Roman", 32, "bold"), foreground="#183b66", padding=12, background="#8fc6da")
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)
welcome_label = ttk.Label(main_window, text="Главное меню", style="BW.TLabel")
welcome_label.pack(pady=100)
words_button = ttk.Button(main_window, text="Темы", command=open_themes_window, style="BW.TButton")
words_button.pack(pady=10)
words_button = ttk.Button(main_window, text="Словари", command=open_words_window, style="BW.TButton")
words_button.pack(pady=10)
text_button = ttk.Button(main_window, text="Предложения", command=open_text_window, style="BW.TButton")
text_button.pack(pady=10)
sound_button = ttk.Button(main_window, text="Произношение и аудирование", command=open_sound_window, style="BW.TButton")
sound_button.pack(pady=10)
log_out_button = ttk.Button(main_window, text="Выйти", command=close_main_window, style="BW.TButton")
log_out_button.pack(pady=10)
main_window.mainloop()
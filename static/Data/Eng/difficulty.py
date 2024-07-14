from tkinter import Tk, Label, Button, StringVar
from PIL import Image, ImageTk
import os
from tkinter import ttk

def close_window():
    window.destroy()
    os.system("python Data/Eng/main.py")


def easy():
    window.destroy()
    os.system("python Data/Eng/Difficulty/dictionary1.py")


def medium():
    window.destroy()
    os.system("python Data/Eng/Difficulty/dictionary2.py")


def hard():
    window.destroy()
    os.system("python Data/Eng/Difficulty/dictionary3.py")

window = Tk()
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
selected_difficulty = StringVar()
gl_difficulty_label = ttk.Label(window, text="Choose the difficulty:", style="BW.TLabel")
gl_difficulty_label.pack(pady=100)
gl_button_easy = ttk.Button(window, text="Easy", command=easy, style="BW.TButton")
gl_button_easy.pack(pady=10)
gl_button_medium = ttk.Button(window, text="Average", command=medium, style="BW.TButton")
gl_button_medium.pack(pady=10)
gl_button_hard = ttk.Button(window, text="Hard", command=hard, style="BW.TButton")
gl_button_hard.pack(pady=10)
back_button = ttk.Button(window, text="←", style="BW.TButton", command=close_window)
back_button.pack(pady=10)
window.mainloop()
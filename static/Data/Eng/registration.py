from tkinter import ttk
import pymysql
from pymysql import Error
import os
from tkinter import *
from PIL import Image, ImageTk

def login_user():
    username = login_username_entry.get()
    passw = login_password_entry.get()
    try:
        connection = pymysql.connect(
            host="93.81.253.61",
            port=3306,
            user="chelik",
            password="1234",
            database="sakila",
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM qwerty  WHERE username=%s AND passw=%s"
                cursor.execute(sql, (username, passw))
                result = cursor.fetchone()
                a = str(result)
                if result:
                    if "''" in a:
                        result_label.config(text="Incorrect login or password", fg="red")
                    else:
                        first_window.withdraw()
                        open_main_window()
                else:
                    result_label.config(text="Incorrect login or password", fg="red")
        except Error as e:
            pass
        finally:
            connection.close()
    except Exception as ex:
        pass


def register_user():
    username = register_username_entry.get().strip()
    email = register_email_entry.get().strip()
    passw = register_password_entry.get().strip()
    try:
        connection = pymysql.connect(
            host="93.81.253.61",
            port=3306,
            user="chelik",
            password="1234",
            database="sakila",
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE IF NOT EXISTS `qwerty`(id int AUTO_INCREMENT," \
                                     " username varchar(32)," \
                                     " email varchar(32)," \
                                     " passw varchar(32), PRIMARY KEY (id));"
                cursor.execute(create_table_query)
                u1 = str(username)
                e1 = str(email)
                p1 = str(passw)
                if u1 == '' or e1 == '' or p1 == '' or len(u1) < 4 or e1.find('@') == -1 or e1.find('.') == -1:
                    result_label.config(text="Registration error", fg="red")
                else:
                    insert_query = """INSERT INTO qwerty (username, email, passw) VALUES (%s, %s, %s)"""
                    vals = (username, email, passw)
                    cursor.execute(insert_query, vals)
                    result_label.config(text="User successfully registered!", fg="green")
                    connection.commit()
        except Error as e:
            pass
        finally:
            connection.close()
    except Exception as ex:
        pass


def open_words_window():
    os.system("python Data/Eng/dictionary.py")


def open_text_window():
    os.system("python Data/Eng/text.py")


def open_sound_window():
    os.system("python Data/Eng/sound.py")


def open_difficulty_window():
    os.system("Data/Eng/difficulty.py")


def close_main_window():
    first_window.deiconify()


def close_gl_window():
    first_window.deiconify()


def open_main_window():
    os.system("python Data/Eng/main.py")

def close_window():
    first_window.destroy()
    os.system("python main.py")

first_window = Tk()
first_window.state('zoomed')
first_window.title("Accelingvo")
first_window.iconbitmap('Data/py.ico')
first_window.geometry("1920x1080")
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((first_window.winfo_screenwidth(), first_window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)

style = ttk.Style()
style.configure("BW.TLabel", font=("Times New Roman", 20), foreground="#183b66", padding=8, background="#8fc6da")
style.configure("BW.TButton", font=("Times New Roman", 24, "bold"), foreground="#183b66", padding=12, background="#8fc6da")
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)
register_label = ttk.Label(first_window, text="Sign up", style="BW.TLabel")
register_label.pack(pady=20)
register_username_label = ttk.Label(first_window, text="Username:", style="BW.TLabel")
register_username_label.pack()
register_username_entry = Entry(first_window, font=("Roboto", 20))
register_username_entry.pack()
register_email_label = ttk.Label(first_window, text="Email:", style="BW.TLabel")
register_email_label.pack()
register_email_entry = Entry(first_window, font=("Roboto", 20))
register_email_entry.pack()
register_password_label = ttk.Label(first_window, text="Password:", style="BW.TLabel")
register_password_label.pack()
register_password_entry = Entry(first_window, show="*", font=("Roboto", 20))
register_password_entry.pack()
register_button = ttk.Button(first_window, text="Finish", command=register_user, style="BW.TButton")
register_button.pack(pady=20)
login_label = ttk.Label(first_window, text="Log in", style="BW.TLabel")
login_label.pack(pady=20)
login_username_label = ttk.Label(first_window, text="Login:", style="BW.TLabel")
login_username_label.pack()
login_username_entry = Entry(first_window, font=("Roboto", 20))
login_username_entry.pack()
login_password_label = ttk.Label(first_window, text="Password:", style="BW.TLabel")
login_password_label.pack()
login_password_entry = Entry(first_window, show="*", font=("Roboto", 20))
login_password_entry.pack()
login_button = ttk.Button(first_window, text="Continue", command=login_user, style="BW.TButton")
login_button.pack(pady=20)
result_label = Label(first_window, text="", font=("Roboto", 32))
result_label.pack()
back_button = ttk.Button(first_window, text="←", style="BW.TButton", command=close_window)
back_button.pack(pady=10)
first_window.mainloop()
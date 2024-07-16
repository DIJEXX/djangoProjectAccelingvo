import random
import tkinter as tk

class Card:
    def init(self, front_text, back_text):
        self.front_text = front_text
        self.back_text = back_text

def create_cards(word_list):
    cards = []
    lines = word_list.strip().split("\n")
    for line in lines:
        parts = line.split("–")  # Разделитель "–"
        if len(parts) == 1:
            parts = line.split("-")  # Разделитель "-"
        if len(parts) > 1:
            front_text = parts[0].strip()
            back_text = parts[1].strip()
            cards.append(Card(front_text, back_text))
        else:
            print(f"Ignoring invalid entry: {line}")
    random.shuffle(cards)  # Shuffle the cards
    return cards

def show_cards(cards):
    root = tk.Tk()
    root.title("Flashcards")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 2000
    window_height = 400
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.configure(bg='black')

    current_card = tk.StringVar()
    current_card.set(cards[0].front_text)

    def show_translation():
        current_card.set(cards[index].back_text)

    def next_card():
        nonlocal index
        index = (index + 1) % len(cards)
        current_card.set(cards[index].front_text)

    index = 0

    card_label1 = tk.Label(root, fg="black", bg="black")
    card_label1.pack(pady=20)
    card_label = tk.Label(root, textvariable=current_card, font=("Arial", 28), fg="white", bg="black")
    card_label.pack(pady=20)

    def show_next_card(event=None):
        if next_button["text"] == "Show Translation":
            show_translation()
            next_button["text"] = "Next Card"
        else:
            next_card()
            current_card.set(cards[index].front_text)
            next_button["text"] = "Show Translation"

    next_button = tk.Button(root, text="Show Translation", command=show_next_card)
    next_button.pack(pady=10)

    root.bind_all('<Return>', show_next_card)

    is_fullscreen = False  # Переменная, хранящая состояние окна

    def toggle_fullscreen(event=None):
        nonlocal is_fullscreen
        is_fullscreen = not is_fullscreen
        root.wm_attributes("-fullscreen", is_fullscreen)

    root.bind_all('<F11>', toggle_fullscreen)  # Привязываем событие нажатия клавиши F11

    root.mainloop()


def main():
    word_list = """
Accept – Принимать, одобрять, признавать
Access – Доступ, обращение, оценивать
Accurate – Точный, тщательный
Application – Приложение, прикладная программа; Применение, использование
Apply – Использовать, применять; Прилагать, прикладывать
Backup – Резервная копия
Bug/Error – Ошибка
Cancel – Отменить
Charge – Заряд
Data – Данные, информация, Сведения
Default – По умолчанию
Delete – Удалять
Develop – Разрабатывать
Under development – В разработке
Download – Скачивать
Erase – Стирать, разрушать
Error – Ошибка, погрешность
Fix – Исправление ошибки в программе
Font – Шрифт
Keyboard – Клавиатура, клавишная панель
Input – Ввод, вход
Install – Устанавливать
To load – Загружать
Password – Пароль
To press a key – Нажимать на клавишу
Accomplish – Выполнять
Adjust/Customize – Регулировать; Настраивать; Корректировать; Adjustment сущ
Advantage – Преимущество; Выгода, польза
Advert – Реклама; Объявление Advertise гл. Advertisement сущ
Affect – Действовать, воздействовать, влиять
Aid – Помощь, содействие ; Aids - Пособия
Aligh – Выравнивать, распологать по одной линии; left, right - По краю
Alter – Изменять, перестраивать, преобразовывать
Amend – Изменять, вносить поправки, редактировать
Anticipate, Warning – Опережать, упреждать, Предупреждать
Appliance – Прибор, приспособление, устройство
Approach – Подход, позиция, Метод
Approximate – Приближать
Access – Оценивать, Доступ
Assign, give – Назначать, присваивать; Давать
Attach – Прикреплять, присоединять; Подсоединять; Attachment сущ
Backbone – Магистральный, стержневой, основной, базовый
Band/Bandwidth – Полоса частот
Bar-code scanner – Устройство считывания штрих-кода
Benefit – Выгода, Польза
Board – Плата, Панель, пульт, стол, щит
Behavior – Режим работы
Boot – Загрузка (начальная)
Broadband – Широкополосная передача
Browse – Просматривать
Burn – Записывать файлы на компакт-диск
Bus – Шина, канал передачи информации
Button – Кнопка мыши
Capable – Способный
Capacity – Ёмкость; Мощность, нагрузка, производительность
Caption – Подпись, надпись
Card – Плата, Карта
Case – Регистр (клавиатуры), нижний Верхний
Cause – Причина
Chart/Circuit – Схема, 1 Диаграмма, таблица, график; 2 цепь, контур
Chip – Микросхема, интегральная схема
Click – Нажать кнопку мыши, кликнуть
Cloud computing – Облачные вычисления
Continuing quantity – Непрерывная величина
Collocation – Сочетание слов; Устойчивое словосочетание
Compability – Совместимость; Соответствие
Conceal – Скрывать, укрывать
Conduct – Проводить; Ставить (опыты); Вести; Руководить
Confine – Ограничивать
Conform – Соответствовать
Contribute – Содействовать, способствовать; Делать вклад
Convenience – Удобство; Convenient прил
Conventions – Условные обозначения
Convert – Преобразовывать; Превращать
Computer privacy – Защищённость компьютера
Corrupt – Портить, искажать
To cut out the human beings altogether – Полностью исключить человеческий фактор
Customize – Настраивать; Подстраивать; Переделывать, подгонять (под заказчика)
Damage – Повреждать, разрушать, наносить ущерб
Debug – Отлаживать (программу)
Decrease – Уменьшение, снижение, падение
Determination – Определение; Установление
Pointing device – Указательное устройство
Digit – Цифра; Разряд
Digital – Цифровой
Disposition – Удаление
Disadvantage – Недостаток; Ущерб; Невыгодное положение
Disconnect – Разъединять, размыкать
Distinct – Разный, различный; Явный, отчётливый
Downsizing – Уменьшение размера
Drag – Перетаскивать, передвигать
Drive – Диск, Накопитель, дисковод; Привод, передача
Flash drive – Флэшка, флэш-накопитель
Durability – Долговечность, прочность
Eliminating memory tasks – Остановка ресурсозатратных задач
Eject – Выдавать, испускать
Eliminate – Устранить, исключить
Embedded – Встроенный; Вложенный
Emerge – Появляться, возникать
Employ – Нанимать, предоставлять работу; использовать, применять
Embedded circuitry – Встроенные электронные схемы
Encounter – Сталкиваться, неожиданно встретиться, наталкиваться
Encrypt – Шифровать, кодировать
Enhance – Улучшать, совершенствовать
Equation – Уравнение
Evaluate – Оценивать, давать оценку

Execute – Исполнять, выполнять
Exponentiation – Возведение в степень
To evolve – Развивать, усовершенствовать
To feed – Подавать, вводить данные
Fire – Запускать, срабатывать, возбуждать
Firewall – Брандмауэр, Межсетевой экран, защитная система
Firewire – Скоростной последовательный интерфейс
Fit – Собирать, монтировать; Прогонять, приспасабливать; Помещаться
Flame – Наезд, ругань в сети; Скандальное послание
Flaw – Дефект, недостаток; Изьян
Flowchart – Блок-схема
Footer – Нижний колонтитул
Framework – Структура, основа, база, оболочка, конструкция
Frequency – Частота, повторяемость
Gain – Получать, приобретать; Добиваться
Gateway – Сетевой шлюз
Handle – Обрабатывать, оперировать, манипулировать
Hardware – Железо, технические средства(обеспечение); Аппаратное оборудование
Hard drive – запоминающие средства, привод, Жёсткий диск
Heavy-duty – Работающий в тяжелом режиме
Highlight – ярко освещать, выдвигать на первый план, придавать большое значение
Highway – Магистраль, магистральная шина; Канал информации
Hook up – Соединять, подключать, связывать
Hop – Транзит, Транзитный участок, Пересылка

., [16.07.2024 20:58]
Keypad – Малая клавиатура
Kickstand – Подставка, стойка
Immediate access – Прямой доступ
Internet browsing – Просмотр компьютерной сети
Internet faxing – Передача сообщений по компьютерной сети
Initiate – Приведение в действие
Indication – Введение отступов, Структурированное расположение текста
Insert – Вставлять; Вкладывать
Integrate – Объединять, интегрировать; Integrity - Целостность
Interconnect – Взаимосвязывать
Instruction set – Система команд
To issue – Посылать сигнал, Выдавать сообщение
Key – Клавиша
Lack – Отсутствие, нехватка, недостаток, дефицит
Lack the versatility – Не хватать многофункциональности
Layer – Слой; Уровень (иерархии)
Layout – Схема расположения, планировка, компоновка, план
Lead to – Вызвать, приводить (к чему-либо), иметь результатом
Link – Связь, звено, связующее звено
Log in/Log out – Входить/выходить в/из системы
Loop – Цикл (Программный)
Loudspeaker – Динамик; Громкоговоритель
Mainboard – Материнская плата, системная плата
Maintain – Обслуживать, Содержать в исправности; Поддерживать, сохранять
Malware – Вредоносное ПО
Margin – Поле, край, граница
Master – Оригинал, эталон; Ведущее устройство, Хозяин
Match – Сочетать; Согласовывать; Подгонять, подбирать
To manipulate – Управлять, обрабатывать, преобразовывать
Compact disk read-only memory – Пзу на компакт-диске
Non-volatile memory – энергонезависимая память
Volatile memory – энергозависимая память
Radon access memory (RAM) – Память с произвольной выборкой
Read only memory (ROM) – Постоянная память
Mode – Режим работы; Способ, метод, принцип (работы)
Dial-up modem – Модем коммутируемой линии передачи
CRT (cathode ray tube) monitor – ЭЛТ-монитор, электролучевая трубка
LCD (liquid crystal display) monitor – ЖК-монитор жидко-кристаллический
LED (light-emitting diodes) monitor – Монитор на основе светоизлучающих диодов
Motherboard – Материнская плата, системная плата
Mount – Монтировать, устанавливать
Net – Интернет
Notation/Record – Запись; Представление; Система обозначений; Нотация
The number of failures – Количество отказов
Operate – Производить операции; Работать, функционировать; Режим работы
Outsourcing – Привлечение внешних исполнителей для решения собственных проблем
Pan – Панорамировать
To pitch – Иметь наклон, уклон
Plug(into) – (вставлять)Разъём, гнездо 
To point – Указывать, показывать (show)
Prevent – Предотвращать, мешать, препятствовать
Processing – Обработка; Технологический процесс
Processing power – Скорость обработки
Proliferation – Размножение, быстрое увеличение
Network service provider – Поставщик сетевых услуг
Proxy – Модуль доступа; Программа посредник
Query – Запрос
Range – Диапазон, интервал, ряд, серия
Rate – частота
Ratio – Коэффициент
Random Access Memory – Озу, оперативно запоминающее устройство
Refer to information – Обращаться к информации
Reference – Ссылка, отсылка
Retention – Хранение
Release – Выпускать
Rely/Trust – Доверять
Remote – Дистанционный, удалённый
Removable – Съёмный
Replace – Заменять
Require – Требовать

Restrict – Ограничивать
To result in – Следовать
Retrieve – Извлекать
Reveal – Показывать
Ribbon – Лента
Rotate – Вращать
Route – Маршрут
Router – Маршрутизатор
Run – Выполнять, запускать
Safeguard – Предохранитель
Scatternet – Распределённая сеть
Scramble – Скремблировать, зашифровать
Search engine –  система поиска
Secure – Защищённый, безопасный
Security – Защита
Self-contained – Автономный
Separate – Отдельный
Sequence – Последовательность
Remote server – Удалённый сервер
Shade – экран, затенять
Style sheet – Таблица стилей
Shift – Смещение, сдвиг
Shortcut – Сокращенное наименование
Sign – Предъявлять пароль
Sign-on – Предъявление пароля
Simulate – Имитировать
Slave – Подчинённый компонент системы
Slide – Скользить
Slot – Гнездо
Socket – Гнездо, розетка
Software – Программное обеспечение
Speaker – Колонка

., [16.07.2024 20:58]
Split – Разделение, дробление
Spread – Распространение
State – Режим, состояние
Storage – Хранилище
Removable storage – Съёмное запоминающее устройство
Store – Хранилище
Stream – Поток
Strike – Ударять, нажимать
Substitute – Замена
Suit – Подходить, соответствовать, устраивать
Suite – Комплект, набор
Application suite – Прикладной программный комплекс
Supplied data – Введённые данные
Swipe an icon – Провести пальцем иконку
Switch – Переключать
System – Система
Tablet – Планшет
Tailor – Приспосабливать
Tabulate the census – Занести данные по переписи в таблицу
Telework – Работать дистанционно
Tier – Ряд
Response time – Время отклика
Standby time – Время ожидания ответа
Programming tools – Средства программирования
Touchscreen – Сенсорный экран
Tower – Вертикальный корпус
Track – Канал, дорожка
Transaction – Сделка, транзакция
Unit – Устройство
USB (Universal Serial Bus) – Универсальная последовательная шина, интерфейс USB
User interaction – Диалог системы с пользователем
Utility – Утилита, служебная программа
Utilize – Использовать
Voltage – Напряжение
Volatile – Временный
Volume – Громкость
Web-based application – Веб-приложения
Wheel – Колесо
Widespread – Широко распространённый
Wire – Провод
Wireless – Беспроводной
Wiretap – Подключение к линии
Worth – Стоящий, заслуживающий
Be worth – Заслуживать
Wrap – Заключать в оболочку
Account – Аккаунт, учётная запись; Отчёт, доклад, рассказ, описание
Animation – Анимация, мультипликация
Annotate – Аннотировать (примечание), давать примечание, комментировать
Applet – Апплет, прикладная мини-программа
Interactive program – Интерактивная прикладная программа
Assistant – Ассистент, помощник
Browser – Браузер
Disk – Диск
Domain – Домен, область, зона
Host – Хост; Главный/Ведущий компьютер
Hypermedia – Гипермедия, гиперсреда
Hypertext – Гипертекст, обощённый текст
Interface – Интерфейс, сопрягать, устройство сопряжения
Process – Процесс, способ, метод
Processor – Процессор; Узел обработки
Provider – Провайдер, поставщик
"""
    cards = create_cards(word_list)
    show_cards(cards)

if __name__ == "main":
    main()

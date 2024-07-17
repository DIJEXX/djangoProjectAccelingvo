import random

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from myapp.templates.themes.sentencesbank import sentences1, sentences2, sentences3, sentences4, sentences5, psentences, \
    ptranslations
from myapp.templates.sound.sentencesp import sentencesforsay
import sounddevice as sd
from scipy.io.wavfile import write
from playsound3 import playsound3
from gtts import gTTS
import os


def index(request):
    return render(request, 'index.html')


def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")

    context = {'registerform': form}

    return render(request, 'register.html', context=context)


def my_login(request):
    print("login")
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("main")

    context = {'loginform': form}

    return render(request, 'login.html', context=context)


def main(request):
    return render(request, 'main.html')


# new
class Card:
    def __init__(self, front_text, back_text):
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

def show_cards(request):
    if 'index' not in request.session:
        request.session['index'] = 0
        request.session['show_translation'] = False

    index = request.session['index']
    show_translation = request.session['show_translation']

    if request.method == 'POST':
        if 'next' in request.POST:
            request.session['index'] = (index + 1) % len(cards)
            request.session['show_translation'] = False
        elif 'show_translation' in request.POST:
            request.session['show_translation'] = True

        return redirect('show_cards')

    current_card = cards[index]
    context = {
        'front_text': current_card.front_text,
        'back_text': current_card.back_text if show_translation else '',
        'show_translation': show_translation
    }
    return render(request, 'show_cards.html', context)


def themes(request):
    return render(request, 'themes.html')


def popular(request):
    random.shuffle(sentences1)
    english_sentences = [sentence[0] for sentence in sentences1[:5]]
    russian_sentences = [sentence[1] for sentence in sentences1[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'themes/popular.html', context)


def family(request):
    random.shuffle(sentences2)
    english_sentences = [sentence[0] for sentence in sentences2[:5]]
    russian_sentences = [sentence[1] for sentence in sentences2[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'themes/family.html', context)


def school(request):
    random.shuffle(sentences3)
    english_sentences = [sentence[0] for sentence in sentences3[:5]]
    russian_sentences = [sentence[1] for sentence in sentences3[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'themes/school.html', context)


def shop(request):
    random.shuffle(sentences4)
    english_sentences = [sentence[0] for sentence in sentences4[:5]]
    russian_sentences = [sentence[1] for sentence in sentences4[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'themes/shop.html', context)


def doctor(request):
    random.shuffle(sentences5)
    english_sentences = [sentence[0] for sentence in sentences5[:5]]
    russian_sentences = [sentence[1] for sentence in sentences5[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'themes/doctor.html', context)


def get_random_sentence():
    index = random.randint(0, len(psentences) - 1)
    return psentences[index], ptranslations[index]


def sentence(request):
    if request.method == 'POST':
        user_translation = request.POST.get('translation')
        correct_translation = request.POST.get('correct_translation')
        if user_translation == correct_translation:
            result = "Правильный перевод!"
            color = "green"
        else:
            result = "Неправильный перевод!"
            color = "red"
    else:
        result = ""
        color = ""

    sentence, translation = get_random_sentence()
    context = {
        'sentence': sentence,
        'correct_translation': translation,
        'result': result,
        'color': color
    }
    return render(request, 'sentence.html', context)


def my_sound(request):
    if 'current_sentence_index' not in request.session:
        request.session['current_sentence_index'] = 0
    current_sentence_index = request.session['current_sentence_index']
    current_sentence = sentencesforsay[current_sentence_index]

    if request.method == 'POST':
        if 'next' in request.POST:
            # Выбираем случайное предложение
            current_sentence_index = random.randint(0,
                                                    len(sentencesforsay) - 1)  # (current_sentence_index + 1) % len(sentencesforsay)
            request.session['current_sentence_index'] = current_sentence_index
            current_sentence = sentencesforsay[current_sentence_index]

        elif 'playtext' in request.POST:
            tts = gTTS(text=current_sentence, lang='en')
            tts.save("myapp/templates/sound/reformation.mp3")
            playsound3.playsound("myapp/templates/sound/reformation.mp3")

        elif 'record' in request.POST:
            fs = 44100  # Частота дискретизации
            seconds = 5  # Продолжительность записи (в секундах)
            audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
            sd.wait()
            write("myapp/templates/sound/recorded_voice.wav", fs, audio)
        elif 'play' in request.POST:
            playsound3.playsound("myapp/templates/sound/recorded_voice.wav")

    context = {
        'sentence': current_sentence
    }
    return render(request, 'sound.html', context)


def dictionary(request):
    return render(request, 'dictionary.html')


ewords = []
elearned_words = 0


def eload_words():
    global ewords, elearned_words
    elearned_words = 0
    with open("myapp/templates/difficulty/dictionary1.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            word, translation, learned = line.strip().split("|")
            ewords.append((word, translation, learned == "True"))
            if learned == "True":
                elearned_words += 1


def esave_words():
    global ewords
    with open("myapp/templates/difficulty/dictionary1.txt", "w", encoding="utf-8") as file:
        for word, translation, learned in ewords:
            file.write(f"{word}|{translation}|{str(learned)}\n")


def eget_next_word_index(current_word_index):
    global ewords
    next_word_index = current_word_index + 1
    while next_word_index < len(ewords) and ewords[next_word_index][2]:
        next_word_index += 1
    if next_word_index < len(ewords):
        return next_word_index
    else:
        return -1


def easy(request):
    global ewords, elearned_words
    if not ewords:
        eload_words()
    current_word_index = request.session.get('current_word_index', 0)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'next':
            current_word_index = eget_next_word_index(current_word_index)
        elif action == 'check':
            request.session['show_translation'] = True
        elif action == 'done':
            word, translation, learned = ewords[current_word_index]
            if not learned:
                ewords[current_word_index] = (word, translation, True)
                elearned_words += 1
            current_word_index = eget_next_word_index(current_word_index)
        elif action == 'clear':
            elearned_words = 0
            for i in range(len(ewords)):
                word, translation, learned = ewords[i]
                if learned:
                    ewords[i] = (word, translation, False)
        elif action == 'save':
            esave_words()
        elif action == 'statistics':
            request.session['show_statistics'] = True
        request.session['current_word_index'] = current_word_index
        # return redirect('easy')

    word, translation, learned = ewords[current_word_index]
    context = {
        'word': word,
        'translation': translation if request.session.get('show_translation') else '',
        'learned_words': elearned_words if request.session.get('show_statistics') else None
    }
    request.session['show_translation'] = False
    request.session['show_statistics'] = False
    return render(request, 'difficulty/easy.html', context)


mwords = []
mlearned_words = 0


def mload_words():
    global mwords, mlearned_words
    mlearned_words = 0
    with open("myapp/templates/difficulty/dictionary2.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            word, translation, learned = line.strip().split("|")
            mwords.append((word, translation, learned == "True"))
            if learned == "True":
                mlearned_words += 1


def msave_words():
    global mwords
    with open("myapp/templates/difficulty/dictionary2.txt", "w", encoding="utf-8") as file:
        for word, translation, learned in mwords:
            file.write(f"{word}|{translation}|{str(learned)}\n")


def mget_next_word_index(current_word_index):
    global mwords
    next_word_index = current_word_index + 1
    while next_word_index < len(mwords) and mwords[next_word_index][2]:
        next_word_index += 1
    if next_word_index < len(mwords):
        return next_word_index

    else:
        return -1


def medium(request):
    global mwords, mlearned_words
    if not mwords:
        mload_words()
    current_word_index = request.session.get('current_word_index', 0)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'next':
            current_word_index = mget_next_word_index(current_word_index)
        elif action == 'check':
            request.session['show_translation'] = True
        elif action == 'done':
            word, translation, learned = mwords[current_word_index]
            if not learned:
                mwords[current_word_index] = (word, translation, True)
                mlearned_words += 1
            current_word_index = mget_next_word_index(current_word_index)
        elif action == 'clear':
            mlearned_words = 0
            for i in range(len(mwords)):
                word, translation, learned = mwords[i]
                if learned:
                    mwords[i] = (word, translation, False)
        elif action == 'save':
            msave_words()
        elif action == 'statistics':
            request.session['show_statistics'] = True
        request.session['current_word_index'] = current_word_index
        # return redirect('easy')

    word, translation, learned = mwords[current_word_index]
    context = {
        'word': word,
        'translation': translation if request.session.get('show_translation') else '',
        'learned_words': mlearned_words if request.session.get('show_statistics') else None
    }
    request.session['show_translation'] = False
    request.session['show_statistics'] = False
    return render(request, 'difficulty/medium.html', context)


hwords = []
hlearned_words = 0


def hload_words():
    global hwords, hlearned_words
    hlearned_words = 0
    with open("myapp/templates/difficulty/dictionary3.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            word, translation, learned = line.strip().split("|")
            hwords.append((word, translation, learned == "True"))
            if learned == "True":
                hlearned_words += 1


def hsave_words():
    global hwords
    with open("myapp/templates/difficulty/dictionary3.txt", "w", encoding="utf-8") as file:
        for word, translation, learned in hwords:
            file.write(f"{word}|{translation}|{str(learned)}\n")


def hget_next_word_index(current_word_index):
    global hwords
    next_word_index = current_word_index + 1
    while next_word_index < len(hwords) and hwords[next_word_index][2]:
        next_word_index += 1
    if next_word_index < len(hwords):
        return next_word_index
    else:
        return -1


def hard(request):
    global hwords, hlearned_words
    if not hwords:
        hload_words()
    current_word_index = request.session.get('current_word_index', 0)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'next':
            current_word_index = hget_next_word_index(current_word_index)
        elif action == 'check':
            request.session['show_translation'] = True
        elif action == 'done':
            word, translation, learned = hwords[current_word_index]
            if not learned:
                hwords[current_word_index] = (word, translation, True)
                hlearned_words += 1
            current_word_index = hget_next_word_index(current_word_index)
        elif action == 'clear':
            hlearned_words = 0
            for i in range(len(hwords)):
                word, translation, learned = hwords[i]
                if learned:
                    hwords[i] = (word, translation, False)
        elif action == 'save':
            hsave_words()
        elif action == 'statistics':
            request.session['show_statistics'] = True
        request.session['current_word_index'] = current_word_index
        # return redirect('easy')

    word, translation, learned = hwords[current_word_index]
    context = {
        'word': word,
        'translation': translation if request.session.get('show_translation') else '',
        'learned_words': hlearned_words if request.session.get('show_statistics') else None
    }
    request.session['show_translation'] = False
    request.session['show_statistics'] = False
    return render(request, 'difficulty/hard.html', context)

import random
from django.conf import settings
from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


sentences1 = [
    ("I like to watch movies.", "Мне нравится смотреть фильмы."),
    ("She speaks three languages.", "Она говорит на трех языках."),
    ("He is a talented musician.", "Он талантливый музыкант."),
    ("Do you want to go for a walk?", "Хочешь пойти на прогулку?"),
    ("My favorite color is blue.", "Мой любимый цвет - синий."),
    ("We went to the beach yesterday.", "Вчера мы поехали на пляж."),
    ("She is a great dancer.", "Она отличная танцовщица."),
    ("I have a pet cat.", "У меня есть домашний кот."),
    ("They live in a beautiful house.", "Они живут в красивом доме."),
    ("He plays the guitar very well.", "Он очень хорошо играет на гитаре."),
    ("I'm studying computer science.", "Я изучаю компьютерные науки."),
    ("She enjoys reading books.", "Ей нравится читать книги."),
    ("Do you have any siblings?", "У тебя есть братья или сестры?"),
    ("He works as a software engineer.", "Он работает инженером-программистом."),
    ("My parents are coming to visit.", "Мои родители приезжают в гости."),
    ("She likes to play tennis.", "Ей нравится играть в теннис."),
    ("I want to learn how to cook.", "Я хочу научиться готовить."),
    ("We need to buy some groceries.", "Нам нужно купить продукты."),
    ("He is always on time.", "Он всегда приходит вовремя."),
    ("She is a good friend.", "Она хороший друг."),
    ("Do you have any plans for the weekend?", "У тебя есть планы на выходные?"),
    ("I'm going to visit my grandparents.", "Я собираюсь навестить своих бабушку и дедушку."),
    ("She wants to become a doctor.", "Она хочет стать врачом."),
    ("I need to buy a new phone.", "Мне нужно купить новый телефон."),
    ("We are going on a trip next week.", "Мы собираемся в путешествие на следующей неделе."),
    ("He is a talented artist.", "Он талантливый художник."),
    ("She has a beautiful voice.", "У нее красивый голос."),
    ("Do you like to go hiking?", "Тебе нравится ходить в походы?"),
    ("I'm excited about the concert tonight.", "Я взволнована концертом сегодня вечером."),
    ("She enjoys playing video games.", "Ей нравится играть в видеоигры."),
    ("I have a meeting at 3 PM.", "У меня встреча в 15:00."),
]


sentences2 = [
    ("Family is the most important thing in my life.", "Семья - самое важное в моей жизни."),
    ("We are going to visit my grandparents this weekend.",
     "В эти выходные мы собираемся навестить моих бабушку и дедушку."),
    ("He has a big family with four siblings.", "У него большая семья из четырех братьев и сестер."),
    ("Family gatherings are always filled with laughter and joy.",
     "Семейные собрания всегда наполнены смехом и радостью."),
    ("She comes from a close-knit family.", "Она из семьи, где все близки друг другу."),
    ("I have fond memories of family vacations.", "У меня есть приятные воспоминания о семейных отпусках."),
    ("Family traditions are important to uphold.", "Семейные традиции важно сохранять."),
    ("My family has a tradition of having a big feast on holidays.",
     "У нашей семьи есть традиция устраивать большой праздничный пир."),
    ("She has a strong bond with her family.", "У нее крепкая связь со своей семьей."),
    ("I'm grateful for the love and support of my family.", "Я благодарен за любовь и поддержку своей семьи."),
    ("Having a loving family is a blessing.", "Иметь любящую семью - благословение."),
    ("She cherishes the time spent with her family.", "Она ценит время, проведенное с семьей."),
    ("Family reunions bring everyone together.", "Семейные воссоединения сближают всех."),
    ("She is a dedicated mother who always puts her family first.",
     "Она преданная мать, которая всегда ставит свою семью на первое место."),
    ("I'm proud to be a part of such a wonderful family.", "Я горжусь, что являюсь частью такой замечательной семьи."),
    ("Family support is crucial during difficult times.", "Семейная поддержка является важной в трудные времена."),
    ("She has a large extended family.", "У нее большая расширенная семья."),
    ("I have two loving parents who always support me.",
     "У меня двое любящих родителей, которые всегда меня поддерживают."),
    ("Family values play a significant role in shaping a person's character.",
     "Семейные ценности играют важную роль в формировании характера человека."),
    ("She enjoys spending quality time with her family.", "Ей нравится проводить качественное время со своей семьей."),
    ("Family is a source of strength and comfort.", "Семья - источник силы и утешения."),
    ("He is the head of the family.", "Он глава семьи."),
    ("I have a large family tree with many relatives.", "У меня большое семейное древо с множеством родственников."),
    ("She has a happy and loving family.", "У нее счастливая и любящая семья."),
    ("I'm looking forward to the family gathering next week.",
     "Я с нетерпением жду семейного собрания на следующей неделе."),
    ("Family bonds are unbreakable.", "Семейные связи нерушимы."),
    ("She has a big, noisy family, but she loves them all.", "У нее большая, шумная семья, но она всех их любит."),
    ("I enjoy family picnics in the park.", "Мне нравятся семейные пикники в парке."),
    ("She shares a close relationship with her siblings.", "У нее тесные отношения с братьями и сестрами."),
    ("Family is a place where you can always find love and acceptance.",
     "Семья - это место, где всегда можно найти любовь и принятие."),
    ("She has a beautiful family portrait hanging on the wall.", "У нее висит красивый семейный портрет на стене."),
]


sentences3 = [
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
    ("I can't wait for summer break to be free from school.",
     "Не могу дождаться летних каникул, чтобы освободиться от школы."),
]


sentences4 = [

]


sentences5 = [

]


def index(request):
    return render(request, 'index.html')

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")


    context = {'registerform':form}

    return render(request, 'register.html', context=context)



def my_login(request):

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


    context = {'loginform':form}

    return render(request, 'login.html', context=context)
def main(request):
    return render(request, 'main.html')


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


psentences = [
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

ptranslations = [
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



def difficulty(request):
    return render(request, 'difficulty.html')
def sound(request):
    return render(request, 'sound.html')

def text(request):
    return render(request, 'text.html')



def difficulty_level(request, level):
    return render(request, 'difficulty_level.html', {'level': level})

def theme_selection(request, theme):
    return render(request, 'theme_selection.html', {'theme': theme})
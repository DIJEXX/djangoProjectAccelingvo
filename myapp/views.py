import random
from django.conf import settings
from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


sentences1 = [

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

]


sentences4 = [

]


sentences5 = [

]

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
    random.shuffle(sentences2)
    english_sentences = [sentence[0] for sentence in sentences2[:5]]
    russian_sentences = [sentence[1] for sentence in sentences2[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'popular.html', context)


def family(request):
    random.shuffle(sentences2)
    english_sentences = [sentence[0] for sentence in sentences2[:5]]
    russian_sentences = [sentence[1] for sentence in sentences2[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'family.html', context)


def school(request):
    random.shuffle(sentences2)
    english_sentences = [sentence[0] for sentence in sentences2[:5]]
    russian_sentences = [sentence[1] for sentence in sentences2[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'school.html', context)


def shop(request):
    random.shuffle(sentences2)
    english_sentences = [sentence[0] for sentence in sentences2[:5]]
    russian_sentences = [sentence[1] for sentence in sentences2[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'shop.html', context)


def doctor(request):
    random.shuffle(sentences2)
    english_sentences = [sentence[0] for sentence in sentences2[:5]]
    russian_sentences = [sentence[1] for sentence in sentences2[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'doctor.html', context)


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
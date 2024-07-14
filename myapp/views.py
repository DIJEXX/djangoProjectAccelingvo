from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import random
from django.conf import settings
from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required


# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

sentences = [
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

def family(request):
    random.shuffle(sentences)
    english_sentences = [sentence[0] for sentence in sentences[:5]]
    russian_sentences = [sentence[1] for sentence in sentences[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'family.html', context)

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

# def login(request):
#     return render(request, 'login.html')

def difficulty(request):
    return render(request, 'difficulty.html')
def sound(request):
    return render(request, 'sound.html')

def text(request):
    return render(request, 'text.html')

def themes(request):
    return render(request, 'themes.html')

def difficulty_level(request, level):
    return render(request, 'difficulty_level.html', {'level': level})

def theme_selection(request, theme):
    return render(request, 'theme_selection.html', {'theme': theme})
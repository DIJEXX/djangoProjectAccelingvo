import random
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from myapp.templates.themes.sentencesbank import sentences1, sentences2, sentences3, sentences4, sentences5, psentences, \
    ptranslations, word_list
from myapp.templates.sound.sentencesp import sentencesforsay
import sounddevice as sd
from scipy.io.wavfile import write
from playsound3 import playsound3
from gtts import gTTS


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
    random.shuffle(cards)  # Shuffle the cards
    return cards


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


# def doctor(request):
#     random.shuffle(sentences5)
#     english_sentences = [sentence[0] for sentence in sentences5[:5]]
#     russian_sentences = [sentence[1] for sentence in sentences5[:5]]
#     context = {
#         'english_sentences': english_sentences,
#         'russian_sentences': russian_sentences
#     }
#     return render(request, 'themes/doctor.html', context)
def travel(request):
    random.shuffle(sentences5)
    english_sentences = [sentence[0] for sentence in sentences5[:5]]
    russian_sentences = [sentence[1] for sentence in sentences5[:5]]
    context = {
        'english_sentences': english_sentences,
        'russian_sentences': russian_sentences
    }
    return render(request, 'themes/travel.html', context)


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

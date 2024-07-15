import random
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from myapp.templates.themes.sentencesbank import sentences1, sentences2, sentences3, sentences4, sentences5, psentences, \
    ptranslations
from myapp.templates.difficulty.dictionary import dictionary1, dictionary2, dictionary3
from myapp.templates.sound.sentencesp import sentencesforsay

import sounddevice as sd
from scipy.io.wavfile import write
from playsound3 import playsound3
from gtts import gTTS
import os

def my_sound(request):
    if 'current_sentence_index' not in request.session:
        request.session['current_sentence_index'] = 0
    current_sentence_index = request.session['current_sentence_index']
    current_sentence = sentencesforsay[current_sentence_index+2]

    if request.method == 'POST':
        if 'next' in request.POST:
            current_sentence_index = (current_sentence_index + 1) % len(sentencesforsay)
            request.session['current_sentence_index'] = current_sentence_index
            tts = gTTS(text=sentencesforsay[current_sentence_index+1], lang='en')
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


def dictionary(request):
    return render(request, 'dictionary.html')


def easy(request):
    return render(request, 'difficulty/easy.html')


def medium(request):
    return render(request, 'difficulty/medium.html')


def hard(request):
    return render(request, 'difficulty/hard.html')


def sound(request):
    return render(request, 'sound.html')

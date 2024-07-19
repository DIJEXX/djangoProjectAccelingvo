FROM python:3.12.4

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev gettext cron openssh-client flake8 locales vim ffmpeg libportaudio2 libasound-dev python3-pip

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /accelingvo

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install --upgrade wheel

RUN useradd -rms /bin/bash accelingvo && chmod 777 /opt /run

RUN mkdir /accelingvo/static && chown -R accelingvo:accelingvo /accelingvo && chmod 777 /accelingvo

COPY --chown=accelingvo:accelingvo . .

RUN pip install -r requirements.txt

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

USER accelingvo

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]






#python manage.py makemigrations
#python manage.py migrate
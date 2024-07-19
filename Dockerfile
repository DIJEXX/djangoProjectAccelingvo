FROM python:3.12.4


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN python -m pip install --upgrade pip

RUN python -m pip install --upgrade wheel

RUN python -m venv .venv

RUN source .venv/bin/activate

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev gettext cron openssh-client flake8 locales ffmpeg vim

RUN useradd -rms /bin/bash accelingvo && chmod 777 /opt /run

WORKDIR /accelingvo

RUN mkdir /accelingvo/static && chown -R accelingvo:accelingvo /accelingvo && chmod 755 /accelingvo

COPY --chown=accelingvo:accelingvo . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "makemigrations"]

CMD ["python", "manage.py", "migrate"]

USER accelingvo

CMD ["python", "manage.py", "runserver", "localhost:8000"]






#python manage.py makemigrations
#python manage.py migrate
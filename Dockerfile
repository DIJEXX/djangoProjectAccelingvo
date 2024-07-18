FROM python

RUN python -m pip install --upgrade pip

RUN python -m pip install --upgrade wheel

RUN python -m venv .venv

RUN .venv/Scripts/activate

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

#python manage.py makemigrations
#python manage.py migrate
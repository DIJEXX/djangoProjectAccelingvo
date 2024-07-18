FROM python

RUN python -m pip install --upgrade pip

RUN python -m pip install --upgrade wheel

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

#python manage.py makemigrations
#python manage.py migrate
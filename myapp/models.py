from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    language = models.CharField(max_length=10, choices=[('ru', 'Русский'), ('en', 'English')])

    def __str__(self):
        return self.username
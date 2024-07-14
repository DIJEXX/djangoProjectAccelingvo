from datetime import date
from django.conf import settings
from django.db import models
from django import forms


class main(models.Model):
    created_at = models.DateField(default=date.today)


class Message(models.Model):
    text = models.CharField(max_length=500)    
    created_at = models.DateField(default=date.today)    
    main = models.ForeignKey(main, on_delete=models.CASCADE, related_name='main_message_set', default=None, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')    
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')
    

class RegistryUser(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
# Generated by Django 5.0.7 on 2024-07-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('language', models.CharField(choices=[('ru', 'Русский'), ('en', 'English')], max_length=10)),
            ],
        ),
    ]

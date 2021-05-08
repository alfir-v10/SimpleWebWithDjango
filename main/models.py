from django.db import models
from django.utils import timezone
from django import forms
import datetime
#mysitemain123
# Create your models here.
class Person(models.Model):
    first_name = models.CharField('Имя',max_length=200, primary_key=True)
    last_name = models.CharField('Фамилия',max_length=200)
    birthday = models.DateField('День рождение',default=timezone.now(), blank=True)
    address = models.CharField('Электроная почта',max_length=50, blank=True)
    city = models.CharField('Город',max_length=60, blank=True)
    country = models.CharField('Страна',max_length=50, blank=True)
    website = models.URLField('Веб-сайт',blank=True)
    money = (('Бюджет', 'Бюджет'), ('Контракт', 'Контракт'))
    money_field = models.CharField('Форма обучения', max_length=10, choices=money, default= 'Не указано', blank=True)
    sex = (('Мужской', 'Мужской'), ('Женский', 'Женский'))
    sex_field = models.CharField('Пол', max_length=10, choices=sex, default='Не указано', blank=True)

class Perform(models.Model):
    perform = models.ForeignKey(Person, on_delete=models.CASCADE, primary_key=True)
    mathPerf = models.IntegerField('Математика')
    physPerf = models.IntegerField('Физика')
    engPerf = models.IntegerField('Иностранный язык')
    geomPerf = models.IntegerField('Геометрия')
    geogPerf = models.IntegerField('География')

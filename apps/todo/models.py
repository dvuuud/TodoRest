from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    completed = models.BooleanField(default=False, verbose_name='Окончен')
    created = models.DateTimeField(auto_now_add=True)
    

from django.db import models

# Create your models here.
class Learn_class(models.Model):
    classroom = models.CharField("Класс", max_length=20, help_text="Введите цифру и букву", unique=True)
    url = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
        return self.classroom

class Reader(models.Model):
    surname = models.CharField("Фамилия", max_length=200, help_text="Введите фамилию")
    name = models.CharField("Имя", max_length=200, help_text="Введите имя")
    middle_name = models.CharField("Отчество", max_length=200, help_text="Введите отчество(при наличии)", blank=True)
    classroom = models.ForeignKey(Learn_class, on_delete=models.SET_NULL, null=True)
    mail = models.CharField("Почта", max_length=300, unique=True)

    def __str__(self):
        return '%s, %s' % (self.surname, self.name)
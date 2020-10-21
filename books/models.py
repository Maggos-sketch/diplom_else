from django.db import models
from readers.models import Reader
import uuid # Required for unique book instances
from datetime import date

# Create your models here.
class Author(models.Model):
    name = models.CharField("Фамилия и инициалы автора", max_length=300)
    date_of_birth = models.DateField("Дата рождения", null=True, blank=False, default=date.today)
    date_of_death = models.DateField("Дата смерти", null=True, blank=True, default=date.today)

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField("Жанр", max_length=300)
    url = models.SlugField(max_length=300)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Модель, представляющая книгу (но не конкретный экземпляр книги)."""
    title = models.CharField("Название книги", max_length=300)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField("Описание", help_text="Введите небольшое описание о книге")
    genre = models.ManyToManyField(Genre)
    url = models.SlugField(max_length = 250, null = True, blank = True)
    img = models.ImageField(upload_to="books/pic")

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    
    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title

class BookInstance(models.Model): #Для книг которые можно взять из библиотеки    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный идентификатор этой конкретной книги во всей библиотеке")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True, default=date.today)
    send_to = models.ForeignKey(Reader, on_delete=models.SET_NULL, null=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text="Наличие книги")

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.__str__())
    
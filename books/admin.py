from django.contrib import admin
from .models import Author, Genre, Book, BookInstance
# Register your models here.

# Админ класс для описания расположения элементов интерфейса
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'date_of_death')
    fields = ['name', ('date_of_birth', 'date_of_death')] # Для красивого отображения


# Декоратор. он делает то же самое, что и метод admin.site.register()
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') #ManyToManyField напрямую вызывать нельзя

# Регистрируем используя декоратор
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)


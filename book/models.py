from django.db import models


class Book(models.Model):

    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('ROMAN', 'ROMAN'),
        ('DETECTIVE', 'DETECTIVE'),
        ('ADVENTURE', 'ADVENTURE'),
    )

    title = models.CharField('Название книги', max_length=100)
    author = models.CharField('Автор книги', max_length=100)
    description = models.TextField('Описание книги')
    image = models.ImageField('Картинка', upload_to='')
    quantity = models.PositiveIntegerField('Количество страниц')
    genre = models.CharField('Жанр', max_length=100, choices=GENRE)
    link = models.URLField('Ссылка на книгу')
    price = models.PositiveIntegerField('Цена')
    mass = models.PositiveIntegerField('Масса книги в граммах')
    age_limit = models.PositiveIntegerField('Возрастное ограничение')
    created_dates = models.DateTimeField(auto_now_add=True, null=True)
    updated_dates = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class RatingBook(models.Model):

    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_object')
    rate = models.IntegerField('Оценка', choices=RATING)
    comment = models.TextField('Комментарий')
    created_date = models.DateTimeField(auto_now_add=True)

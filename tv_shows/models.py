from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Show(models.Model):
    TYPE_SHOW = (
        ('Спортивная', 'Спортивная'),
        ('Комедиеное', 'Комедиеное'),
        ('Семейное', 'Семейное'),
        ('Детское', 'Детское')
    )
    title = models.CharField(max_length=100, verbose_name='укажите название шоу')
    description = models.TextField(verbose_name='Дайте описание шоу', blank=True)
    image = models.ImageField(upload_to='shows/', verbose_name='добавте фото шоу')
    price = models.PositiveIntegerField(verbose_name='укажите цену',
                                       validators=[MinValueValidator(100),
                                                   MaxValueValidator(3000)])

    genre = models.CharField(max_length=100, choices=TYPE_SHOW)
    author = models.CharField(max_length=100, verbose_name='укажите автора')
    trailer = models.URLField(verbose_name='укажите ссылку на трейлер', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



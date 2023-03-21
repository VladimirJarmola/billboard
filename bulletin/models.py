from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Sticker(models.Model):
    """Модель для хранения объявлений."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    TANK = 'Tanks'
    HEALER = 'Healers'
    DAMAGE_DEALER = 'Damage dealers'
    TRADER = 'Traders'
    GUILD_MASTER = 'Guild masters'
    QUEST_GIVER = 'Quest givers'
    SMITH = 'Smiths'
    TANNER = 'Tanners'
    POTION = 'Potions'
    SPELL_MASTER = 'Spell masters'

    CATEGORY_CHOICES = [
        (TANK, 'Tanks'),
        (HEALER, 'Healers'),
        (DAMAGE_DEALER, 'Damage dealers'),
        (TRADER, 'Traders'),
        (GUILD_MASTER, 'Guild masters'),
        (QUEST_GIVER, 'Quest givers'),
        (SMITH, 'Smiths'),
        (TANNER, 'Tanners'),
        (POTION, 'Potions'),
        (SPELL_MASTER, 'Spell masters')
    ]

    category = models.CharField(
        max_length=14,
        choices=CATEGORY_CHOICES,
        default=TANK,
    )
    datetime_of_creation = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=127)
    text_upload = RichTextUploadingField(blank=True, null=True)

    def get_absolute_url(self):
        """Метод возвращает уникальную ссылку на объявление sticker."""
        return reverse('sticker', args=[str(self.id)])

    def __str__(self):
        """Метод для отображения информации об объекте класса."""
        return f'{self.heading.title()}'


class Ans(models.Model):
    """Модель для хранения откликов на объявления."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    datetime_of_creation = models.DateTimeField(auto_now_add=True)
    text = RichTextField(blank=True, null=True)
    condition = models.BooleanField(default=False)

    def __str__(self):
        """Метод для отображения информации об объекте класса."""
        return f'Response {self.author} - {self.text[:20]}'

    def get_absolute_url(self):
        """Метод возвращает уникальную ссылку на отзыв."""
        return reverse('ans', args=[str(self.id)])

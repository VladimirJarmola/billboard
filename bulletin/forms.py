from django import forms

from .models import Ans, Sticker


class StickerForms(forms.ModelForm):
    """Класс генерирует форму для создания объявления Sticker."""

    class Meta:
        """Указываем какие поля модели Sticker использовать."""

        model = Sticker
        fields = ['category', 'heading', 'text_upload']


class AnsForms(forms.ModelForm):
    """Класс генерирует форму для создания откликов Ans."""

    class Meta:
        """Указываем какие поля модели Ans использовать."""

        model = Ans
        fields = ['text']

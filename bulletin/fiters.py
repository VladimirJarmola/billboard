from django.forms import DateTimeInput
from django_filters import DateTimeFilter, FilterSet

from .models import Ans


class AnsFilter(FilterSet):
    """Набор фильтров для модели Ans."""

    added_after = DateTimeFilter(
        field_name='datetime_of_creation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        """Описываем по каким полям модели будет производиться фильтрация."""

        model = Ans
        fields = {
            'sticker': ['exact'],
            'text': ['icontains'],
        }

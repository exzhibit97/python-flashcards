import django_filters

from FlashcardsWeb.models import Deck


class DeckFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Deck
        fields = ['title', ]

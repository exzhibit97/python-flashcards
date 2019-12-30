from django.contrib import admin

# Register your models here.
from .models import Deck, Card


def push_active(modeladmin, request, queryset):
    rows_updated = queryset.update(is_public=True)
    if rows_updated == 1:
        message_bit = "1 deck was"
    else:
        message_bit = "%s decks were" % rows_updated
    modeladmin.message_user(request, "%s successfully marked as active" % message_bit)


push_active.short_description = "Mark selected decks as active"


class DeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'is_public', 'num_of_cards')
    list_filter = ('is_public',)
    search_fields = ['title']
    actions = [push_active]


class CardAdmin(admin.ModelAdmin):
    pass


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)

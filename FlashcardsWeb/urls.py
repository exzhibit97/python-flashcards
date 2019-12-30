from django.urls import path

from . import views
from .views import DeckCreateView, DeckListView, DeckUpdateView, DeckDeleteView, CardCreateView, DeckDetailView, \
    UserDetailView, CardUpdateView, CardDeleteView, DeckFilteredListView

urlpatterns = [
    path('', views.index, name='home'),
    path('decks/', DeckListView.as_view(), name='decks'),
    path('decks_filtered/', DeckFilteredListView.as_view(), name='decks_filtered'),
    path('decks/create/', DeckCreateView.as_view(), name='deck_create'),
    path('decks/edit/<int:pk>', DeckUpdateView.as_view(), name='deck_edit'),
    path('decks/details/<int:pk>', DeckDetailView.as_view(), name='deck_detail'),
    path('decks/delete/<int:pk>', DeckDeleteView.as_view(), name='deck_delete'),
    path('cards/create/<int:deck_id>', CardCreateView.as_view(), name='card_create'),
    path('cards/edit/<int:deck_id>/<int:pk>', CardUpdateView.as_view(), name='card_edit'),
    path('cards/delete/<int:deck_id>/<int:pk>', CardDeleteView.as_view(), name='card_delete'),
    path('accounts/signup', views.SignUp.as_view(), name='signup'),
    path('accounts/profile/<int:pk>', UserDetailView.as_view(), name='profile'),
]

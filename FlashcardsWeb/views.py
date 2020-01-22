from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .forms import DeckForm, CardForm, SignUpForm
from .models import Deck, Card


def index(request):
    return render(request, 'index.html', context=None)


# def decks(request):
#     qs = Deck.objects.order_by('title').filter(is_public=True)
#     context = {'decks': qs}
#     return render(request, 'deck/deck_list.html', context)

# def createDeck(request):
#     """
#     Renders the form to add new decks to the database
#     """
#     if request.method == 'POST':
#         form = DeckForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/decks')
#     else:
#         form = DeckForm()
#
#     context = {}
#     return render(request, 'deck/deck_form.html', {'form': form})


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    form_class = CardForm
    # form_class.fields["parentDeck"].queryset = Deck.objects.filter(creator=)
    template_name = 'card/card_form.html'

    def get_initial(self):
        form_class = CardForm
        deck_id = get_object_or_404(Deck, id=self.kwargs.get('deck_id'))
        initial_base = super(CardCreateView, self).get_initial()
        initial_base['parentDeck'] = Deck.objects.get(id=deck_id.pk)
        form_class.base_fields["parentDeck"].queryset = Deck.objects.filter(creator=self.request.user)
        return initial_base

    def get_success_url(self):
        deck = get_object_or_404(Deck, id=self.kwargs.get('deck_id'))
        deck_id = str(deck.pk)
        return '/decks/details/' + deck_id


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    template_name = 'card/card_form.html'

    def get_success_url(self):
        user_id = str(self.request.user.id)
        return '/accounts/profile/' + user_id


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card

    def get_success_url(self):
        user_id = str(self.request.user.id)
        return '/accounts/profile/' + user_id


class DeckCreateView(LoginRequiredMixin, CreateView):
    model = Deck
    form_class = DeckForm
    template_name = 'deck/deck_form.html'
    success_url = reverse_lazy('decks')

    def form_valid(self, form):
        deck = form.save(commit=False)
        deck.creator = self.request.user
        deck.save()
        return super(DeckCreateView, self).form_valid(form)

    # def get(self, request):
    #     form = DeckForm
    #     form.creator = self.request.user.get_username
    #     return render(self.request, 'deck/deck_form.html', {'form': form})


class DeckListView(ListView):
    paginate_by = 13
    model = Deck
    template_name = 'deck/deck_list.html'
    context_object_name = 'decks'
    success_url = reverse_lazy('decks')

    def get_queryset(self):
        return Deck.objects.all().filter(is_public=True)


class DeckFilteredListView(ListView):
    paginate_by = 13
    model = Deck
    template_name = 'deck/deck_list.html'
    context_object_name = 'decks'

    def get_queryset(self):
        # qs = self.model.objects.all()
        search_query = self.request.GET.get('title_contains')
        print(search_query)
        return Deck.objects.all().filter(title__contains=search_query, is_public=True)


class DeckUpdateView(LoginRequiredMixin, UpdateView):
    model = Deck
    form_class = DeckForm
    template_name = 'deck/deck_form.html'
    success_url = reverse_lazy('decks')

    def form_valid(self, form):
        deck = form.save(commit=False)
        deck.creator = self.request.user
        deck.save()
        return super(DeckUpdateView, self).form_valid(form)


class DeckDetailView(DetailView):
    model = Deck
    template_name = 'deck/deck_detail.html'

    def dispatch(self, *args, **kwargs):
        deck = get_object_or_404(Deck, id=self.kwargs.get('pk'))
        if deck.creator != self.request.user and deck.is_public != True:
            return redirect('decks')
        return super(DeckDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        deck = get_object_or_404(Deck, id=self.kwargs.get('pk'))
        cards = deck.card_set.all()
        card = cards.first()
        context = super(DeckDetailView, self).get_context_data(**kwargs)
        if 'card' in self.request.GET:
            card = get_object_or_404(Card, id=self.request.GET['card'])
        context['card'] = card
        return context


class DeckDeleteView(LoginRequiredMixin, DeleteView):
    model = Deck
    success_url = reverse_lazy('decks')


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_profile_view.html'

    def get_context_data(self, **kwargs):
        decks = Deck.objects.filter(creator=self.request.user)
        context = super(UserDetailView, self).get_context_data(**kwargs)

        context['decks'] = decks
        return context

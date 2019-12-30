from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from FlashcardsWeb.models import Deck, Card


class DeckForm(forms.ModelForm):
    title = forms.CharField(max_length=40, required=True, help_text='Field is required. Max 40 characters.')
    description = forms.CharField(max_length=50, required=False, help_text='Optional field. Max 50 characters.')
    is_public = forms.BooleanField(required=False,
                                   help_text="Optional field. Tick if you want to publish your deck, can be changed "
                                             "later.")

    class Meta:
        model = Deck
        fields = ['creator', 'title', 'description', 'is_public']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save deck'))


class CardForm(forms.ModelForm):
    front = forms.CharField(max_length=30, required=False, help_text='Field is required. Max 30 characters.')
    back = forms.CharField(max_length=30, required=False, help_text='Optional field. Max 30 characters.')
    usageExample = forms.CharField(max_length=80, required=False, help_text='Optional field. Max 80 characters.')

    class Meta:
        model = Card
        fields = ['parentDeck', 'front', 'back', 'usageExample']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save card'))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

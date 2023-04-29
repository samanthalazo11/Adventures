from django.forms import ModelForm
from .models import Restauraunts, Excursions


class RestaurauntsForm(ModelForm):
    class Meta:
        model = Restauraunts
        fields = ('name', 'location', 'description')

class ExcursionsForm(ModelForm):
    class Meta:
        model = Excursions
        fields = ('name', 'price', 'description')
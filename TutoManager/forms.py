# Created by Mateusz at 03.03.2022
from django.forms import ModelForm, TextInput, DateTimeField
from django.utils import timezone

from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'date', 'price']
        date = DateTimeField(input_formats=["%Y-%m-%d %H:%M"])
        initial = {'date': timezone.now(), 'price': 30}
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'date': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
        }

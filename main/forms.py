from .models import scientist
from django.forms import ModelForm , TextInput


class scientistForm(ModelForm):
    class Meta:
        model=scientist
        fields = ['name','surname']
        widgets = {
            'name': TextInput (attrs={
                'placeholder':"Введите имя",
                'class':"form-control"
            }),
            'surname': TextInput(attrs={
                'placeholder': "Введите фамилию",
                'class': "form-control"
            }),
        }
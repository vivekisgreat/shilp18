from django import forms

from .models import Ca

class CaForm(forms.ModelForm):

    class Meta:
        model = Ca
        fields = ('name', 'email',)

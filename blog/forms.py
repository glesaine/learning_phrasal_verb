from django import forms
from .models import Verb
# from .models import Proposition

class EnterVerbForm(forms.ModelForm):
    class Meta:
        model = Verb
        fields = ('phrasal_verb','meaning','example')

class AskVerbForm(forms.Form):
    proposition = forms.CharField(max_length=100)

class Button(forms.Form):
    pass

# from django import forms
#
# class ContactForm(forms.Form):
#     phrasal_verb = forms.CharField(max_length=100)
#     meaning = forms.CharField(max_length=100)
#     example = forms.CharField(max_length=100)

from django import forms

class NameForm(forms.Form):
    anyword = forms.CharField(max_length=100, label="word")
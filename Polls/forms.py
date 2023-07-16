from django import forms

class WordForm(forms.Form):
    your_word = forms.CharField(widget=forms.TextInput)

class UpperForm(forms.Form):
    upper_word = forms.CharField(widget=forms.Textarea(attrs={'name': 'upper'}))
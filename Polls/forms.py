from django import forms

class WordForm(forms.Form):
    your_word = forms.CharField(widget=forms.TextInput(attrs=
    {
        'placeholder': 'Name', 
         'style': 'position: relative', 
        'class': 'form-word'
     
     }))

class UpperForm(forms.Form):
    upper_word = forms.CharField(widget=forms.Textarea(attrs={'name': 'upper'}))
from django import forms

class WordForm(forms.Form):
    your_word = forms.CharField(required=True,widget=forms.TextInput(attrs=
    {
        'placeholder': 'Name', 
        'style': 'position: relative', 
        'class': 'form-word',}
        ))
    convert_choice = forms.ChoiceField(choices=[('upper', 'Maiscula'), ('lower', 'Minuscula')],
    widget=forms.RadioSelect(attrs={'class': 'convert_choice'})

)
    

# class WordForm(forms.Form):
#     your_word = forms.CharField(max_length=100,required=True)
#     lower_case = forms.BooleanField(required=False, widget=forms.HiddenInput)

# class UpperForm(forms.Form):
#     upper_word = forms.CharField(widget=forms.Textarea(attrs={'name': 'upper'}))

# class NameForm(forms.Form):
#     anyword = forms.CharField(max_length=100, label="word")
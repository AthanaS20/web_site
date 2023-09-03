from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import WordForm
import json




# Create your views here.

@csrf_exempt
def word_conversion(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['your_word']
            convert_choice = form.cleaned_data['convert_choice']

            if convert_choice == 'lower':
                word = word.lower()
            elif convert_choice == 'capitalize':
                word = word.capitalize()
            else:
                word = word.upper()

            json_pretty = json.dumps(word)
            context = {
                'form': form,
                'json_pretty': json_pretty
            }
            return render(request, 'upper_case_form.html', context)
        else:
             return render(request, 'upper_case_form.html', {'form': form})
        
    else:
        new_word = WordForm()
        return render(request, 'upper_case_form.html', {'form': new_word})
    





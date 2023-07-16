from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import WordForm
from django.http import JsonResponse




# Create your views here.

@csrf_exempt
def word_conversion(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['your_word']
            word = word.upper()
            return JsonResponse({'word': word})
        else:
             return render(request, 'upper_case_form.html', {'form': form})
        
    else:
        new_word = WordForm()
        return render(request, 'upper_case_form.html', {'form': new_word})
    
# def low_word(user_word):
#     if user_word.method == 'POST':
#         word_lower = user_word.POST.get('word_lower')
#         word_conversion_lower = word_lower.lower()
#         return render(user_word, 'upper_case_form.html', {'word_conversion_lower': word_conversion_lower})
#     else:
#         return render(user_word, 'upper_case_form.html')





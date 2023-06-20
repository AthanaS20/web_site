from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from ckeditor.fields import RichTextField



# Create your views here.

# def index(request):
#     return HttpResponse('CONVERSOR DE PALAVRAS')

@csrf_exempt
def word_conversion(user_word):
    if user_word.method == 'POST':
        word = user_word.POST.get('word')
        word_conversion = word.upper()
        return render(user_word, 'upper_case_form.html', {'word_conversion': word_conversion})
    
    if user_word.method == 'POST':
        word_lower = user_word.POST.get('word_lower')
        word_conversion_lower = word_lower.lower()
        return render(user_word, 'upper_case_form.html', {'word_conversion_lower': word_conversion_lower})
    else:
        return render(user_word, 'upper_case_form.html')
    

 





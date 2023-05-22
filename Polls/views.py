from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

# def index(request):
#     return HttpResponse('CONVERSOR DE PALAVRAS')

@csrf_exempt
def word_conversion(user_word):
    if user_word.method == 'POST':
        word = user_word.POST.get('word')
        word_conversion = word.upper()
        return JsonResponse({'word_conversion': word_conversion})
    else:
        return render(user_word, 'upper_case_form.html')
    

        





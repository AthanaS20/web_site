from . import views
from django.urls import path
from .views import word_conversion

urlpatterns = [
        path('uppercase/', word_conversion, name='word_conversion'),
]

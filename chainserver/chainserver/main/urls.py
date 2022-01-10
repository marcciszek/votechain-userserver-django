from django.urls import path, register_converter
from . import views

app_name = 'main'

urlpatterns = [
    path('block/',
         views.block,
         name='block'),
]

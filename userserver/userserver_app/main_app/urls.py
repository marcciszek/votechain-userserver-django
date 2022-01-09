from django.urls import path, register_converter
from . import views
from django.shortcuts import redirect

app_name = 'main_app'

urlpatterns = [
    path('', lambda request: redirect('voting/')),
    path('test/',
         views.test,
         name='test'),
    path('voting/',
         views.voting,
         name='voting'),
    path('sendvote/',
         views.sendvote,
         name='sendvote'),
]

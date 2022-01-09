from django.urls import path, register_converter
from . import views

app_name = 'main_app'

urlpatterns = [
    path('test/',
         views.test,
         name='test'),
    path('voting/',
             views.voting,
             name='voting'),
]
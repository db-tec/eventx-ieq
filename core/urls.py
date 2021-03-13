from django.urls import path
from .views import index, fazer_inscricao

urlpatterns = [
    path('', index, name='index'),
    path('inscricao/', fazer_inscricao, name="fazer_inscricao")
]
from django.urls import path
from .views import index, inscricao

urlpatterns = [
    path('', index, name='index'),
    path('inscricao/', inscricao, name="inscricao")
]
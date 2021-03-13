from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Evento, Inscricao
from .forms import EventoForm, InscricaoForm


def index(request):
    context = {
        'eventos': Evento.objects.all()
    }
    return render(request,'index.html', context)

def fazer_inscricao(request):
    form = InscricaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'inscricao.html', {'form': form})

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

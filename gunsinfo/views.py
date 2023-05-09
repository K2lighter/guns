from django.shortcuts import render
from django.views.generic import DetailView, UpdateView

from .models import *


def index(request):
    data = {
        'main': ['О сайте', "Добавить статью", "Обратная связь"],
        'title': 'Добро пожаловать в мир Airsoft'
    }
    return render(request, 'gunsinfo/index.html', data)


class GunsDetailView(DetailView):
    model = Pistol
    template_name = 'gunsinfo/pistol_detail.html'
    context_object_name = 'pistol'


def pistol(request):
    pistols = Pistol.objects.order_by('title')
    return render(request, 'gunsinfo/pistol.html', {'pistols': pistols, 'title': 'Информация о пистолетах'})

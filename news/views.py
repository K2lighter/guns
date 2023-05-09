from django.shortcuts import render, redirect
from .models import News

from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = News.objects.order_by('title')
    return render(request, 'news/news.html', {'news': news, 'title': 'Свежие оружейные новости'})


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_view.html'
    context_object_name = 'news'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/create.html'
    # fields = ['title', 'anons', 'text', 'date']

    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'news/news_delete.html'



def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неправильная форма'
    form = NewsForm()
    data = {"form": form, 'title': 'Форма по добавлению статьи', 'error': error}
    return render(request, 'news/create.html', data)

from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, HttpResponse, redirect
from .models import Women

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h2>Cats: {catid}</h2>')


def archive(request, year):
    if int(year) > 2020:
        # raise Http404()
        return redirect('home')
    return HttpResponse(f'<h2>Archive: {year}</h2>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h2>')

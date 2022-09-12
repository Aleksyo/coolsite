from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, HttpResponse, redirect
from .models import Women

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    posts = Women.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'}

    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h2>Cats: {catid}</h2>')


def addpage(request):
    return HttpResponse('Добавить страницу')


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Вход')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id={post_id}')


def archive(request, year):
    if int(year) > 2020:
        # raise Http404()
        return redirect('home')
    return HttpResponse(f'<h2>Archive: {year}</h2>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h2>')

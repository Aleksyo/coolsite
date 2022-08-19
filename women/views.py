from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse('<h1>Main</h1>')


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

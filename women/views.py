from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import *
from .models import Women, Category

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


# def index(request):
#     posts = Women.objects.filter(is_published=True)
#     context = {'posts': posts,
#                'title': 'Главная страница',
#                'cat_selected': 0,
#                }
#     return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Women.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat.slug,
    }
    return render(request, 'women/post.html', context=context)


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat.slug
        return context


# def show_category(request, cat_slug):
#     posts = Women.objects.filter(cat__slug=cat_slug, is_published=True)
#
#     if not len(posts):
#         raise Http404
#
#     context = {'posts': posts,
#                'title': 'Отображение по рубрикам',
#                'cat_selected': cat_slug,
#                }
#     return render(request, 'women/index.html', context=context)


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Вход')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h2>')

# def archive(request, year):
#     if int(year) > 2020:
#         # raise Http404()
#         return redirect('home')
#     return HttpResponse(f'<h2>Archive: {year}</h2>')

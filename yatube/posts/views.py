from django.shortcuts import render, get_object_or_404
from .models import Post, Group
# from django.http import HttpResponse
# Create your views here.
# Главная страница


def index(request):
    template = 'posts/index.html'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию 
    # (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    # # Словарь с данными принято называть context
    context = {
        'posts': posts,
    }
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    # Словарь с данными принято называть context
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
    # return HttpResponse(('Cтраница, на которой будут посты,'
    #                      f'для группы под названием {slug}.'))

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
    }
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
    }
    return render(request, template, context)
    # return HttpResponse(('Cтраница, на которой будут посты,'
    #                      f'для группы под названием {slug}.'))

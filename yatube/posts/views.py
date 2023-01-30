from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template)
    # return HttpResponse(('Cтраница, на которой будут посты,'
    #                      f'для группы под названием {slug}.'))

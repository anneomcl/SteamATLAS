from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from polls import sql_handler

# Create your views here.
from polls.models import Game


def index(request):
    latest_game_list = Game.objects.all()

    context = {'list': latest_game_list,
                            }

    if(request.GET.get('Recommend')):
        sql_handler.recFunc()
        context['name'] = sql_handler.name
        return render(request, 'polls/index.html', context)

    if(request.GET.get('Delete')):
        sql_handler.deleteFunc(request.GET.get('deleteBox'))
        return render(request, 'polls/index.html', context)

    if(request.GET.get('Insert')):
        sql_handler.insertFunc(request.GET.get('insertBox'), request.GET.get('insertDesc'))
        return render(request, 'polls/index.html', context)

    if(request.GET.get('Search')):
        sql_handler.searchFunc(request.GET.get('searchBox'))
        context['name'] = sql_handler.name
        context['image'] = sql_handler.image
        price = "$ " + str(sql_handler.price[0])
        context['price'] = price
        context['description'] = sql_handler.description[0]
        context['tags'] = sql_handler.tags[0]
        return render(request, 'polls/index.html', context)

    if(request.GET.get('Update')):
        sql_handler.updateFunc(request.GET.get('updateName'), request.GET.get('updateDesc'))
        return render(request, 'polls/index.html', context)








    return render(request, 'polls/index.html', context)

def detail(request, app_ID):
    game = get_object_or_404(Game, pk=app_ID)
    return render(request, 'polls/detail.html', {'game': game})



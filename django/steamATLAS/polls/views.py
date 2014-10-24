from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from polls import testerCode

# Create your views here.
from polls.models import Game


def index(request):
    latest_game_list = Game.objects.all()
    context = {'latest_game_list': latest_game_list,
               'x' : testerCode.x,}

    if(request.GET.get('Delete')):
        testerCode.deleteFunc(request.GET.get('deleteBox'))
        return render(request, 'polls/index.html', context)

    if(request.GET.get('Insert')):
        testerCode.insertFunc(request.GET.get('insertBox'), request.GET.get('insertDesc'))
        return render(request, 'polls/index.html', context)

    if(request.GET.get('Search')):
        testerCode.x=testerCode.searchFunc(request.GET.get('searchBox'))
        return render(request, 'polls/index.html', context)


    if(request.GET.get('Update')):
        testerCode.updateFunc(request.GET.get('updateName'), request.GET.get('updateDesc'))
        return render(request, 'polls/index.html', context)








    return render(request, 'polls/index.html', context)

def detail(request, app_ID):
    game = get_object_or_404(Game, pk=app_ID)
    return render(request, 'polls/detail.html', {'game': game})



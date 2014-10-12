from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

# Create your views here.
from polls.models import Game


def index(request):
    latest_game_list = Game.objects.all()
    context = {'latest_game_list': latest_game_list}
    return render(request, 'polls/index.html', context)

def detail(request, app_ID):
    game = get_object_or_404(Game, pk=app_ID)
    return render(request, 'polls/detail.html', {'game': game})
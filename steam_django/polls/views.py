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
'''
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
'''
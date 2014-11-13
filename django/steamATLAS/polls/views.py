from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from polls import sql_handler
from django.views.decorators.csrf import csrf_exempt
from polls.models import Game
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def recommend(request, tag):
    context = {'game_ID' : tag}
    return render(request, 'polls/recommend.html', context)

@csrf_exempt
def tag_results(request):
    selected_tags = request.POST.get('choice', False)
    context =  {'selected_tags' : selected_tags}
    tag_list = request.POST.getlist('choice')
    context['post'] = tag_list
    #recommendation algorithm
    #To-Do: Use tag_list (list of tags)
    # SQL query to find array of games with all or most tags in selected_tags
    # for now, select one game at random, return its ID in the data variable below
    data = str(request.POST.getlist('choice')[0])
    return HttpResponseRedirect(reverse('polls:game_recommended', kwargs = {'tag' : data}))

@csrf_exempt
def index(request):
    latest_game_list = Game.objects.all()

    context = {'list': latest_game_list,}

    if(request.GET.get('Recommend')):
        sql_handler.recFunc()
        context['name'] = sql_handler.name
        #request_data = request.POST
        #context['selectTags']= request_data
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



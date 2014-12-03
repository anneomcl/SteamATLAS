from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from polls import sql_handler
from django.views.decorators.csrf import csrf_exempt
from polls.models import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls import recalgo
from django.db import connection

# Create your views here.

def recommend(request, tag):
    dataToDisplay=[]
    appendRow=[]
    tester = connection.cursor()
    tester.execute('SELECT name, description, price, score, image  FROM polls_GameResults WHERE 1=1 ')
    for row in tester:
        appendRow.append(row[0])
        appendRow.append(row[1])
        appendRow.append(row[2])
        appendRow.append(row[3])
        appendRow.append(row[4])
        dataToDisplay.append(appendRow)
        appendRow=[]


    context = {'game_ID' : dataToDisplay}
    return render(request, 'polls/recommend.html', context)

@csrf_exempt
def tag_results(request):
    tag_list = request.POST.getlist('choice')
    username = request.POST.get('user')

    global_tag_list = ["batman", "action"]
    tag_list_bool = []
    i = 0
    for tag in global_tag_list:
        if tag in tag_list:
            tag_list_bool.insert(i, 1)
        else:
            tag_list_bool.insert(i, 0)
        i+=1
    sql_handler.gameFinder(tag_list)
    recommended_games=[1530, 10, 30, 1002] #= recalgo.algorithm(tag_list)

    '''print(tag_list)
    print(username)
    print(global_tag_list)
    print(tag_list_bool)'''

    data = '440'

    tester = connection.cursor()
    tester2 = connection.cursor()
    tester.execute("DELETE FROM polls_GameResults WHERE 1==1")

    for eachID in recommended_games:
        tester.execute('SELECT name, description, price, score, image  FROM polls_Game WHERE app_ID=%s ', [eachID])
        for row in tester:
            tester2.execute('INSERT into polls_GameResults (name, description, price, score, image, app_ID) VALUES(%s, %s, %s, %s, %s, %s)', [row[0], row[1], row[2], row[3], row[4], eachID])
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



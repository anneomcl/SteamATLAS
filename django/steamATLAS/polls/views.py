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
@csrf_exempt
def done(request):

    return HttpResponse('FAIL!!!!!')

@csrf_exempt
def recommend(request):

    username=0
    dataToDisplay=[]
    appendRow=[]

    tester = connection.cursor()
    tester.execute('SELECT name, description, price, score, image, app_ID, steamID, tag_list  FROM polls_GameResults2 WHERE 1=1 ')
    print("this happens")
    for row in tester:
        appendRow.append(row[0])
        appendRow.append(row[1])
        appendRow.append(row[2])
        appendRow.append(row[3])
        appendRow.append(row[4])
        appendRow.append(row[5])
        username=row[6]
        dataToDisplay.append(appendRow)
        appendRow=[]
        tagliststr=row[7]

    tag_bools=[]
    for elem in ((tagliststr.strip('[')).strip(']')).split(','):
        tag_bools.append(float(elem))
    for x in range(0,4):
        tag_bools.append(1)
    print(tag_bools)
    if request.method == 'POST':

        if 'likes' in request.POST:

            likes = request.POST['likes']
            likes = likes.split(',')
            games_and_likes = {}
            i=0
            for item in dataToDisplay:
                if i < len(likes):
                    games_and_likes[str(item[5])] = likes[i]
                    i+=1
            #print(games_and_likes)
            if username !=0:
                anotherList=recalgo.mlAlgo(games_and_likes, username, tag_bools)

                tester3 = connection.cursor()
                tester4 = connection.cursor()
                tester3.execute("DELETE FROM polls_GameResults2 WHERE 1==1")

                for eachID in anotherList:
                    print("DONE")
                    tester3.execute('SELECT name, description, price, score, image, app_ID  FROM polls_Game WHERE app_ID=%s ', [eachID])
                    for row in tester3:
                        print("DONE22222")
                        tester4.execute('INSERT into polls_GameResults2 (name, description, price, score, image, app_ID, steamID, tag_list) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', [row[0], row[1], row[2], row[3], row[4], eachID, username, str(tag_bools)])







            else:
                print('ERROR')
        #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {'game_ID' : dataToDisplay}



    return render(request, 'polls/recommend.html', context)


@csrf_exempt
def recommend2(request):
    print(request.GET.get())
    return HttpResponseRedirect(reverse('polls:game_recommended3'))

@csrf_exempt
def recommend3(request):
    print(request.GET.get('Submit'))
    #return redirect('polls:index')


@csrf_exempt
def tag_results(request):
    tag_list = request.POST.getlist('choice')
    username = request.POST.get('user')


    #tag_list=['war', 'shoot', 'singleplayer' ]
    #global_tag_list = ["batman", "action"]

    '''
          'multiplayer',
          'singleplayer',
          'war',
          'fight',
          'zombies',
          'shoot',
          'rpg',
          'sci-fi',
          'puzzle',
          'manage',
          'economy',
          'simulate',
          'action'
          '''
    lower_list=[]
    for elem in tag_list:
        lower_list.append(elem.lower())

    tag_list_bool = []
    i = 0
    for tag in sql_handler.global_tag_list:
        if tag.lower() in lower_list:
            tag_list_bool.insert(i, 1)
        else:
            tag_list_bool.insert(i, 0)
        i+=1
    #sql_handler.gameFinder(tag_list)
    #print(tag_list_bool)
    recommended_games= recalgo.firstAlgo(tag_list_bool, username)
    tag_list_bool=tag_list_bool[:-4]
    '''print(tag_list)
    print(username)
    print(sql_handler.global_tag_list)
    print(tag_list_bool)'''

    tester = connection.cursor()
    tester2 = connection.cursor()
    tester.execute("DELETE FROM polls_GameResults2 WHERE 1==1")

    for eachID in recommended_games:
        tester.execute('SELECT name, description, price, score, image, app_ID  FROM polls_Game WHERE app_ID=%s ', [eachID])
        for row in tester:
            tester2.execute('INSERT into polls_GameResults2 (name, description, price, score, image, app_ID, steamID, tag_list) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', [row[0], row[1], row[2], row[3], row[4], eachID, username, str(tag_list_bool)])
    return HttpResponseRedirect(reverse('polls:game_recommended'))

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



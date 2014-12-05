import hashlib
from polls.models import *
from django.db import connection
import os
from random import randint
from polls import craw



#rev TODO
'''

bugs
achievements
like and dislike arrays....check with Anne
add appID from player info to db for parsing

'''



def recFunc():
    global name
    global image
    global description
    global price
    global app_id
    global tags

    tester = connection.cursor()
    tester.execute("SELECT name FROM polls_Game ORDER BY RANDOM() LIMIT 1")
    y = tester.fetchone()
    name = y[0]

def insertFunc(a, b):
    tester = connection.cursor()
    tester.execute("INSERT INTO polls_Game (name, description) VALUES (%s, %s)", [a, b])
    return a

def deleteFunc(a):
    tester = connection.cursor()
    tester.execute("DELETE FROM polls_Game Where name=%s", [a])
    return a

def searchFunc(a):
    global name
    global image
    global description
    global price
    global app_id
    global tags

    name = a

    tester = connection.cursor()
    tester.execute("SELECT image FROM polls_Game Where name = %s", [a])
    x = tester.fetchone()
    image = x[0]

    tester.execute("SELECT price FROM polls_Game Where name=%s", [a])
    price = tester.fetchone()

    tester.execute("SELECT description FROM polls_Game Where name=%s", [a])
    description = tester.fetchone()

    tester.execute("SELECT app_id FROM polls_Game Where name=%s", [a])
    app_id = tester.fetchone()

    tester.execute("SELECT tags FROM polls_Game Where name=%s", [a])
    tags = tester.fetchone()

def updateFunc(a, b):
    tester = connection.cursor()
    tester.execute("UPDATE polls_Game SET description=%s WHERE name=%s", [b, a])


def gameFinder(tag_list):

    #print("---------------------------------------------------------")
    #print(tag_list[0])
    global name
    global image
    global description
    global price
    global app_id
    global tags
    result_list=[]
    tester = connection.cursor()
    if(tag_list):
        queryMaker="SELECT name FROM polls_Game WHERE"


        for tag in tag_list:
            queryMaker=queryMaker+" tags LIKE \"%"+tag+"%\" and"
            #(tag)
            #tester.execute("SELECT name FROM polls_Game WHERE tags= ?", [tag])
        queryMaker=queryMaker+" 1=1"
        print(queryMaker)

         #tester.execute("SELECT name FROM polls_Game WHERE tags LIKE \"%action%\" and tags LIKE \"%batman%\" and tags LIKE \"%tech%\" and 1=1")
        print("@@@@@@@@@@@@@@@@@@@@@")
        tester.execute(queryMaker)
        for row in tester:
            #print(str(row[0]))
            result_list.append(str(row[0]))
        #print(result_list)
        print("@@@@@@@@@@@@@@@@@@@@@")


    print("-------------------------------------------------------")
    tester.close()

    gamesOwnedArray(76561198039606370)
    allGamesArray()
    craw.getInfo(240760)

    return

def dictGameArray(likeDict):
    returnArray=[]
    tester = connection.cursor()
    tester2 = connection.cursor()
    tester.execute("SELECT app_ID FROM polls_Game WHERE 1=1")
    x=0
    #print("@@@@@@@@@@@@@@@fjkasl;fjdklsa;jfdklas;jdflk;asjfkla;dsjfl;asjflka;sfs@@@@@@")
    for key, value in likeDict.items():
        returnArray.append([])
        #print(key)
        returnArray[x].append(key)

        try:
            tester2.execute("SELECT tags, score, app_ID FROM polls_Game WHERE app_ID=%s", [key])
            for row2 in tester2:
                if len(returnArray[x]) < 2:
                    #print(row2[0])
                    for elem in tagChecker(row2[0]):
                        returnArray[x].append(elem)
                    for elem in scoreSplitter(int(row2[1])):
                        returnArray[x].append(elem)
        except:
            print("missing game:")

        if value == 'like':
            returnArray[x].append(1)
        elif value == 'dislike':
            returnArray[x].append(-1)

        #print(returnArray[x])

        x=x+1

    #print(returnArray)
    #print('\n')
    #print(len(returnArray))
    #print("@@@@@@@@@@@@@@@@@@@@@")
    return returnArray




def allGamesArray():
    returnArray=[]
    tester = connection.cursor()
    tester2 = connection.cursor()
    tester.execute("SELECT app_ID FROM polls_Game WHERE 1=1")
    x=0
    #print("@@@@@@@@@@@@@@@@@@@@@")
    for row in tester:
        returnArray.append([])
        #print(row[0])
        returnArray[x].append(row[0])

        try:
            tester2.execute("SELECT tags, score, app_ID FROM polls_Game WHERE app_ID=%s", [row[0]])
            for row2 in tester2:
                if len(returnArray[x]) < 2:
                    #print(row2[0])
                    for elem in tagChecker(row2[0]):
                        returnArray[x].append(elem)
                    for elem in scoreSplitter(int(row2[1])):
                        returnArray[x].append(elem)
        except:
            print("missing game:")

        #print(returnArray[x])

        x=x+1

    #print(returnArray)
    #print('\n')
    #print(len(returnArray))
    #print("@@@@@@@@@@@@@@@@@@@@@")
    return returnArray


def listOfFriends(steam_id):
    friendsList=[]
    tester = connection.cursor()
    print(steam_id)
    tester.execute("SELECT friends FROM polls_Player WHERE steamID= %s", [steam_id])
    for row in tester:
        text=row[0].split(',')
        #print(text)
    for elem in text:
        if len(elem) >= 17:
            friendsList.append(elem)
    return friendsList


def gamesOwnedArray(steam_id):
    returnArray=[]
    tester = connection.cursor()
    tester2 = connection.cursor()
    tester.execute("SELECT appID FROM polls_Owns WHERE steamID=%s", [steam_id])
    x=0
    #print("@@@@@@@@@@@@@@@@@@@@@")
    for row in tester:
        returnArray.append([])
        #print(row[0])
        returnArray[x].append(row[0])

        try:
            tester2.execute("SELECT tags, score FROM polls_Game WHERE app_ID=%s", [row[0]])
            for row2 in tester2:
                if len(returnArray[x]) < 2:
                    #print(row2[0])
                    for elem in tagChecker(row2[0]):
                        returnArray[x].append(elem)
                    for elem in scoreSplitter(int(row2[1])):
                        returnArray[x].append(elem)
        except:
            print("missing game:")

        returnArray[x].append(1)
        #print(returnArray[x])

        x=x+1

    #print(returnArray)
    #print("@@@@@@@@@@@@@@@@@@@@@")
    return returnArray


TagsEnum=['multiplayer',
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
        ]

def tagChecker(tagString):

    listOfTags=[]

    for s in TagsEnum:
        if s.lower() in tagString.lower():
            listOfTags.append(1)
        else:
            listOfTags.append(0)

    return listOfTags


def scoreSplitter(score):
    scoreList=[]

    if 80<= score <=100:
        scoreList.append(1)
    else:
        scoreList.append(0)
    if 70<= score <=80:
        scoreList.append(1)
    else:
        scoreList.append(0)
    if 50<= score <=70:
        scoreList.append(1)
    else:
        scoreList.append(0)
    if 0<= score <=50:
        scoreList.append(1)
    else:
        scoreList.append(0)

    return scoreList
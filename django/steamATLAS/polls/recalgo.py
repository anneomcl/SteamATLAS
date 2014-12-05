__author__ = 'RR'

from polls import newLearn
from polls import sql_handler
from polls import craw
from django.db import connection
import numpy as np

def firstAlgo(tagsList, username):

    returnArray=[]

    data1=sql_handler.gamesOwnedArray(username)
    friends=sql_handler.listOfFriends(username)
    #print(friends)
    data2=[]
    for friend in friends:
        for elem in sql_handler.gamesOwnedArray(friend):
            data2.append(elem)
    #print(data2)


    totalVector=[]
    for elem in data1:
        if len(elem) >3:
            totalVector.append(elem)
    for elem in data2:
        if len(elem) >3:
            #print(elem)
            totalVector.append(elem)
    #print(totalVector)
    sumArray=[0 for x in range(len(totalVector[0]))]
    #print(sumArray)
    for elem in totalVector:
        #print(elem)
        sumArray=np.add(sumArray, elem)
    sumArray=sumArray/len(sql_handler.global_tag_list)
    sumArray=sumArray[1:(len(sumArray)-1)]
    #print(sumArray)
    for x in range(0,4):
        tagsList.append(1)
    #print(tagsList)
    newSumArray=[]

    for x in range(0, len(tagsList)):
        newSumArray.append(tagsList[x]*sumArray[x])
    sumArray=newSumArray
    #print(sumArray)
    gameList={}
    for elem in sql_handler.allGamesArray():
        gameList[elem[0]]=np.dot(elem[1:len(elem)], sumArray)
    #for key, value in gameList.items():
        #print(key, value)

    sortedList= sorted(gameList.items(), key=lambda x:x[1])
    #for elem in sortedList:
        #print(elem)
    for elem in reversed(sortedList):
        #print(elem[0])
        returnArray.append(elem[0])
    print(returnArray[0:10])
    #print('-----------------------------------')
    #for elem in returnArray:
        #print(elem)
    '''
    f = open('tagsList', 'w')
    for elem in sql_handler.listOfTags():
        f.write(str(elem)+'\n')
    f.close()
    print(sql_handler.listOfTags())
    '''
    return returnArray[0:10]


def mlAlgo(likeDict, username, tags_list):
    print(tags_list)
    topTenGames=[]

    L=[]
    w=[]
    theta=0.0



    for elem in sql_handler.gamesOwnedArray(username):
        L.append(elem)
    for elem in sql_handler.dictGameArray(likeDict):
        L.append(elem)
    '''
    L = [
    [29160, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [33230, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [30, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, -1],
    [70, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, -1]
    ]
    '''
    '''
    f = open('datafile8', 'w')
    for elem in L:
        f.write(str(elem)+'\n')
    f.close()
    '''
    #w=[1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0]


    tester = connection.cursor()

    tester.execute("SELECT weight, theta FROM polls_PlayerWeights WHERE steamID=%s", [username])
    for row in tester:
        try:
            w=[]
            for elem in ((row[0].strip('[')).strip(']')).split(','):
                w.append(float(elem))
            theta=float(row[1])
        except:
            print('error in getting w')
            w=[]
            theta=0.0
    #print(w, theta)
    if len(w) == (len(L[0])-2):
        #print(w, theta)
        pass
    else:
        w = [0.0] * (len(L[0]) - 2)
        theta=0.0
        try:
            tester.execute("Update polls_PlayerWeights set weight=%s where steamID=%s ", [str(w), username])
        except Exception as e:
            print('update weight')
            print(e)

    if theta !=0.0:
        combine = newLearn.startLearn(L, w, theta)
        #print(combine)
        try:
            tester.execute("Update polls_PlayerWeights set theta=%s where steamID=%s ", [combine[-1], username])
        except Exception as e:
            ('update theta MAIN')
            print(e)
        try:
            tester.execute("Update polls_PlayerWeights set weight=%s where steamID=%s ", [str(combine[: len(combine)-1]), username])
        except Exception as e:
            print('update weight MAIN')
            print(e)
    else:
        combine = newLearn.startLearn(L, w, theta)
        #print(combine)

        try:
            tester.execute("Update polls_PlayerWeights set theta=%s where steamID=%s ", [combine[-1], username])
        except Exception as e:
            ('update theta SECOND')
            print(e)
        try:
            tester.execute("Update polls_PlayerWeights set weight=%s where steamID=%s ", [str(combine[: len(combine)-1]), username])
        except Exception as e:
            print('update weight SECOND')
            print(e)
    #print(combine)
    gameList={}
    for elem in sql_handler.allGamesArray():
        #print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        #print(tags_list)

        #print(elem)
        newelem=[]
        newelem.append(elem[0])
        for x in range(0, len(tags_list)):
            newelem.append(tags_list[x]*elem[x+1])
        #print(newelem)


        gameList[elem[0]]=newLearn.predict(combine[: len(combine)-1], newelem, combine[-1])

    sortedList= sorted(gameList.items(), key=lambda x:x[1])
    for elem in reversed(sortedList):
        #print(elem[0])
        topTenGames.append(elem[0])
    print(topTenGames[0:10])

    tester3 = connection.cursor()
    tester4 = connection.cursor()
    #tester3.execute("DELETE FROM polls_GameResults2 WHERE 1==1")
    return topTenGames[0:10]
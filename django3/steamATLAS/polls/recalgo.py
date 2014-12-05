__author__ = 'RR'

from polls import learn
from polls import sql_handler
from polls import craw
import numpy as np

def firstAlgo(tagsList, username):

    returnArray=[]

    data1=sql_handler.gamesOwnedArray(username)
    friends=sql_handler.listOfFriends(username)
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
    sumArray=sumArray/11
    sumArray=sumArray[1:(len(sumArray)-1)]

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
    return returnArray[0:10]


def mlAlgo(likeDict, username):
    topTenGames=[]
    print('righ here buddy')
    L=[]
    w=[]
    theta=0
    #print("111111111111111111111111111111111111")
    #print(craw.getInfo(214340))
    #print("111111111111111111111111111111111111")
    for elem in sql_handler.gamesOwnedArray(username):
        L.append(elem)
    for elem in sql_handler.dictGameArray(likeDict):
        L.append(elem)
    print('did we get here?')
    f = open('datafile8', 'w')
    for elem in L:
        f.write(str(elem)+'\n')
    f.close()

    learn.startLearn(L, w, theta)




    return topTenGames
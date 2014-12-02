from polls.models import Game
from django.db import connection
import os



def populateGamesDB():
    pwd = os.path.dirname(__file__)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM polls_Game WHERE 1==1")
    with open(pwd + '/dbData/info') as f:
        for line in f:
            line=line.strip('\n')
            text=line
            text=text.split('|')
            a=int(text[0])
            b=text[1]
            c=int(text[2])
            d=text[3]
            e=text[4]
            f=text[5]

            imageName=str(a)+".jpg"

            try:
                cursor.execute("INSERT INTO polls_Game (app_ID, name, score, tags, price, description) VALUES (%s, %s, %s, %s, %s, %s)", [a, b, c, d, e, f])
            #cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (%i, %i, %s)",[a] ,[b], [c])
            except:
                print("first game db update error")

            try:
                cursor.execute("UPDATE polls_Game SET image= %s WHERE app_ID=%s", [imageName, a])
            except:
                print("image for games db update error")
            #print(a)
           # print(b)
           # print(c)
    cursor.close()
    return

def populateAchievementDB():
    return

def populatePlayerDB():
    return

def populateAchievedDB():
    pwd = os.path.dirname(__file__)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM polls_Achieved WHERE 1==1")
    print("@@@@@@@@@@@INIT@@@@@@@@@@@@@@@")
    print(pwd)
    with open(pwd + '/dbData/achievements') as f:
        for line in f:
            line=line.strip('\n')
            text=line
            text=text.split(':')
            a=int(text[0])
            b=int(text[1])
            c=text[2]

            cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (%s, %s, %s)", [a, b, c])
            #cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (%i, %i, %s)",[a] ,[b], [c])

            #print(a)
           # print(b)
           # print(c)
    cursor.close()
    return

def populateOwns():
    pwd = os.path.dirname(__file__)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM polls_Owns WHERE 1==1")
    print("@@@@@@@@@@@INIT@@@@@@@@@@@@@@@")
    print(pwd)
    with open(pwd + '/dbData/ownedGames') as f:
        for line in f:
            if line != '\n':
                line=line.strip('\n')
                #print(line)
                text=line
                text=text.split(' ')
                a=int(text[0])
                b=int(text[1])
                c=int(text[2])
                d=int(text[3])
                e=float(text[4])

            try:
                #print("hello")
                cursor.execute("INSERT INTO polls_Owns (steamID, appID, recentlyPlaced, totalPlaytime, achievementsPercentage) VALUES (%s, %s, %s, %s, %s)", [a, b, c, d, e])
            except:
                print("Unexpected error:")
            #cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (%i, %i, %s)",[a] ,[b], [c])

            #print(a)
           # print(b)
           # print(c)
    cursor.close()
    return


populateAchievedDB()
populateGamesDB()
populateOwns()
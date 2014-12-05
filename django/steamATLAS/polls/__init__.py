from polls.models import Game
from django.db import connection
from polls import sql_handler
from polls import craw
import os



def populateGamesDB():
    pwd = os.path.dirname(__file__)
    cursor = connection.cursor()
    #cursor.execute("DELETE FROM polls_Game WHERE 1==1")
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
            except Exception as e:
                #print(a)
                #print(e)
                pass

            try:
                cursor.execute("UPDATE polls_Game SET image= %s WHERE app_ID=%s", [imageName, a])
            except:
                print("image for games db update error")
            #print(a)
           # print(b)
           # print(c)
    cursor.close()
    return

def insertGameFromId(appID):
    cursor = connection.cursor()
    cursor.execute("SELECT app_ID FROM polls_Game WHERE app_ID=%s", [appID])
    data=cursor.fetchall()
    if len(data)!= 0:
        print(appID)
        print("already in there")
        return
    data= craw.getInfo(appID)
    print(appID)
    try:
        cursor.execute("INSERT INTO polls_Game (app_ID, name, score, price, tags, description) VALUES (%s, %s, %s, %s, %s, %s)", [data[0], data[1], data[2], data[3], data[4], data[5]])
        #cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (%i, %i, %s)",[a] ,[b], [c])
    except Exception as e:
        print(e)


    return

def populateAchievementDB():
    return

def populatePlayerDB():
    pwd = os.path.dirname(__file__)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM polls_Player WHERE 1==1")
    with open(pwd + '/dbData/userSummary') as f:
        for line in f:
            line=line.strip('\n')
            text=line
            text=text.split('|')
            a=int(text[0])
            b=text[1]
            c=int(text[2])
            d=text[3]
            e=text[4]


            #try:
            cursor.execute("INSERT INTO polls_Player (steamID, displayName, profileURL, friends) VALUES (%s, %s, %s, %s)", [a, b, d, e])

            #cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (%i, %i, %s)",[a] ,[b], [c])
            #except:
            #print("first player db update error")

    cursor.close()
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
    #cursor.execute("DELETE FROM polls_Owns WHERE 1==1")
    print("@@@@@@@@@@@INIT@@@@@@@@@@@@@@@")
    print(pwd)
    print("9999999999999999999999999999999999999999")
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
                if b==320:
                    print('pooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooop')
            try:
                #print("hello")
                cursor.execute("INSERT INTO polls_Owns (steamID, appID, recentlyPlaced, totalPlaytime, achievementsPercentage) VALUES (%s, %s, %s, %s, %s)", [a, b, c, d, e])
            except Exception as e:
                print(e)
            #cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (%i, %i, %s)",[a] ,[b], [c])


            #print("updating owned games now")
            #print(b)
            try:
                insertGameFromId(b)
                #print("poop")
                #insertGameFromId(b)
            except Exception as e:
                print('more interesting error')
                #print(b)
                print(e)


                #print("owns error")
            #print(a)
           # print(b)
           # print(c)
    cursor.close()
    print("9999999999999999999999999999999999999999")
    return



def updateImages():
    tester = connection.cursor()
    tester2 = connection.cursor()
    tester.execute("SELECT app_ID FROM polls_Game WHERE 1=1")

    for row in tester:
        img=craw.getPicture(row[0])
        print(img)
        try:
            tester2.execute("UPDATE polls_Game SET image= %s WHERE app_ID=%s", [img, row[0]])
        except Exception as e:
            print('update image exception')
            print(e)



try:
    #populateAchievedDB()
    #populateGamesDB()
    #populateOwns()
    #updateImages()
    print('something')
except Exception as e:
    print("some rand error")
    print(e)
populatePlayerDB()
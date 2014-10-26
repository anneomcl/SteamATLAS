from polls.models import Game
from django.db import connection
import os

pwd = os.path.dirname(__file__)
cursor = connection.cursor()
cursor.execute("DELETE FROM polls_Achieved WHERE 1==1")
with open(pwd + '/achievements') as f:
    for line in f:
        line=line.strip('\n')
        text=line
        text=text.split(':')
        a=int(text[0])
        b=int(text[1])
        c=text[2]

        cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (%s, %s, %s)", [a, b, c])
        #cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (%i, %i, %s)",[a] ,[b], [c])

        print(a)
        print(b)
        print(c)

#cursor.execute('''INSERT INTO polls_Game (name, app_ID, price, tags, description, image) VALUES ('testgame2', 100, 100, 'testertags', 'testerDescription', None)''')

#a='this is a cool string'

#cursor.execute("INSERT INTO polls_Achieved (steamID, app_ID, name) VALUES (1001, 100, %s)", [a])

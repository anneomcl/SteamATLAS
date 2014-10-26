import hashlib
from polls.models import Game
from django.db import connection
import os
from random import randint


def recFunc():
    global name
    global image
    global description
    global price
    global app_id
    global tags

    x = randint(0,1)
    if(x ==1):
        tester = connection.cursor()
        tester.execute("SELECT name FROM polls_Game Where app_id == 0")
        y = tester.fetchone()
        name = y[0]

    else:
        name = "Nothing"


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




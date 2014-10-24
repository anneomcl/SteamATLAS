import hashlib
from polls.models import Game
from django.db import connection
import os



global x
x="helloTester"
def insertFunc(a, b):
    tester = connection.cursor()
    tester.execute("INSERT INTO polls_Game (name, description) VALUES (%s, %s)", [a, b])
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    return a
def deleteFunc(a):
    tester = connection.cursor()
    tester.execute("DELETE FROM polls_Game Where name=%s", [a])
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    return a
def searchFunc(a):
    tester = connection.cursor()
    tester.execute("SELECT description FROM polls_Game Where name=%s", [a])
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    x=tester.fetchone()
    return x




def updateFunc(a, b):
    tester = connection.cursor()
    tester.execute("UPDATE polls_Game SET description=%s WHERE name=%s", [b, a])
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")




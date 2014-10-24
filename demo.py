import requests
from xml.dom import minidom

URLS = {'GetOwnedGames':'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001', 'GetPlayerAchievements':'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001'}

KEY = 'E2469B841908CBF830EC652B7BAB5D71'

def ownedGames(id):
    info = {'key': KEY, 'steamid': id, 'format': 'xml'}
    url = URLS['GetOwnedGames']
    r = requests.get(url, params=info)
    return r

def achievements(id, app):
    info = {'appid': str(app), 'key': KEY, 'steamid': id}
    url = URLS['GetPlayerAchievements']
    r = requests.get(url, params=info)
    print r.text

def saveXML(id, need):
    if need == 'GetOwnedGames': req = ownedGames(id)
    elif need == 'GetPlayerAchievements': req = achievements(id)
    f = open(need+'.xml', 'w')
    f.write(str(req.text))
    f.close()

def parseXML(fileName):
    xmldoc = minidom.parse(fileName)
    itemlist = xmldoc.getElementsByTagName('appid') 
    res = []
    for i in itemlist:
        res.append(int(i.firstChild.data))
    return res


anneID = '76561198039606370'
saveXML(anneID, 'GetOwnedGames')
#saveXML('76561198039606370', 'GetPlayerAchievements')
appList = parseXML('GetOwnedGames.xml')
print appList
achievements(anneID, 440)

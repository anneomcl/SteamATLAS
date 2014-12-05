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
    ''' only return ascii values string '''
    info = {'appid': str(app), 'key': KEY, 'steamid': id}
    url = URLS['GetPlayerAchievements']
    r = requests.get(url, params=info)
    return r.text.encode('ascii', 'ignore')

def parseAchieve(content):
    ''' not sure of the format; not use re; just simple delete '''
    lines = content.splitlines()
    res = ''
    i = 0
    while i < len(lines) - 1:
        if '"apiname":' in lines[i]:
            finished = lines[i+1].replace('"achieved":', '').strip()
            isDone = 0
            try:
                isDone = int(finished)
            except: pass
            if isDone: 
                achieve = lines[i].replace('\t\t\t\t"apiname": "', '').replace('",', '')
                res += achieve + ','
        i += 1
    return res

def getAchievements(userInfo):
    res = ''
    for id in userInfo:
        for app in userInfo[id]:
            content = achievements(id, app)
            if '"apiname":' in content:
                res += id + ':' + app + ':' + parseAchieve(content) + '\n'
    f = open('achievements', 'w')
    f.write(res)
    f.close()


def getOwnedGames(userInfo):
    ''' for each id, retrieve info from api, parse its xml, and save into file '''
    res = ''
    for id in userInfo:
        res += id + ':'
        req = ownedGames(id)
        xmldoc = minidom.parseString(str(req.text))
        itemlist = xmldoc.getElementsByTagName('appid') 
        for item in itemlist:
            appId = item.firstChild.data
            res += str(appId) + ','
            userInfo[id].append(str(appId))
        res += '\n'
    f = open('ownedGames', 'w')
    f.write(res)
    f.close()

def readinUser():
    ''' readin all steam ids from file '''
    f = open('steamids', 'r')
    userInfo = {}
    for line in f:
        userInfo[line.strip()] = []
    return userInfo

if __name__ == '__main__':
    userInfo = readinUser()
    getOwnedGames(userInfo)
    getAchievements(userInfo)

    

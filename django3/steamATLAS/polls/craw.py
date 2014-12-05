import requests
from bs4 import BeautifulSoup
import urllib.request
import sys


def getInfo(page_id):


    session = requests.session()
    html = session.get("http://store.steampowered.com/app/%s/" % page_id).text
    # Checking if I'm in the check age page (just checking if the check age form is in the html code)
    if ('<form action="http://store.steampowered.com/agecheck/app/%s/"' % page_id) in html:
        post_data = {
            'snr':'1_agecheck_agecheck__age-gate',
            'ageDay':1,
            'ageMonth':'January',
            'ageYear':'1960'
        }
        html = session.post('http://store.steampowered.com/agecheck/app/%s/' % page_id, post_data).text

    res = ''
    soup = BeautifulSoup(html)
    try:
        title = soup.find(class_='apphub_AppName').text.strip()
    except Exception as e:
        pass
    try:
        score = soup.find_all(id='game_area_metascore')[0].text.replace('/100', '').strip()
    except Exception as e:
        pass
        score=70
    try:
        image = soup.find(class_='game_header_image_full')
    except Exception as e:
            pass
    try:
        imgUrl=(image['src'])
    except Exception as e:
        pass

    urllib.request.urlretrieve(imgUrl,'polls/media/'+ str(page_id)+'.jpg')

    price=''
    priceTry = soup.find(class_='discount_final_price')
    if priceTry == None and soup.find(class_='game_purchase_price price'):
        price = soup.find(class_='game_purchase_price price').text.strip()
    else:
        price = priceTry.text.strip()
    desc = soup.find(class_='game_description_snippet').text.strip()
    tags = ''
    for t in soup.find_all(class_='app_tag'):
        tmp = t.text.strip()
        if len(tmp)  > 1: tags += tmp + ','



    res = [page_id, title, score, price, tags, desc]



    '''
    print(page_id)
    print(title)
    print(score)

    print(tags)
    print(price)
    print(str(desc))

    print("000000000000000000000000000000000000000000000000000000000000000000000000000000000    ")
    #print(res.encode('ascii', 'ignore'))'''
    return res



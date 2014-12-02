import scrapy
from bs4 import BeautifulSoup
import urllib

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["store.steampowered.com"]
    start_urls = []
    base = 'http://store.steampowered.com/app/'
    f = open('apps.txt', 'r')
    for line in f.readlines():
        tmp = base + line.strip()
        start_urls.append(tmp)
        print tmp

    def parse(self, response):
        appId = response.url.split("/")[-1].strip()
        soup = BeautifulSoup(response.body)
        res = ''
        title = soup.find_all('title')[0].text
        name = title.replace('on Steam', '').strip()
        score = soup.find_all(id='game_area_metascore')
        print appId, score

        tags = soup.find_all(class_='app_tag')
        tagText = ''
        for t in tags:
            tmp = t.text.strip()
            if len(tmp) > 1:
                tagText += tmp + ','

        price = soup.find(class_='game_purchase_price price').text.strip()
        desc = soup.find(class_='game_description_snippet').text.strip()

        spans = score[0].find_all('span')
        for s in spans: 
            if not s.has_attr('class') and appId:
                res += appId + '|' + name + '|' + s.text + '|' + tagText + '|' + price + '|' + desc + '\n'

                #urllib.urlretrieve('http://cdn.akamai.steamstatic.com/steam/apps/' + appId + '/header.jpg', 'logos/' + appId + '.jpg')

        with open('info', 'a') as f:
            f.write(res)

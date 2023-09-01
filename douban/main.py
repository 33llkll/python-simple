from lxml import etree
import requests
import time
from bs4 import BeautifulSoup
# import pip
import csv

# 爬虫框架
# Scrapy
# PySpider
# Portia
# Beautiful Soup
# Crawley
# selenium
# Python-goose
# Grab

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
}

base_url = 'https://movie.douban.com/top250?start=0&filter='


def get_resp(url):
    resp = requests.get(url=url, headers=header)

    # tree = BeautifulSoup(resp.text,'lxml')

    # ols = tree.find('ol','grid_view')
    # for i in ols.find_all('li'):

    #     title = i.span.get_text()

    #     contents = i.find('p',_class = '')
    #     contents = contents.get_text().strip().split()
    #     director = contents[1]
    #     actress = contents[5]
    #     pub_time = contents[9]
    #     types = "".join(contents[13:])
    #     print(title,director,actress,pub_time,types)
    html = etree.HTML(resp.text)

    title = html.xpath('//*[@id="content"]/div/div[1]/ol/li//a/span[1]/text()')

    director = html.xpath(
        '//*[@id="content"]/div/div[1]/ol/li//div[@class="bd"]/p[1]/text()[1]')

    actress = html.xpath(
        '//*[@id="content"]/div/div[1]/ol/li//div[@class="bd"]/p[1]/text()[1]')

    types = html.xpath(
        '//*[@id="content"]/div/div[1]/ol/li//div[@class="bd"]/p[1]/text()[2]')

    get_write_down(title, director, actress, types)


def get_write_down(title, director, actress, types):

    for i in range(0, len(title)):

        writer.writerow([title[i], director[i].split()[1], actress[i].split()[
                        5], types[i].strip().split('/')[0], types[i].strip().split('/')[2]])
    # pass


if __name__ == '__main__':
    fp = open('writer.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(fp)
    writer.writerow(['title', 'director', 'actress', 'pub_time', 'type'])
    for url in [f'https://movie.douban.com/top250?start={i}&filter=' for i in range(0, 250, 25)]:
        time.sleep(2)
        get_resp(url)
        # print(url)
        # break
    print('over!')

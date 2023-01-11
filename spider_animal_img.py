import urllib.request
from lxml import etree
# 站长素材的动物图片爬取


def Create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/dongwu.html'
    else:
        url = 'https://sc.chinaz.com/tupian/dongwu_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }

    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


def down_load(content):

    tree = etree.HTML(content)

    list_name = tree.xpath('//div[@class="container"]//img/@alt')

    list_src = tree.xpath('//div[@class="container"]//img/@data-original')

    for i in range(len(list_name)):
        name = list_name[i]
        src = list_src[i]
        url = 'https:' + src

        urllib.request.urlretrieve(
            url=url, filename='./animal_img/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input("请输入起始页码"))
    end_page = int(input("请输入结束页码"))

    for page in range(start_page, end_page+1):
        request = Create_request(page)
        content = get_content(request)
        down_load(content)

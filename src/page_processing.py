# coding: utf-8

""" логика обработки страниц и парсинга """

import os
from lxml import html
from urllib2 import urlopen
from urllib import urlretrieve


def get_images_link(url, page):
    """ получаем список ссылок на картинки """
    url = "%s/%d" % (url, page)
    page_tree = html.fromstring(urlopen(url).read())
    images = page_tree.xpath('//div[@class="strip"]/a/img')
    links = [img.attrib['src'] for img in images]
    return links


def save_image(link, dest):
    """ сохраняем картинки на диск """
    urlretrieve(link, dest + '/' + link.split('/')[-1])


def get_page_count(tree):
    """ получаем число страниц с комиксом """
    desc = tree.xpath('//div[@class="description"]')[1].text_content()
    number = [word for word in desc.split() if word.isdigit()][-1]
    return int(number)


def download(url, dest):
    """ основной сценарий """
    if os.path.isdir(dest):
        os.mkdir(dest)    
    main_url_data = urlopen(url).read()
    tree = html.fromstring(main_url_data)
    page_count = get_page_count(tree)
    for page in range(1, page_count + 1):
        for link in get_images_link(url, page):
            save_image(link, dest)


download_dir = os.environ.get('PWD') + '/download'
url = 'http://comicsia.ru/collections/swine'
download(url, download_dir)

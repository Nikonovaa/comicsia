# coding: utf-8

import os
from lxml import html
from urllib2 import urlopen


def get_images_link(url, page):
    return [] 


def get_page_count(tree):
    desc = tree.xpath('//div[@class="description"]')[1].text_content()
    number = [word for word in desc.split() if word.isdigit()][-1]
    return int(number)


def download(url, dest):
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

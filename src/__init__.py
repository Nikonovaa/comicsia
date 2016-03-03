# coding: utf-8
""" качаем свинок """

import os
from page_processing import download

DIR = os.environ.get('PWD') + '/' + os.environ.get('DST', 'download')
MAIN_URL = os.environ.get('URL', 'http://comicsia.ru/collections/swine')


if __name__ == '__main__':
    download(MAIN_URL, DIR)

import pandas as pd
import requests
import os
from datetime import datetime
import logging


class Search():
    def __init__(self, words):
        self.words = words
        self.URL = 'http://dict-co.iciba.com/api/dictionary.php'
        self.API = 'E0F0D336AF47D3797C68372A869BDBC5'
        self.logger = logging.getLogger(__name__)
        self.jsons = []

    def get_respones(self, word):
        try:
            response = requests.get(self.URL + '?key=' + self.API + '&w=' + word+'&type=json')
        except Exception:
            self.logger.error('哎哟,好像出错了')
        return response


    def doSearch(self):
        pathName = './results'
        fileName = datetime.now().strftime('%Y%m%d-%H%M%S')
        for word in self.words:
            resp = self.get_respones(word)
            print(resp.json())
            self.jsons.append(resp.json())



if __name__ == '__main__':
    search = Search(['china', 'japan'])
    search.doSearch()
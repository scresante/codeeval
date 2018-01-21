#!/usr/bin/python3
# this is the thing that generates a new file to work on codeeval
# also download challenges (desc, input, output, etc)

from sys import argv
import os
import argparse
from bs4 import BeautifulSoup as bs
import requests

secrets =
DEBUG = True

class codeEvalChallenge:
    def __init__(self, challenge_number, backup=True):
        url = f'https://www.codeeval.com/browse/{challenge_number}'
        source = requests.get(url)
        parser = 'html.parser' #lxml
        self.soup = bs(source.text, parser)
        if backup:
            self.writeBackup(source.text, challenge_number)
        pass
    def writeBackup(self, data, num):
        save_path = f'ce-backup/{num}.html'
        if not os.path.isdir(save_path):
            os.mkdir('ce-backup')
        with open(save_path, 'w') as f:
            f.writelines(data)
        if DEBUG: print(save_path + ' written')
    def collectData(self):
        self.title = self.soup.h2.text
        pass


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('challenge_number', type=str)
        args = parser.parse_args()
        c = codeEvalChallenge(args.challenge_number)
    except Exception as e:
        # this doesnt catch argument problems, but does catch internet ones
        print('i need an argument for challenge number')
        print(type(e),e)

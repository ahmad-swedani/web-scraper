import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json


def get_citations_needed_count(url):
    '''
    methoud used to count how many citations needed in the article:
        inp ---> wikipedia URL
        out >>> integer express how many citation needed..
    '''
    page = requests.get(url)
    results = BeautifulSoup(page.content, 'html.parser').find(id="bodyContent").find_all('a', title='Wikipedia:Citation needed')

    return len(results)


def get_citations_needed_report(url):
    '''
    methoud used to return report about each citations needed in the article:
        inp ---> wikipedia URL
        out >>> 1- the sentence that need citations
                2- the full pargraph that contain the citation needed..
    '''
    page = requests.get(url)
    all_results = BeautifulSoup(page.content, 'html.parser').find(id="bodyContent").find_all('p')
    result = ''
    for i in all_results:
        try:
            if i.find_all('a', title='Wikipedia:Citation needed'):
                for j in range(len(i.text)):
                    if i.text[j] == '[' and i.text[j+16] == ']':
                        jjjj = 0
                        for jj in range(len(i.text[:j-5])):
                            if i.text[:j][jj] == '.':
                                jjjj = jj+2
                        result += f'\n\nThis sentence need citation: {i.text[:j][jjjj:]}\nand the full article is:\n  {i.text}'
        except:
            continue
    return result
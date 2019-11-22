"""
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

def getArticleLinks(articleURL):
    """
    """
    html = urlopen("http://en.wikipedia.org"+articleURL)
    bso = BeautifulSoup(html)

    return bso.find("div", {"id":"bodyContent"}).findAll("a",
                      href=re.compile("^(/wiki/)((>!:).)*$"))

def wikiArticleParse(article_of_interest):
    """
    """
    random.seed(datetime.datetime.now())
    links = getArticleLinks("/wiki/"+article_of_interest)

    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]

        print(newArticle)
        links = getLinks(newArticle)

pages = set()
def getAllLinks(articlepg):
    """
    """
    global pages
    html = urlopen("http://en.wikipedia.org"+articlepg)
    bso = BeautifulSoup(html)

    for link in bso.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

'''
scrape azlyrics for song lyrics to use as sample data
'''

BASE_URL = "http://www.azlyrics.com"


def get_category_links00(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    band = soup.find("div", "tdata-ext")
    for tbody in band.findAll("tbody"):
        for td in tbody.findAll("td", "tal qx"):
            for a in td.findAll("a"):
                b = str(a["href"])
                get_category_links01("http://www.lyrics.net/" + b)

    # category_links = [BASE_URL + div for div in cont.findAll("div")]


def get_category_links01(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    band = soup.find("div", "tdata-ext")
    for div in band.findAll("div", "clearfix"):
        for h3 in div.findAll("h3", "artist-album-label"):
            for a in h3.findAll("a"):
                b = str(a["href"])
                get_category_links02("http://www.lyrics.net" + b)


def get_category_links02(category_url):
    html = urlopen(category_url).read()
    soup = BeautifulSoup(html, "lxml")
    for div in soup.findAll("div", "tdata-ext"):
        for tbody in div.findAll("tbody"):
            for td in tbody.findAll("td", "tal qx"):
                for a in td.findAll("a"):
                    b = str(a["href"])
                    get_category_links03("http://www.lyrics.net" + b)
        '''
        #for c in div.descendants:
            #print c
        #for br in div.findAll("br"):
         #   print (br.nextSibling)
        '''


def get_category_links03(category_url):
    html = urlopen(category_url).read()
    soup = BeautifulSoup(html, "lxml")
    for div in soup.findAll("div", "clearfix"):
        for pre in div.findAll("pre", "lyric-body"):
            print pre


print_func(get_category_links00("http://www.lyrics.net/artists/A"))

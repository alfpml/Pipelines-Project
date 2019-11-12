import pandas as pd
import re
import numpy as np
import requests
import re
from bs4 import BeautifulSoup
import unicodedata

##function to remove accents
def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(text)

## Getting Soup
def scraping(input_team):
    url='https://dondeverlo.com/futbol/equipo/{}'.format(team)
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    return soup

##next_match
def next_match(soup):
    matches=soup.findAll('h2',{"class":'Event__title'})
    match=matches[0].text
    match=match.lstrip().rstrip()
    return match

##team2
def team2(soup,team):
    matches=soup.findAll('h2',{"class":'Event__title'})
    match=matches[0].text
    match=match.lstrip().rstrip()
    
    nm2=re.sub("\s\s+" , " ",match)
    nm2=strip_accents(nm2)
    nm3=nm2.split(" - ",)
    local=nm3[0]
    visitor=nm3[1]
    if local==team:
        return visitor
    else:
        return local

##date_next_match
def date_next_match(soup):
    dates = soup.findAll('div',{"class":'Event__when'})
    date_match = dates[0].text
    date_match = date_match.lstrip().rstrip()
    return date_match

##competition_next_match
def competition_next_match(soup):
    competition = soup.findAll('span',{"class":'Event__championshipText'})
    competition_match = competition[0].text
    competition_match = competition_match.lstrip().rstrip()
    competition=competition_match.split("-")
    return competition[1].lstrip().rstrip()

##matchday_next_match
def matchday_next_match(soup):
    matchday = soup.findAll('div',{"class":'Event__description'})
    matchday_match = matchday[0].text
    matchday_match = matchday_match.lstrip().rstrip()
    return matchday_match

##summary scrapping next match
def printer(soup,team):
    return "El proximo partido de tu equipo es el {} contra {} correspondiente a la {} de {}.".format(date_match,contender,matchday_match,competition_match)
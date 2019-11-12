import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

## Getting Soup
def scraping(team):
    url='https://dondeverlo.com/futbol/equipo/{}'.format(team.lower())
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    return soup

##next_match
def next_match(soup):
    matches = soup.findAll('h2',{"class":'Event__title'})
    next_match = matches[0].find("a").text
    next_match = next_match.lstrip().rstrip()
    return next_match

##team2
def team2(soup,team):
    matches = soup.findAll('h2',{"class":'Event__title'})
    next_match = matches[0].find("a").text
    next_match = next_match.lstrip().rstrip()
    nm2=re.sub("\s\s+" , " ",next_match)
    nm3=nm2.split(" - ",)
    nm3 = [w.replace('Alavés','Alaves') for w in nm3]
    local=nm3[0].lower()
    visitor=nm3[1].lower()
    team=team.lower()

    ##print(nm3,nm31)
    if local==team:
        return visitor
    else:
        return local

##date_next_match
def date_next_match(soup):
    dates = soup.findAll('div',{"class":'Event__when'})
    date_next_match = dates[0].text
    date_next_match = date_next_match.lstrip().rstrip()
    return date_next_match

##competition_next_match
def competition_next_match(soup):
    competition = soup.findAll('span',{"class":'Event__championshipText'})
    competition_next_match = competition[0].text
    competition_next_match = competition_next_match.lstrip().rstrip()
    competition=competition_next_match.split("-")
    return competition[1].lstrip().rstrip()

##matchday_next_match
def matchday_next_match(soup):
    matchday = soup.findAll('div',{"class":'Event__description'})
    matchday_next_match = matchday[0].text
    matchday_next_match = matchday_next_match.lstrip().rstrip()
    return matchday_next_match

def printer(soup,team):
    return "El proximo partido de tu equipo es el {} contra el {} correspondiente a la {} de {}.".format(date_next_match(soup),team2(soup,team).upper(),matchday_next_match(soup),competition_next_match(soup))
import requests
from bs4 import BeautifulSoup
import pandas as pd

## Getting Soup
def scraping(team):
    url='https://dondeverlo.com/futbol/equipo/{}'.format(team)
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    return soup

##next_match
def next_match(team):
    matches = soup.findAll('h2',{"class":'Event__title'})
    next_match = matches[0].find("a").text
    return next_match

##date_next_match
def date_next_match(team):
    dates = soup.findAll('div',{"class":'Event__when'})
    date_next_match = dates[0].text
    return date_next_match

##competition_next_match
def competition_next_match(team):
    competition = soup.findAll('span',{"class":'Event__championshipText'})
    competition_next_match = competition[0].text
    return competition_next_match

##matchday_next_match
def matchday_next_match(team):
    matchday = soup.findAll('div',{"class":'Event__description'})
    matchday_next_match = matchday[0].text
    return matchday_next_match

team="eibar"
scraping(team)
print(next_match(team))
print(date_next_match(team))
print(competition_next_match(team))
print(matchday_next_match(team))
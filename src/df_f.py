import pandas as pd
import re
import numpy as np

def dfFilter(team,contender):
    df=pd.read_csv("./input/FMEL_Dataset.csv")
    df['localTeam']=df['localTeam'].map(lambda x: x.lower() if isinstance(x,str) else x)
    df['visitorTeam']=df['visitorTeam'].map(lambda x: x.lower() if isinstance(x,str) else x)
    dff=df[(df['timestamp']>=1093644000) & ((df['localTeam']==(team)) | (df['localTeam']==(contender))) & ((df['visitorTeam']==(contender)) | (df['visitorTeam']==(team)))]
    return dff.sort_values('timestamp', ascending=False)

##function to translate if your team wins, loses, or draws for each game
def result (row,team):
    if row['localGoals']==row['visitorGoals']:
        return 1
    if row['localTeam']==team and row['localGoals']>row['visitorGoals']:
        return 3
    if row['visitorTeam']==team and row['visitorGoals']>row['localGoals']:
        return 3
    else:
        return 0

##creating and appending new column
def summary(a,team,team2):
    a = a.value_counts()
    ##sign=a.value_counts()
    ##sign=df_team['result'].value_counts()
    return "{} y {} se han enfrentado {} veces en los últimos 20 años. El {} ha ganado {} partidos, perdido {}, y empatado {}.".format(team.upper(),team2.upper(),a.sum(),team.upper(),a[3],a[0],a[1])
import pandas as pd
import re
import numpy as np

def dfFilter(team,team2):
   team=team.lower()
   team2=team2.lower()
   df=pd.read_csv("./input/FMEL_Dataset.csv")
   df['localTeam']=df['localTeam'].map(lambda x: x.lower() if isinstance(x,str) else x)
   df['visitorTeam']=df['visitorTeam'].map(lambda x: x.lower() if isinstance(x,str) else x)
   df_team=df[(df['timestamp']>=1093644000) & ((df['localTeam']==(team)) | (df['localTeam']==(team2))) & ((df['visitorTeam']==(team2)) | (df['visitorTeam']==(team)))]
   return df_team

##function to translate if your team wins, loses, or draws for each game
def result (row):
   if row['localGoals'] == row['visitorGoals']:
      return 1
   if row['localTeam']==team and row['localGoals']>row['visitorGoals']:
      return 3
   if row['visitorTeam']==team and row['visitorGoals']>row['localGoals']:
      return 3
   else:
      return 0

##creating and appending new column

def summary(sign):
    return print("{} y {} se han enfrentado {} veces en los últimos 20 años. {} ha ganado {} partidos, perdido {}, y empatado {}.".format(team,team2,sign.sum(),team,sign[3],sign[0],sign[1]))

team="Levante"
team2="Mallorca"

df_team=dfFilter(team,team2)
df_team['result'] = df_team.apply(lambda row: result(row), axis=1)
a=df_team['result'].value_counts()
print(df_team)
print(a)
print(summary(a))
##print(summary(df_team['result']))
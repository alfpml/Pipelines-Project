import pandas as pd
import re
import numpy as np

def dfFilter(team,team2):
   team2=team2.lower()
   df=pd.read_csv("./input/FMEL_Dataset.csv")
   df['localTeam']=df['localTeam'].map(lambda x: x.lower() if isinstance(x,str) else x)
   df['visitorTeam']=df['visitorTeam'].map(lambda x: x.lower() if isinstance(x,str) else x)
   df_team=df[(df['timestamp']>=1093644000) & ((df['localTeam']==(team)) | (df['localTeam']==(team2))) & ((df['visitorTeam']==(team2)) | (df['visitorTeam']==(team)))]
   return df_team

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


'''
team="Levante"
team2="Mallorca"

df_team=dfFilter(team,team2)
df_team['result'] = df_team.apply(lambda df_team: result(df_team), axis=1)

print(df_team)
print(summary(df_team['result']))
'''
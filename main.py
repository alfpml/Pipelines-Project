import pandas as pd
import re
import numpy as np
import src.df_f as df_f
import src.scrp_f as scrp_f

##Exporting csv
df=pd.read_csv("./input/FMEL_Dataset.csv")
team="Sevilla"

scrp_f.scrapping(team)

team2="Eibar"

print(df_f.dfFilter(df,team,team2).head(100))

##print(df.dtypes)
##print(df.head(10))

##Filtering to take last 20 years and team selected by user (team) and next team playing aguunst (team2)
df_team=df[(df['timestamp']>=1093644000) & ((df['localTeam']==team) | (df['localTeam']==team2)) & ((df['visitorTeam']==team2) | (df['visitorTeam']==team))]

'''
##function to translate if your team wins, loses, or draws for each game
def result (row):
   if row['localGoals'] == row['visitorGoals']:
      return 1
   if row['localTeam']==team and row['localGoals']>row['visitorGoals']:
      return 3
   if row['visitorTeam']==team and row['visitorGoals']>row['localGoals']:
      return 3
   return 0
'''

##appending new column
df_team['result'] = df_team.apply (lambda row: df_f.result(row), axis=1)

'''
##print(df_team.dtypes)
##print(df_team)

sign=df_team['result'].value_counts()

print("{} y {} se han enfrentado {} veces en los últimos 20 años. {} ha ganado {} partidos, perdido {}, y empatado {}.".format(team,team2,sign.sum(),team,sign[3],sign[0],sign[1]))
'''
print(df_f.summary(df_team['result']))
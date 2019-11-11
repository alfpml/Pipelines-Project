def dfFilter(df,team,team2):
   df_team=df[(df['timestamp']>=1093644000) & ((df['localTeam']==team) | (df['localTeam']==team2)) & ((df['visitorTeam']==team2) | (df['visitorTeam']==team))]
   df_team['localTeam']=df_team['localTeam'].map(lambda x: x.lower() if isinstance(x,str) else x)
   df_team['visitorTeam']=df_team['visitorTeam'].map(lambda x: x.lower() if isinstance(x,str) else x)
   ##df_team3=df_team2['visitorTeam'].map(lambda x: x.lower() if isinstance(x,str) else x)
   return df_team

##function to translate if your team wins, loses, or draws for each game
def result (row):
   if row['localGoals'] == row['visitorGoals']:
      return 1
   if row['localTeam']==team and row['localGoals']>row['visitorGoals']:
      return 3
   if row['visitorTeam']==team and row['visitorGoals']>row['localGoals']:
      return 3
   return 0

##creating and appending new column
##df_team['result'] = df_team.apply (lambda row: result(row), axis=1)

def summary(a):
    ##a=df_team['result']
    sign=a.value_counts()
    return print("{} y {} se han enfrentado {} veces en los últimos 20 años. {} ha ganado {} partidos, perdido {}, y empatado {}.".format(team,team2,sign.sum(),team,sign[3],sign[0],sign[1]))
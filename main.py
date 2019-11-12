import pandas as pd
import re
import numpy as np
import argparse
import src.df_f as df_f
import src.scrp_f as scrp_f

def parse():
    parser = argparse.ArgumentParser(description='Descubre al siguiente rival de tu equipo')          
    parser.add_argument('--team', help='Elige tu equipo de la Liga. Ex: Villareal.', default='Levante')
    args = parser.parse_args()
    return args

# funcion principal
def main(): 
    args=parse()
    team=args.team
    team=team.lower()
    soup=scrp_f.scraping(team)
   
    next_match=scrp_f.next_match(soup)
    team2=scrp_f.team2(soup,team)
    team2=team2.lower()

    scrp_f.date_next_match(soup)
    scrp_f.competition_next_match(soup)
    scrp_f.matchday_next_match(soup)
    
    df_team=df_f.dfFilter(team,team2)
    df_team["result"] = df_team.apply(lambda df_team: df_f.result(df_team,team), axis=1)

    print(team)
    print(team2)
    print(df_team)

    print(scrp_f.printer(soup,team))
    print(df_f.summary(df_team['result'],team,team2))

if __name__=='__main__':
    main()

'''
team="Sevilla"
team=team.lower()
soup=scrp_f.scraping(team)
next_match=scrp_f.next_match(soup)
team2=scrp_f.team2(soup,team).lower()
scrp_f.date_next_match(soup)
scrp_f.competition_next_match(soup)
scrp_f.matchday_next_match(soup)
df_team=df_f.dfFilter(team,team2)
df_team['result'] = df_team.apply(lambda df_team: df_f.result(df_team,team), axis=1)

##print(team)
##print(team2)
##print(next_match)

print(scrp_f.printer(soup,team))
print(df_f.summary(df_team['result'],team,team2))
'''
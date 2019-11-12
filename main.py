import pandas as pd
import re
import numpy as np
import argparse
import src.df_f as df_f
import src.scrp_f as scrp_f

def parse():
    parser = argparse.ArgumentParser(description='Descubre al siguiente rival de tu equipo')
    parser.add_argument('--team', help='Elige tu equipo de la Liga. Ex: Villareal.')
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
    
    df_filtered=df_f.dfFilter(team,team2)
    df_filtered["result"] = df_filtered.apply(lambda df_filtered: df_f.result(df_filtered,team), axis=1)
    Last_Games=df_filtered.head(5)

    ##Saving csv file with last 5 games:
    Last_Games.to_csv("./output/lastgames.csv")

    print("Tu equipo: {}".format(team.upper()))
    print(scrp_f.printer(soup,team))
    print(df_f.summary(df_filtered['result'],team,team2))
    print("Ultimos 5 enfrentamientos:")
    print(Last_Games)

if __name__=='__main__':
    main()
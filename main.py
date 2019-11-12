import pandas as pd
import re
import numpy as np
import argparse
import src.df_f as df_f
import src.scrp_f as scrp_f

def parse():
    parser = argparse.ArgumentParser(description='Descubre al siguiente rival de tu equipo')
    parser.add_argument('--input_team', help='Elige tu equipo de la Liga. Ex: Villareal.')
    args = parser.parse_args()
    return args

# funcion principal
def main(): 
    args=parse()
    input_team=args.input_team
    soup=scrp_f.scraping(input_team)
    team=scrp_f.strip_accents(input_team)
    match=scrp_f.next_match(soup)
    
    team2=scrp_f.team2(soup,team)
    contender=scrp_f.strip_accents(team2)
    
    date_match=scrp_f.date_next_match(soup)
    competition_match=scrp_f.competition_next_match(soup)
    matchday_match=scrp_f.matchday_next_match(soup)
    
    df_filtered=df_f.dfFilter(team,contender)
    df_filtered["result"] = df_filtered.apply(lambda df_filtered: df_f.result(df_filtered,team), axis=1)
    
    Last_Games=df_filtered.head(5)

    ##Saving csv file with last 5 games:
    Last_Games.to_csv("./output/lastgames.csv")

    print("Tu equipo: {}".format(team.upper()))
    print("Tu rival: {}".format(contender.upper()))
    print("El proximo partido de tu equipo es el {} contra el {} correspondiente a la {} de {}.".format(date_match,contender.upper(),matchday_match,competition_match))

    print(df_f.summary(df_filtered['result'],team,contender))
    print("Ultimos 5 enfrentamientos:")
    print(Last_Games)
    
if __name__=='__main__':
    main()
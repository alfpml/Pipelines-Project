import pandas as pd
import re
import numpy as np
import src.df_f as df_f
import src.scrp_f as scrp_f

##Exporting csv
##df=pd.read_csv("./input/FMEL_Dataset.csv")


team="Sevilla"

soup=scrp_f.scraping(team)

next_match=scrp_f.next_match(soup)
team2=scrp_f.team2(soup,team)

print(next_match)
print(team2)

scrp_f.date_next_match(soup)
scrp_f.competition_next_match(soup)
scrp_f.matchday_next_match(soup)

print(df_f.dfFilter(team,team2))

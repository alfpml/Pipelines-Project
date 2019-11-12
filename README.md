# Pipelines-Project
SUMMARY
En este proyecto utilizo los siguientes inputs:
    1. Kaggle dataset con el histórico de partidos de la liga desde los años 70
    2. Scrapping de https://dondeverlo.com/ con la información de los siguientes partidos que jugará cada equipo
    3. User argument: el user indica su equipo en la terminal

Para producir el ssiguiente output:
    1. En la terminal se imprime el siguiente rival (contender) del equipo seleccionado y la fecha del siguiente partido y la competición y jornada correspondiente a ese partido. Todo esa información viene del scraping (funciones guardadas en scrp_f.py)
    2. Además se imprime en la terminal un resumen de los enfrentamientos directos entre estos dos equipos en los últimos 20 años indicando el número de victorias, derrotas y empates del equipo pasado como argumento. ADemás se imprime el resultado de los 5 últimos enfrentamientos que se imprime también en un csv en la carpeta output. (funciones guardadas en df_f.py).
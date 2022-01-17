#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests
import argparse
import warnings
#warnings.filterwarnings('ignore');
pd.set_option('display.max_rows', 500)

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import webbrowser


# In[23]:


from p_reporting import p_reporting as rp
    
def argument_parser():
    parser = argparse.ArgumentParser(description='comandos para obtener información de tus parques favoritos')
    
    parser.add_argument("-l", "--listado", help="listado con todos los nombres de los parques de la Comunidad de Madrid", action='store_true')
    parser.add_argument("-bs", "--bicimad_station", help="nombre de la estación de BiciMAD más cercana", action='store_true')
    parser.add_argument("-bm", "--bicimad_station_meters", help="distancia a la estación de BiciMAD más cercana", action='store_true')
    parser.add_argument("-ba", "--bicimad_adress", help="dirección de la estación de BiciMAD más cercana", action='store_true')
    parser.add_argument("-bb", "--bicimad_bikes", help="número de bicis disponibles", action='store_true')
    parser.add_argument("-bd", "--bicimad_dejar_bici", help="base disponible para dejar la bici", action='store_true')
    parser.add_argument("-pd", "--place_description", help="descripción del parque", action='store_true')
    parser.add_argument("-pb", "--place_barrio", help="barrio en el que se encuentra el parque", action='store_true')
    parser.add_argument("-pt", "--place_transport", help="transporte público cercano al parque", action='store_true')
    parser.add_argument("-e", "--email", help="escribe 'wikiparque.py -e' para recibir el listado completo de parques y estaciones de BiciMAD en tu email", action='store_true')


    args = parser.parse_args()
    return args


def main(arguments):
    
    location_min_dataset = "datasets/final_df_min_distance_optimizated.csv"
    interaction_min_dataset = rp.import_min_dataset(location_min_dataset)
    filename = "datasets/final_df_min_distance_optimizated.csv" 
    
    
    
    if not arguments.listado and  not arguments.bicimad_station and  not arguments.bicimad_adress and  not arguments.bicimad_bikes and  not arguments.bicimad_dejar_bici and  not arguments.place_description and  not arguments.place_barrio and  not arguments.place_transport and  not arguments.place_transport and  not arguments.email and not arguments.bicimad_station_meters:
        print("Hola, esta es una app informativa sobre los Parques Municipales de la excelentisima Comunidad de Madrid, presidida por nuestra dueña y señora AYUSO.\n Escribe: 'python wikiparque.py -h' para saber todo lo que podemos ofrecerte")
        
    elif arguments.listado:
        print(interaction_min_dataset["Place of interest"])
        print("\n")
        print("Si quieres más información escribe uno de los comandos que te mostramos en 'python wikiparque.py -h'")
           
    elif arguments.bicimad_station:
        input_parque = input("¿Cuál es tu parque favorito?: ")
        bicimad_station2 = rp.bicimad_station(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_station2)
        else:
            print("Parque mal escrito... busca en Google cachondo")
            
    elif arguments.bicimad_adress:
        input_parque = input("¿Cuál es tu parque favorito?: ")
        bicimad_adress2 = rp.bicimad_adress(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_adress2)
        else:
            print("Parque mal escrito... busca en Google cachondo")
            
    elif arguments.bicimad_bikes:
        input_parque = input("¿Cuál es tu parque favorito?: ")
        bicimad_bikes2 = rp.bicimad_bikes(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_bikes2)
        else:
            print("Parque mal escrito... busca en Google cachondo")
            
    elif arguments.bicimad_dejar_bici:
        input_parque = input("¿Cuál es tu parque favorito?: ")
        bicimad_dejar_bici2 = rp.bicimad_dejar_bici(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_dejar_bici2)
        else:
            print("Parque mal escrito... busca en Google cachondo")
            
    elif arguments.place_description:
        input_parque = input("¿Cuál es tu parque favorito?: ")
        place_description2 = rp.place_description(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(place_description2)
        else:
            print("Parque mal escrito... busca en Google cachondo")
            
    elif arguments.place_barrio:
        input_parque = input("¿Cuál es tu parque favorito?: ")
        place_barrio2 = rp.place_barrio(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(place_barrio2)
        else:
            print("Parque mal escrito... busca en Google cachondo")
            
    elif arguments.place_transport:
        input_parque = input("¿Cuál es tu parque favorito?: ")
        place_transport2 = rp.place_transport(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(place_transport2)
        else:
            print("Parque mal escrito... busca en Google cachondo")

    elif arguments.bicimad_station_meters:
        input_parque = input("¿Cuál es tu parque favorito?: ")
        bicimad_station_meters2 = rp.bicimad_station_meters(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_station_meters2)
            g_maps_question = input("esta distancia es en linea recta. ¿Quieres saber la distancia exacta en Google Maps. Escribe 'si' o 'no': ")
            if g_maps_question == "si" or g_maps_question == "SI" or g_maps_question == "Si" or g_maps_question == "sI":
                url_q_maps_question = rp.open_wikipedia(input_parque,interaction_min_dataset)
                webbrowser.open(url_q_maps_question)
            else:
                print("disfruta del parque")
        else:
            print("Parque mal escrito... busca en Google cachondo")
            
    elif arguments.email:
        receiver_email = input("escribe tu email: ")
        try:
            rp.wikiparque_email_sender(receiver_email,filename)
        except:
            print("Email mal escrito, fallo en Matrix")
        else:
            print("email enviado con éxito")  
        
    else:
        print("Comando mal escrito, escribe 'python wikiparque.py -h' para volver a ver el conjunto de comandos")     
                  
# Pipeline execution

if __name__ == '__main__':
    try:
        main(argument_parser())
    except:
        print("LOCOOOO, ¡ESTATE ATENTO! --> Comando mal escrito, escribe 'python wikiparque.py -h' para volver a ver el conjunto de comandos")


# In[ ]:





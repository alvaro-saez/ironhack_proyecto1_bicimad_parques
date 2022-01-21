#!/usr/bin/env python
# coding: utf-8

# ## MAIN ADMIN SCRIPT
# 
# THIS IS THE MAIN ADMIN SCRIPT, WHICH EXECUTE THE NEEDED CODE TO CREATE THE FINAL DATASETS USED BY THE USER SCRIPT

# In[1]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests
import argparse
import warnings
warnings.filterwarnings('ignore');


# In[2]:


from p_acquisition import p_acquisition as ac
from p_wrangling import p_wrangling as wr
from p_analysis import p_analysis as an

if __name__ == "__main__":

    def main_dataset():
        
    #credentials and file location needed to import the data
        email = "alvarosaezsanchez@gmail.com"
        psw = "Bicimad1%"
        location_parque = "datasets/parques_municipales.csv"
        #location_bici = "datasets/bicimad_statios_database.csv" --> deprecated location of a csv to create the bicimad dataframe
        
    # A) ACQUISITON MODULE
        #Dataframe of my Places of Interest
        parques_municipales_df = ac.import_parques_municipales(location_parque)
        #Dataframe with the BiciMAD information
        bicimad_st_df= ac.bicimad_api(email,psw)

    # B) WRANGLING MODULE
        wr.datasets_transformados(parques_municipales_df,bicimad_st_df)

    # C) ANALYSIS MODULE
        final_df_place = an.preparar_tabla_place(parques_municipales_df)
        final_df_bici = an.preparar_tabla_bicimad(bicimad_st_df)
        final_df = an.preparar_tabla_final(final_df_place,final_df_bici)
        final_df_min_distance = an.preparar_tabla_final_minimizada(final_df)
        an.open_street_maps(final_df_min_distance)    
        
        print("exportado con éxito")
    
#EJECUTION OF THE MAIN FUNCTION
    main_dataset()


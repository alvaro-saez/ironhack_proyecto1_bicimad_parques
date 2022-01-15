#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests


# In[ ]:


from p_acquisition import p_acquisition as ac
from p_wrangling import p_wrangling as wr
from p_analysis import p_analysis as an

#def main():

#DATA PIPELINE
if __name__ == "__main__":
    location_parque = "datasets/parques_municipales.csv"
    parques_municipales_df = ac.import_parques_municipales(location_parque)
    
    location_bici = "datasets/bicimad_statios_database.csv"
    bicimad_st_df= ac.import_bicimad(location_bici)
    

    wr.datasets_transformados(parques_municipales_df,bicimad_st_df)
    
    final_df_place = an.preparar_tabla_place(parques_municipales_df)
    final_df_bici = an.preparar_tabla_bicimad(bicimad_st_df)
    final_df = an.preparar_tabla_final(final_df_place,final_df_bici)
    final_df_min_distance = an.preparar_tabla_final_minimizada(final_df)
    
    print("exportado con éxito")


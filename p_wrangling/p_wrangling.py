#!/usr/bin/env python
# coding: utf-8

# ## WRANGLING SCRIPT
# 
# IN THIS SCRIPT WE TRANSFORM THE INITIAL DATAFRAMES TO CREATE THE FINAL DATAFRAMES

# In[1]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests
import warnings
warnings.filterwarnings('ignore');


# In[18]:


def datasets_transformados(parques_municipales_df,bicimad_st_df):
    #PARQUES MUNICIAPLES DATAFRAME --> we add a static value to use in the main user script
    parques_municipales_df["Type of Place"] = "Principales parques y jardines municipales"
    
    #BICIMAD DATAFRAME --> we extract the Longitude and Latitude
    def bicimad_geo_long(geo):
        geo_clean = str(geo).replace("[","").replace("]","").split(",")
        longitud = geo_clean[0].strip()
        return longitud
    bicimad_st_df["LONGITUD"] = bicimad_st_df["geometry_coordinates"].apply(bicimad_geo_long)
    
    def bicimad_geo_lat(geo):
        geo_clean = str(geo).replace("[","").replace("]","").split(",")
        latitud = geo_clean[1].strip()
        return latitud
    bicimad_st_df["LATITUD"] = bicimad_st_df["geometry_coordinates"].apply(bicimad_geo_lat)

    return "transformed datasets with success"


# In[19]:


#transform_parques_municipales(parques_municipales_df) 


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests


# In[3]:


#parques_municipales_df = pd.read_csv("../datasets/parques_municipales.csv", sep=';')


# In[4]:


#bicimad_st_df = pd.read_csv("../datasets/bicimad_statios_database.csv", sep=',')


# In[11]:


def datasets_transformados(parques_municipales_df,bicimad_st_df):
    parques_municipales_df["Type of Place"] = "Principales parques y jardines municipales"
    
    def bicimad_geo_long(geo):
        geo_clean = geo.replace("[","").replace("]","").split(",")
        longitud = geo_clean[0].strip()
        return longitud
    bicimad_st_df["LONGITUD"] = bicimad_st_df["geometry_coordinates"].apply(bicimad_geo_long)
    
    def bicimad_geo_lat(geo):
        geo_clean = geo.replace("[","").replace("]","").split(",")
        latitud = geo_clean[1].strip()
        return latitud
    bicimad_st_df["LATITUD"] = bicimad_st_df["geometry_coordinates"].apply(bicimad_geo_lat)

    return "datasets trasnformados"


# In[12]:


#transform_parques_municipales(parques_municipales_df) 


# In[ ]:





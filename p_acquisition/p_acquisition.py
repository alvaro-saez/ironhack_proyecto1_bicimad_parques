#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests


# #### importar dataset parques municipales

# In[10]:


# location = "../datasets/parques_municipales.csv"
def import_parques_municipales(location_parque):
    parques_municipales_df = pd.read_csv(location_parque, sep=';')
    return parques_municipales_df


# In[5]:


#location = "../datasets/parques_municipales.csv"
#import_parques_municipales(location)


# #### importar dataset bicimad

# In[11]:


def import_bicimad(location_bici):
    bicimad_st_df = pd.read_csv(location_bici, sep=',')
    return bicimad_st_df


# In[8]:


#location = "../datasets/bicimad_statios_database.csv"
#import_bicimad(location)


# In[ ]:





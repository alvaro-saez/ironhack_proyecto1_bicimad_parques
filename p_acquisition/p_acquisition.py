#!/usr/bin/env python
# coding: utf-8

# ## ACQUISITION SCRIPT
# 
# IN THIS SCRIPT WE IMPORT ALL THE DATA NEEDED TO CREATE THE FINAL DATAFRAMES

# In[14]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests
import warnings
warnings.filterwarnings('ignore');


# #### Import dataset of "parques municipales"

# The best practice would be to use the API of the city council of Madrid but I use the CSV because it has more information and my main objective is to create an app about the parks of Madrid, not about BiciMAD. This information is not updated everyday, so it is feasible to download the csv once per month:
# 
# The API code would be the next one:
# 
#     json_parques =  requests.get("https://datos.madrid.es/egob/catalogo/200761-0-parques-jardines.json").json()["@graph"]
# 
#     json_parques_df = pd.json_normalize(json_parques)

# In[15]:


# location = "../datasets/parques_municipales.csv"
def import_parques_municipales(location_parque):
    parques_municipales_df = pd.read_csv(location_parque, sep=';')
    return parques_municipales_df


# In[16]:


#location = "../datasets/parques_municipales.csv"
#import_parques_municipales(location)


# #### Import dataset of bicimad API

# The best practice is to use the BiciMAD API service beacuse it has information which changes every day.
# 
# (DOCUMENTATION API: https://apidocs.emtmadrid.es/#api-Block_4_TRANSPORT_BICIMAD-List_of_Bicimad_Stations)

# In[ ]:


def bicimad_api(email,psw):
    auth_url = "https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/"
    json_bicimad =  requests.get(auth_url, headers={"email":email,"password":psw})
    json_bicimad_token= json_bicimad.json()['data'][0]['accessToken']
    bicimad_list_url = "https://openapi.emtmadrid.es/v1/transport/bicimad/stations/"
    json_bicimad_list = requests.get(bicimad_list_url, headers = {"accessToken":json_bicimad_token}).json()
    json_bicimad_df = pd.json_normalize(json_bicimad_list)["data"][0]
    
    def geometry_coordinates_bm(geometry):
        geometry_coordinates = geometry["coordinates"]
        return geometry_coordinates
    
    bicimad_st_df = pd.DataFrame(json_bicimad_df)
    bicimad_st_df["geometry_type"] = "Point"
    bicimad_st_df["geometry_coordinates"] = bicimad_st_df["geometry"].apply(geometry_coordinates_bm)
    
    bicimad_st_df = bicimad_st_df.drop(["geometry"], axis=1)
    
    return bicimad_st_df


# The code to use a csv file would be the next one:

#     def import_bicimad(location_bici):
# 
#         bicimad_st_df = pd.read_csv(location_bici, sep=',')
# 
#         return bicimad_st_df

# In[1]:


#bicimad_api(email,psw)


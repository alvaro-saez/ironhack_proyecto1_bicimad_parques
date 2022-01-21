#!/usr/bin/env python
# coding: utf-8

# ## ANALYSIS SCRIPT
# 
# IN THIS SCRIPT WE START TO APPLY FUNCTIONS TO THE FINAL DATAFRAMES TO OBTAIN THE GEOLOCATION INFORMATION AND TO PUT THE FINAL NAMES TO THEIR COLUMNS

# In[50]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests
import warnings
warnings.filterwarnings('ignore')
import osmnx as ox
import folium


# ####  1. PREPARE THE FINAL DATAFRAME
# 

# #### a) place dataframe

# In[41]:


def preparar_tabla_place(parques_municipales_df):
    
    #NAME OF COLUMNS
    final_df_colnames_place = ["Place of interest","Type of place","Place address","Place distrit","Place neighborhood","Place description","Place transport","Place latitude","Place longitude"]
    final_df_place = parques_municipales_df[["NOMBRE","Type of Place","NOMBRE-VIA","DISTRITO", "BARRIO", "DESCRIPCION-ENTIDAD", "TRANSPORTE","LATITUD","LONGITUD"]]
    final_df_place.columns = final_df_colnames_place
    
    #MERCATOR FUNCITON OF GEOPANDAS
    def to_mercator2(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
        c = gpd.GeoSeries([Point(lat, long)], crs=4326)
        c = c.to_crs(3857)
        return c
    
    final_df_place["mercator place"] = final_df_place.apply(lambda final_df_place: to_mercator2(final_df_place["Place latitude"], final_df_place["Place longitude"]), axis=1)
    
    return final_df_place


# In[42]:


#final_df_place = preparar_tabla_place(parques_municipales_df)
#final_df_place


# #### b) bicimad dataframe

# In[43]:


def preparar_tabla_bicimad(bicimad_st_df):

    #NAME OF COLUMNS    
    final_df_colnames_bici = ["BiciMAD station","Station location","Station latitude","Station longitude","Station base availability","Station Bikes Availability"]
    final_df_bici = bicimad_st_df[["name","address","LATITUD","LONGITUD", "no_available", "dock_bikes"]]
    final_df_bici.columns = final_df_colnames_bici
    
    #AVAILABILITY TEXT TRANSFORMATION
    def change_availability(data):
        if data == 0:
            return "disponible"
        elif data == 1:
            return "no disponible"
        else:
            return data
        
    final_df_bici["Station base availability"] = final_df_bici["Station base availability"].apply(change_availability)
    
    #MERCATOR FUNCITON OF GEOPANDAS
    def to_mercator2(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
        c = gpd.GeoSeries([Point(lat, long)], crs=4326)
        c = c.to_crs(3857)
        return c
    
    final_df_bici["Station latitude"] = pd.to_numeric(final_df_bici["Station latitude"])
    final_df_bici["Station longitude"] = pd.to_numeric(final_df_bici["Station longitude"])
    final_df_bici["mercator station"] = final_df_bici.apply(lambda final_df_bici: to_mercator2(final_df_bici["Station latitude"], final_df_bici["Station longitude"]), axis=1)
    
    return final_df_bici


# In[44]:


#final_df_bici = preparar_tabla_bicimad(bicimad_st_df)
#final_df_bici


# #### c) UNIFIED FINAL DATAFRAME WITH BOTH PREVIOUS TABLES ("parques" and "bicimad")

# In[45]:


def preparar_tabla_final(final_df_place,final_df_bici):
    
    #MERGE OF BOTH TABLES
    final_df = final_df_place.assign(key=1).merge(final_df_bici.assign(key=1), how='outer', on = 'key')
    
    #FINAL GEOPANDAS FUNCTION TO OBTAIN THE DISTANCE BETWEEN THE PARK AND THE BICIMAD STATION
    def distance_meters(start,finish):
        return start.distance(finish)
    
    #COLUMN ADDED
    final_df["Distance Between BiciMAD station and Place of interest"] = final_df.apply(lambda final_df: distance_meters(final_df["mercator place"], final_df["mercator station"]), axis=1)
    
    #EXPORTATION OF THIS DATAFRAME IN A CSV
    final_df_full_info_csv_optimizated = final_df.to_csv("datasets/final_df_full_info_optimizated.csv", sep=',',index=False)
    
    return final_df


# In[46]:


#final_df = preparar_tabla_final(final_df_place,final_df_bici)
#final_df


# #### 2. PREPARE THE FINAL MINIMIZED DATAFRAME
# 

# In[47]:


def preparar_tabla_final_minimizada(final_df):
    
    #OBTAINING THE MINIMUM DISTANCE USING GROUPBY() METHOD AND MIN() METHOD
    total_distance_array_min = final_df.groupby(["Place of interest"])["Distance Between BiciMAD station and Place of interest"].min().tolist()
    
    #CREATING A NEW DATAFRAME WITH ONLY ONE DISTANCE PER PARK
    list_min=[]
    for i in total_distance_array_min:
        linea_para_df = final_df.loc[final_df["Distance Between BiciMAD station and Place of interest"]==i]
        linea_para_df_list = linea_para_df.values.tolist()[0]
        list_min.append(linea_para_df_list)

    final_df_colnames_total = ["Place of interest","Type of place","Place address","Place distrit","Place neighborhood","Place description","Place transport","Place latitude","Place longitude","mercator place","key","BiciMAD station","Station location","Station latitude","Station longitude","Station base availability","Station Bikes Availability","mercator station"]
    final_df_min_distance = pd.DataFrame(list_min, columns=final_df_colnames_total+["Distance Between BiciMAD station and Place of interest"])
    
    #ENRICHING THE DATAFRAME WITH THE FINAL URL OF SOME INTEREST PLACES IN GOOGLE MAPS
    def place_maps_func(data):
        place_maps = "+".join(data.split(" "))
        return place_maps
    def g_maps_func(place_maps, bici_maps):
        g_maps = "https://www.google.com/maps/dir/" + str(place_maps) + "/" + str(bici_maps)
        return g_maps

    final_df_min_distance["place_maps"] = final_df_min_distance["Place of interest"].apply(place_maps_func)
    final_df_min_distance["bici_maps"] = final_df_min_distance["Station location"].apply(place_maps_func)
    final_df_min_distance["g_maps"] = final_df_min_distance.apply(lambda final_df_min_distance: g_maps_func(final_df_min_distance["place_maps"], final_df_min_distance["bici_maps"]), axis=1)
    
    #EXPORTING THIS DATAFRAME IN A CSV
    final_df_min_distance_csv_optimizated = final_df_min_distance.to_csv("datasets/final_df_min_distance_optimizated.csv", sep=',',index=False)
    
    return final_df_min_distance


# In[48]:


#final_df_min_distance = preparar_tabla_final_minimizada(final_df)
#final_df_min_distance


# #### open_street_maps
# 
# It is a function to obtain a map with all the parks of Madrid in a single HTML file

# In[ ]:


def open_street_maps(final_df_min_distance):
    m = folium.Map([40.433462, -3.678595], zoom_start=12)
    locs = zip(final_df_min_distance["Place latitude"].tolist(), final_df_min_distance["Place longitude"].tolist())
    for location in locs:
        #print(location)
        if "nan" not in str(location):
            folium.CircleMarker(location=location).add_to(m)
            m.save('datasets/open_street_df.html')
    return m


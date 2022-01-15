#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests


# In[2]:


#parques_municipales_df = pd.read_csv("../datasets/parques_municipales.csv", sep=';')


# In[3]:


#bicimad_st_df = pd.read_csv("../datasets/bicimad_statios_database.csv", sep=',')


# In[4]:


"""
def transform_parques_municipales(parques_municipales_df):
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
"""


# In[5]:


#transform_parques_municipales(parques_municipales_df) 


# #### preparar la tabla final
# 

# In[13]:


def preparar_tabla_place(parques_municipales_df):
    final_df_colnames_place = ["Place of interest","Type of place","Place address","Place distrit","Place neighborhood","Place description","Place transport","Place latitude","Place longitude"]
    final_df_place = parques_municipales_df[["NOMBRE","Type of Place","NOMBRE-VIA","DISTRITO", "BARRIO", "DESCRIPCION-ENTIDAD", "TRANSPORTE","LATITUD","LONGITUD"]]
    final_df_place.columns = final_df_colnames_place
    
    def to_mercator2(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
        c = gpd.GeoSeries([Point(lat, long)], crs=4326)
        c = c.to_crs(3857)
        return c
    
    final_df_place["mercator place"] = final_df_place.apply(lambda final_df_place: to_mercator2(final_df_place["Place latitude"], final_df_place["Place longitude"]), axis=1)
    return final_df_place


# In[21]:


#final_df_place = preparar_tabla_place(parques_municipales_df)
#final_df_place


# In[17]:


def preparar_tabla_bicimad(bicimad_st_df):
    final_df_colnames_bici = ["BiciMAD station","Station location","Station latitude","Station longitude","Station base availability","Station Bikes Availability"]
    final_df_bici = bicimad_st_df[["name","address","LATITUD","LONGITUD", "no_available", "dock_bikes"]]
    final_df_bici.columns = final_df_colnames_bici
    
    def change_availability(data):
        if data == 0:
            return "disponible"
        elif data == 1:
            return "no disponible"
        else:
            return data
        
    final_df_bici["Station base availability"] = final_df_bici["Station base availability"].apply(change_availability)
    
    def to_mercator2(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
        c = gpd.GeoSeries([Point(lat, long)], crs=4326)
        c = c.to_crs(3857)
        return c
    
    final_df_bici["Station latitude"] = pd.to_numeric(final_df_bici["Station latitude"])
    final_df_bici["Station longitude"] = pd.to_numeric(final_df_bici["Station longitude"])
    final_df_bici["mercator station"] = final_df_bici.apply(lambda final_df_bici: to_mercator2(final_df_bici["Station latitude"], final_df_bici["Station longitude"]), axis=1)
    
    return final_df_bici


# In[22]:


#final_df_bici = preparar_tabla_bicimad(bicimad_st_df)
#final_df_bici


# In[25]:


def preparar_tabla_final(final_df_place,final_df_bici):
    final_df_colnames_total = ["Place of interest","Type of place","Place address","Place distrit","Place neighborhood","Place description","Place transport","Place latitude","Place longitude","mercator place","BiciMAD station","Station location","Station latitude","Station longitude","Station base availability","Station Bikes Availability","mercator station"]
    
    final_df_list =[]
    for i in range(len(final_df_place)): #203 filas
        for e in range(len(final_df_bici)): # 264 filas
            #raw_number = i*e #53592 filas
            #final_df.loc[raw_number] = final_df_place.loc[i].append(final_df_bici.loc[e])
            str_individual = final_df_place.loc[i].append(final_df_bici.loc[e])
            list_individual = str_individual.tolist()
            final_df_list.append(list_individual)

    final_df = pd.DataFrame(final_df_list,columns=final_df_colnames_total)
    
    def distance_meters(start,finish):
    # return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
    #start = to_mercator2(lat_start, long_start)
    #finish = to_mercator2(lat_finish, long_finish)
        return start.distance(finish)
    
    final_df["Distance Between BiciMAD station and Place of interest"] = final_df.apply(lambda final_df: distance_meters(final_df["mercator place"], final_df["mercator station"]), axis=1)
    
    final_df_full_info_csv_optimizated = final_df.to_csv("datasets/final_df_full_info_optimizated.csv", sep=',')
    
    return final_df


# In[27]:


#final_df = preparar_tabla_final(final_df_place,final_df_bici)
#final_df


# #### preparar la tabla minimizada
# 

# In[34]:


def preparar_tabla_final_minimizada(final_df):
    total_distance = final_df["Distance Between BiciMAD station and Place of interest"].tolist()

    total_distance_array = np.array(total_distance).reshape(203,264)

    total_distance_array_min = []
    for i in total_distance_array:
        total_distance_array_min.append(i.min())

    list_min=[]
    for i in total_distance_array_min:
        linea_para_df = final_df.loc[final_df["Distance Between BiciMAD station and Place of interest"]==i]
        linea_para_df_list = linea_para_df.values.tolist()[0]
        list_min.append(linea_para_df_list)

    final_df_colnames_total = ["Place of interest","Type of place","Place address","Place distrit","Place neighborhood","Place description","Place transport","Place latitude","Place longitude","mercator place","BiciMAD station","Station location","Station latitude","Station longitude","Station base availability","Station Bikes Availability","mercator station"]
    final_df_min_distance = pd.DataFrame(list_min, columns=final_df_colnames_total+["Distance Between BiciMAD station and Place of interest"])
    
    final_df_min_distance_csv_optimizated = final_df_min_distance.to_csv("datasets/final_df_min_distance_optimizated.csv", sep=',')
    
    return final_df_min_distance


# In[36]:


#final_df_min_distance = preparar_tabla_final_minimizada(final_df)
#final_df_min_distance


# In[ ]:





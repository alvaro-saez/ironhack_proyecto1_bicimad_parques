<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __ih_datamadpt1121_project_m1__

Ironhack Madrid - Data Analytics Part Time - November 2021 - Project Module 1

The current proyect consist on simulate the experience of an app through python code via Terminal UI. This "app" is about information around the Parks of Madrid.

It has 16 terminal commands to interact with the app asking for useful information:   
   
|  0 | wikiparque.py -help | comandos de ayuda para utilizar la app                                                                  |

|  1 | wikiparque.py -l    | listado con todos los nombres de los parques de la Comunidad de Madrid                                  |

|  2 | wikiparque.py -lpb  | listado con todos los parques de la Comunidad de Madrid y su respectiva estación de BiciMad más cercana |

|  3 | wikiparque.py -m    | mapa con todos los parques de la Comunidad de Madrid                                                    |

|  4 | wikiparque.py -bs   | nombre de la estación de BiciMAD más cercana                                                            |

|  5 | wikiparque.py -bm   | distancia a la estación de BiciMAD más cercana                                                          |

|  6 | wikiparque.py -ba   | dirección de la estación de BiciMAD más cercana                                                         |

|  7 | wikiparque.py -bb   | número de bicis disponibles en la estación de BiciMAD más cercana                                       |

|  8 | wikiparque.py -bd   | base disponible para dejar la bici en la estación de BiciMAD más cercana                                |

|  9 | wikiparque.py -pd   | descripción del parque                                                                                  |

| 10 | wikiparque.py -pb   | barrio en el que se encuentra el parque                                                                 |

| 11 | wikiparque.py -pt   | transporte público cercano al parque                                                                    |

| 12 | wikiparque.py -e    | para recibir el listado completo de parques y estaciones de BiciMAD en tu email                         |

| 13 | wikiparque.py -gm   | rutas en Google Maps desde tu ubicación hasta tu parque favorito                                        |

| 14 | wikiparque.py -gi   | imágenes del parque                                                                                     |

| 15 | wikiparque.py -gr   | restaurantes cerca de tu parque favorito                                                                |

| 16 | wikiparque.py -tr   | videos random que se irán actualizando de celebridades usando los parques de la Comunidad de Madrid

## **Data:**

There are 2 main datasources:

- **MADRID CITY HALL API OR CSV** 

The best practice would be to use the API of the city council of Madrid but I have used the CSV because it has more information and my main objective is to create a complete app about the parks of Madrid. This information is not updated everyday, so it is feasible to download the csv once per month


- **API REST OF BICIMAD.** 

The best practice is to use the BiciMAD API service beacuse it has information which changes every day and it is not feasible to dowload every day.

(DOCUMENTATION API: https://apidocs.emtmadrid.es/#api-Block_4_TRANSPORT_BICIMAD-List_of_Bicimad_Stations)


---

## **MODULES:**

This Python App (**Data Pipeline**) has 2 main scripts:

- ADMIN SCRIPT called "main_script_dataset.py": It executes the needed code to create the final datasets used bu the user script. It use 3 modules:

   a) p_acquisition: In this script we import all the data needed to create the final dataframes.
   
   b) p_wrangling: it transforms the previous dataframes to the right format and number of collumns to be enriched.
   
   c) p_analysis: In it we start to apply functions to the final dataframes to obtain geolocation information and to put the final names to their columns
   
- USER SCRIPT called "wikiparque.py": This script pretends to establish a conversation with the user to give useful information about the parks of madrid. It use one module:
   a) p_reporting: 
       - it imports the final dataframes via CSV, so as we had made all the api cals in the admin script, this script will spend less time to be executed. This is very important to the user experience.
       - it also has functions which give us the desired value by the customer when she/he writes her/his favourite park

The interaction is expressed using inputs method and ARPARSE, which allows to use commands in the terminal. 

--- 

## **CODE**

- ACQUISITION SCRIPT:
a) Import dataset of "parques municipales": 

The API code would be the next one:

   json_parques =  requests.get("https://datos.madrid.es/egob/catalogo/200761-0-parques-jardines.json").json()["@graph"]

   json_parques_df = pd.json_normalize(json_parques)
   
The final csv is:

# location = "../datasets/parques_municipales.csv"

def import_parques_municipales(location_parque):
    parques_municipales_df = pd.read_csv(location_parque, sep=';')
    return parques_municipales_df


b) Import dataset of bicimad API:
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

- WRANGLING SCRIPT:

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

- ANALYSIS SCRIPT:

1. PREPARE THE FINAL DATAFRAME

a) place dataframe:

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
    
b) bicimad dataframe:

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
    
c) UNIFIED FINAL DATAFRAME WITH BOTH PREVIOUS TABLES ("parques" and "bicimad"):

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

2. PREPARE THE FINAL MINIMIZED DATAFRAME

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
    
 
 


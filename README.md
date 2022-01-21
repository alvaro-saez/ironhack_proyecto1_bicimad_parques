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
<p align="left"><img src="https://github.com/alvaro-saez/ih_datamadpt1121_project_m1/blob/main/datasets/code_img/ac1.png"></p>









 


 


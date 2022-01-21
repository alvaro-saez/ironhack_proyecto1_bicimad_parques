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

You can see all the code in the differents modules. It is explained with comments. T

The next code belongs to the main user script (wikiparque.py") which establishes the interaction with the user

def argument_parser():
    parser = argparse.ArgumentParser(description='comandos para obtener información de tus parques favoritos',add_help=False)
    
    #THE PARSER ARGUMENT WHICH THE USER HAS
    parser.add_argument("-help", "--help_app_used", help="restaurantes cerca de tu parque favorito", action='store_true')
    parser.add_argument("-l", "--listado", help="listado con todos los nombres de los parques de la Comunidad de Madrid", action='store_true')
    parser.add_argument("-lpb", "--listado_parques_bicis", help="listado con todos los parques de la Comunidad de Madrid y su respectiva estación de BiciMad más cercana", action='store_true')
    parser.add_argument("-m", "--maps_parques", help="mapa con todos los parques de la Comunidad de Madrid", action='store_true')
    parser.add_argument("-bs", "--bicimad_station", help="nombre de la estación de BiciMAD más cercana", action='store_true')
    parser.add_argument("-bm", "--bicimad_station_meters", help="distancia a la estación de BiciMAD más cercana", action='store_true')
    parser.add_argument("-ba", "--bicimad_adress", help="dirección de la estación de BiciMAD más cercana", action='store_true')
    parser.add_argument("-bb", "--bicimad_bikes", help="número de bicis disponibles en la estación de BiciMAD más cercana", action='store_true')
    parser.add_argument("-bd", "--bicimad_dejar_bici", help="base disponible para dejar la bici en la estación de BiciMAD más cercana", action='store_true')
    parser.add_argument("-pd", "--place_description", help="descripción del parque", action='store_true')
    parser.add_argument("-pb", "--place_barrio", help="barrio en el que se encuentra el parque", action='store_true')
    parser.add_argument("-pt", "--place_transport", help="transporte público cercano al parque", action='store_true')
    parser.add_argument("-e", "--email", help="escribe 'wikiparque.py -e' para recibir el listado completo de parques y estaciones de BiciMAD en tu email", action='store_true')
    parser.add_argument("-gm", "--google_maps", help="rutas en Google Maps desde tu ubicación hasta tu parque favorito", action='store_true')
    parser.add_argument("-gi", "--google_maps_img", help="imágenes del parque", action='store_true')
    parser.add_argument("-gr", "--place_restaurantes", help="restaurantes cerca de tu parque favorito", action='store_true')
    parser.add_argument("-tr", "--troll", help="videos random que se irán actualizando de celebridades usando los parques de la Comunidad de Madrid", action='store_true')

    args = parser.parse_args()
    return args


def main(arguments):
    
    #LOCATION OF THE FILES NEEDED TO USE IN THIS SCRIPT
    location_min_dataset = "datasets/final_df_min_distance_optimizated.csv"
    interaction_min_dataset = rp.import_min_dataset(location_min_dataset)
    filename = "datasets/final_df_min_distance_optimizated.csv"
    location_speak = "datasets/input_speak.mp3" #deprecated (old voice command location)
    engine = pyttsx3.init(); #for voice command
    
    #A NEW DATAFRAME TO SHOW TO THE USER ALL THE COMMANDS IN A PRETTIER TABLE
    argparse_comand_list = ["wikiparque.py -help", "wikiparque.py -l", "wikiparque.py -lpb",  "wikiparque.py -m",  "wikiparque.py -bs",  "wikiparque.py -bm",  "wikiparque.py -ba",  "wikiparque.py -bb",  "wikiparque.py -bd",  "wikiparque.py -pd",  "wikiparque.py -pb",  "wikiparque.py -pt",  "wikiparque.py -e",  "wikiparque.py -gm",  "wikiparque.py -gi",  "wikiparque.py -gr", "wikiparque.py -tr"]
    argparse_comand_list_help = ["comandos de ayuda para utilizar la app",
                                 "listado con todos los nombres de los parques de la Comunidad de Madrid",
                                 "listado con todos los parques de la Comunidad de Madrid y su respectiva estación de BiciMad más cercana",
                                 "mapa con todos los parques de la Comunidad de Madrid",
                                 "nombre de la estación de BiciMAD más cercana",
                                 "distancia a la estación de BiciMAD más cercana",
                                 "dirección de la estación de BiciMAD más cercana",
                                 "número de bicis disponibles en la estación de BiciMAD más cercana",
                                 "base disponible para dejar la bici en la estación de BiciMAD más cercana",
                                 "descripción del parque",
                                 "barrio en el que se encuentra el parque",
                                 "transporte público cercano al parque",
                                 "para recibir el listado completo de parques y estaciones de BiciMAD en tu email",
                                 "rutas en Google Maps desde tu ubicación hasta tu parque favorito",
                                 "imágenes del parque",
                                 "restaurantes cerca de tu parque favorito",
                                 "videos random que se irán actualizando de celebridades usando los parques de la Comunidad de Madrid"]
    argparse_comand_list_df = pd.DataFrame({"command lists":argparse_comand_list,
                              "commands description":argparse_comand_list_help})
    
    #FUNCTION OF FUZZYWUZY TO INCREASE THE APP LEGIBILITY
    def fw_ratio(x):
        fw1 = x
        fw2 = input_parque_user
        ratio = fuzz.ratio(input_parque_user.lower().strip(), x.lower().strip())
        return ratio
    
    #INITIAL STATEMENT TO PRESENT TO THE USER THE APP
    if not arguments.listado and  not arguments.help_app_used and  not arguments.listado_parques_bicis and  not arguments.maps_parques and  not arguments.bicimad_station and  not arguments.bicimad_adress and  not arguments.bicimad_bikes and  not arguments.bicimad_dejar_bici and  not arguments.place_description and  not arguments.place_barrio and  not arguments.place_transport and  not arguments.place_transport and  not arguments.email and not arguments.bicimad_station_meters and not arguments.google_maps and not arguments.google_maps_img and not arguments.place_restaurantes and  not arguments.troll:
        intro = "Hola, esta es una app informativa sobre los Parques Municipales de la excelentísima Comunidad de Madrid, presidida por nuestra dueña y señora AYUSO.\n Escribe: 'python wikiparque.py -help' para saber todo lo que podemos ofrecerte"
        print(intro)
        #rp.speak_wikiparque(intro, location_speak)
        engine.say(intro);
        engine.runAndWait();
    
    #EXECUTION OF ALL THE COMMANDS
    elif arguments.help_app_used:
        print(tabulate(
            argparse_comand_list_df,
            headers=argparse_comand_list_df.columns,
            floatfmt=".5f",
            showindex=True,
            tablefmt="psql",
            )
        )
        #print(interaction_min_dataset["Place of interest"])
        print("\n")
        listado_text = "Si quieres más información escribe uno de los comandos que te mostramos en 'python wikiparque.py -help'"
        print(listado_text)
        engine.say(listado_text);
        engine.runAndWait();

    elif arguments.listado:
        print(tabulate(
            pd.DataFrame(interaction_min_dataset["Place of interest"]),
            headers=pd.DataFrame(interaction_min_dataset["Place of interest"]).columns,
            floatfmt=".5f",
            showindex=True,
            tablefmt="psql",
            )
        )
        #print(interaction_min_dataset["Place of interest"])
        print("\n")
        listado_text = "Si quieres más información escribe uno de los comandos que te mostramos en 'python wikiparque.py -help'"
        print(listado_text)
        engine.say(listado_text);
        engine.runAndWait();
        
    elif arguments.listado_parques_bicis:
        print(tabulate(
            pd.DataFrame(interaction_min_dataset[["Place of interest","BiciMAD station"]]),
            headers=pd.DataFrame(interaction_min_dataset[["Place of interest","BiciMAD station"]]).columns,
            floatfmt=".5f",
            showindex=True,
            tablefmt="psql",
            )
        )
        #print(interaction_min_dataset[["Place of interest","BiciMAD station"]])
        print("\n")
        listado_text = "Si quieres más información escribe uno de los comandos que te mostramos en 'python wikiparque.py -help'"
        print(listado_text)
        engine.say(listado_text);
        engine.runAndWait();
        
    elif arguments.maps_parques:
        #rp.open_street_maps(interaction_min_dataset)
        webbrowser.open("file:///C:/Users/AlvaroSaez/Desktop/ironhack/ih_datamadpt1121_project_m1/datasets/open_street_df.html")
        print("\n")
        maps_parques_text = "Si quieres más información escribe uno de los comandos que te mostramos en 'python wikiparque.py -help'"
        print(maps_parques_text)
        engine.say(maps_parques_text);
        engine.runAndWait();
        
    elif arguments.bicimad_station:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        bicimad_station2 = rp.bicimad_station(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_station2)
            engine.say(bicimad_station2);
            engine.runAndWait();
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();
            
    elif arguments.bicimad_adress:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        bicimad_adress2 = rp.bicimad_adress(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_adress2)
            engine.say(bicimad_adress2);
            engine.runAndWait();
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();
            
    elif arguments.bicimad_bikes:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        bicimad_bikes2 = rp.bicimad_bikes(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_bikes2)
            engine.say(bicimad_bikes2);
            engine.runAndWait();
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();
            
    elif arguments.bicimad_dejar_bici:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        bicimad_dejar_bici2 = rp.bicimad_dejar_bici(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_dejar_bici2)
            engine.say(bicimad_dejar_bici2);
            engine.runAndWait();
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();
            
    elif arguments.place_description:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        place_description2 = rp.place_description(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(place_description2)
            engine.say(place_description2);
            engine.runAndWait();
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();
            
    elif arguments.place_barrio:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        place_barrio2 = rp.place_barrio(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(place_barrio2)
            engine.say(place_barrio2);
            engine.runAndWait();
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();
            
    elif arguments.place_transport:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        place_transport2 = rp.place_transport(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(place_transport2)
            engine.say(place_transport2);
            engine.runAndWait();
            print("\n")
            engine.say("Dinos tu ubicación y te mostraremos en Google Maps cuanto tardarías para cada uno de los trasportes públicos");
            engine.runAndWait();
            ubicación_place_transport_user = input("Dinos tu ubicación y te mostraremos en Google Maps cuanto tardarías para cada uno de los trasportes públicos: ").strip()
            ubicación_place_transport_user_formated = "+".join(ubicación_place_transport_user.split(" "))
            imput_parque_user_formated = "+".join(input_parque.split(" "))
            url_formated_transport_open_g_maps = "https://www.google.com/maps/dir/" + ubicación_place_transport_user_formated  + "/" + imput_parque_user_formated 
            webbrowser.open(url_formated_transport_open_g_maps)
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();

    elif arguments.bicimad_station_meters:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        bicimad_station_meters2 = rp.bicimad_station_meters(input_parque,interaction_min_dataset)
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            print(bicimad_station_meters2)
            engine.say(bicimad_station_meters2);
            engine.runAndWait();
            engine.say("esta distancia es en linea recta. ¿Quieres saber la distancia exacta en Google Maps. Escribe 'si' o 'no'");
            engine.runAndWait();
            g_maps_question = input("esta distancia es en linea recta. ¿Quieres saber la distancia exacta en Google Maps. Escribe 'si' o 'no': ").strip()
            if g_maps_question == "si" or g_maps_question == "SI" or g_maps_question == "Si" or g_maps_question == "sI":
                url_q_maps_question = rp.open_wikipedia(input_parque,interaction_min_dataset)
                webbrowser.open(url_q_maps_question)
            #else:
                #disfruta_del_parque_vocie = "disfruta del parque"
                #print(disfruta_del_parque_vocie)
                #engine.say(disfruta_del_parque_vocie);
                #engine.runAndWait();
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();
            
    elif arguments.email:
        engine.say("escribe tu email");
        engine.runAndWait();
        receiver_email = input("escribe tu email: ").strip()
        try:
            rp.wikiparque_email_sender(receiver_email,filename)
        except:
            email_wrong_voice = "Email mal escrito, fallo en Matrix"
            print(email_wrong_voice)
            engine.say(email_wrong_voice);
            engine.runAndWait();
        else:
            email_ok_voice = "email enviado con éxito"
            print(email_ok_voice)
            engine.say(email_ok_voice);
            engine.runAndWait();
        
    elif arguments.google_maps:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            engine.say("¿Cuál es tu ubicación?");
            engine.runAndWait();
            ubicación_place_transport_user = input("¿Cuál es tu ubicación?: ").strip()
            ubicación_place_transport_user_formated = "+".join(ubicación_place_transport_user.split(" "))
            imput_parque_user_formated = "+".join(input_parque.split(" "))
            url_formated_transport_open_g_maps = "https://www.google.com/maps/dir/" + ubicación_place_transport_user_formated  + "/" + imput_parque_user_formated 
            webbrowser.open(url_formated_transport_open_g_maps)
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();

    elif arguments.place_restaurantes:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            imput_parque_user_formated = "+".join(input_parque.split(" "))
            url_formated_restaurants_g_maps = "https://www.google.com/maps/search/Restaurantes+cerca+de+" + imput_parque_user_formated  + "/"
            webbrowser.open(url_formated_restaurants_g_maps)
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();

    elif arguments.google_maps_img:
        engine.say("¿Cuál es tu parque favorito?");
        engine.runAndWait();
        
        #imput_parque_user
        input_parque_user = input("¿Cuál es tu parque favorito?: ").strip()
        
        #fuzzywuzzy max ratio place of interest
        interaction_min_dataset["place_sim_ratio"] = interaction_min_dataset["Place of interest"].apply(fw_ratio)
        place_sim_ratio_max = interaction_min_dataset["place_sim_ratio"].max()
        input_parque = interaction_min_dataset.loc[(interaction_min_dataset[("place_sim_ratio")]==place_sim_ratio_max)]["Place of interest"].tolist()[0]
        
        engine.say("para" + input_parque);
        engine.runAndWait();
        if input_parque in interaction_min_dataset["Place of interest"].tolist():
            imput_parque_user_formated = "+".join(input_parque.split(" "))
            url_formated_img_g_maps = "https://www.google.com/search?q=" + imput_parque_user_formated  + "&source=lnms&tbm=isch"
            webbrowser.open(url_formated_img_g_maps)
        else:
            error_wrong_park = "Parque mal escrito... busca en Google cachondo"
            print(error_wrong_park)
            engine.say(error_wrong_park);
            engine.runAndWait();
            
    elif arguments.troll:
        troll_video = "file:///C:/Users/AlvaroSaez/Desktop/ironhack/ih_datamadpt1121_project_m1/datasets/almeida_parques_fin.mp4"
        webbrowser.open(troll_video)
        print("\n")
        listado_text = "gracias por usar wikiparque, esperamos volver a verte pronto"
        print(listado_text)
        engine.say(listado_text);
        engine.runAndWait();

    #MESSAGE IN CASE THE USER WRITES A WRONG COMMAND
    else:
        error_wrong_command = "Comando mal escrito, escribe 'python wikiparque.py -help' para volver a ver el conjunto de comandos"     
        print(error_wrong_command)
        engine.say(error_wrong_command);
        engine.runAndWait(); 
        
# Pipeline execution

if __name__ == '__main__':
    #TO HANDLING ERRORS WE USE TRY, EXCEPT AND ELSE, MINIMIZING CODE AND INCREASING THE USER EXPERIENCE
    try:
        main(argument_parser())
    except:
        error_command_locoo = "¡LOCO, Comando mal escrito! ¡ESTATE ATENTO!, Escribe 'python wikiparque.py -help' para volver a ver el conjunto de comandos"
        print(error_command_locoo)
        engine = pyttsx3.init(); #for voice command
        engine.say(error_command_locoo);
        engine.runAndWait();
    else:
        disfruta_del_parque_voice = "disfruta del parque"
        print(disfruta_del_parque_voice)
        engine = pyttsx3.init(); #for voice command
        engine.say(disfruta_del_parque_voice);
        engine.runAndWait();


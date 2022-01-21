#!/usr/bin/env python
# coding: utf-8

# ## REPORTING SCRIPT
# 
# IN THIS SCRIPT WE DEFINE ALL THE FUNCTIONS WHICH WILL BE USED IN THE USER INTERACTION SCRIPT CALLED "WIKIPARQUE.PY"

# In[54]:


import pandas as pd
from shapely.geometry import Point
import geopandas as gpd   # conda install -c conda-forge geopandas
import numpy as np
import requests

import warnings
warnings.filterwarnings('ignore');
pd.set_option('display.max_rows', 500)

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import webbrowser

import osmnx as ox
import folium


# #### IMPORT THE FINAL DATAFRAME CREATED WITH THE ADMIN SCRIPT

# In[63]:


#location_min_dataset = "../datasets/final_df_min_distance_optimizated.csv"
def import_min_dataset(location_min_dataset):
    interaction_min_dataset = pd.read_csv(location_min_dataset, sep=',', index_col=False)
    return interaction_min_dataset


# In[1]:


#interaction_min_dataset = import_min_dataset(location_min_dataset)
#interaction_min_dataset


# #### THE NEXT FUNCTIONS GIVES US A DESIRED VALUE BY THE CUSTOMER WHEN HE/SHE WRITES HIS/HER FAVOURITE PARK

# In[4]:


#CLOSEST BICIMAD STATION

def bicimad_station(input_parque,interaction_min_dataset):
    bicimad_station = "la estación de bicis más cercana es: " +str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "BiciMAD station"].tolist()[0])
    return bicimad_station


# In[5]:


#ADRESS OF THE CLOSEST BICIMAD STATION

def bicimad_adress(input_parque,interaction_min_dataset):
    bicimad_adress = "su dirección es: " + str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "Station location"].tolist()[0])
    return bicimad_adress


# In[6]:


#NUMBER OF BIKES OF THE CLOSEST BICIMAD STATION

def bicimad_bikes(input_parque,interaction_min_dataset):
    bicimad_bikes = "hay " + str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "Station Bikes Availability"].tolist()[0]) + " bicis disponibles"
    return bicimad_bikes


# In[7]:


#AVAILABILITY OF THE BASE OF THE CLOSEST BICIMAD STATION

def bicimad_dejar_bici(input_parque,interaction_min_dataset):
    bicimad_dejar_bici =str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "Station base availability"].tolist()[0]) + " base para dejar la bici"
    return bicimad_dejar_bici


# In[8]:


#DESCRIPTION OF THE PARK CHOSEN BY THE USER

def place_description(input_parque,interaction_min_dataset):
    place_description = str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "Place description"].tolist()[0])
    return place_description


# In[9]:


#NEIGHBORHOOD OF THE PARK CHOSEN BY THE USER

def place_barrio(input_parque,interaction_min_dataset):
    place_barrio = "su barrio es: " + str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "Place neighborhood"].tolist()[0])
    return place_barrio


# In[10]:


#NPUBLIC TRANSTPORT AVAILABLE OF THE PARK CHOSEN BY THE USER

def place_transport(input_parque,interaction_min_dataset):
    place_transport = "contiene los siguientes transportes: " + str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "Place transport"].tolist()[0])
    if str(place_transport) == "contiene los siguientes transportes: nan":
        place_transport = "lo siento, no hay transporte público cercano, anda un poco que te vendrá bien"
    elif "Servicio Bicimad" in str(place_transport):
        place_transport = place_transport.split("Servicio Bicimad")[0]
    return place_transport


# In[11]:


#DISTANCE IN METERS OF THE CLOSEST BICIMAD STATION

def bicimad_station_meters(input_parque,interaction_min_dataset):
    bicimad_station = "la estación de bicis más cercana esta a : " + str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "Distance Between BiciMAD station and Place of interest"].tolist()[0]) + " metros"
    return bicimad_station


# In[17]:


#FUNCTION TO SEND AN EMAIL TO THE USER WITH THE HOLE DATAFRAME INFORMATION

def wikiparque_email_sender(receiver_email,filename):

    subject = "WikiParque"
    body = "Te adjuntamos en formato CSV la informacion más relevante del conjunto de Paruqes de la Comunidad de Madrid"
    sender_email = "alvarosaezsanchez@gmail.com"
    receiver_email = receiver_email
    password = "jswfzrfqxpxibfzi"
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    
    filename = filename
    
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )     
    
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


# In[41]:


#FUNCTION TO OBTAIN AN URL OF GOOGLE MAPS WITH THE POSIBILITIES OF TRANSPORT BETWEEN THE PARK CHOSEN AND THE CURRENT LOCATION OF THE USER

def open_wikipedia(input_parque,interaction_min_dataset):
    final_open_maps_url = str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "g_maps"].tolist()[0])
    return final_open_maps_url


# In[ ]:


#FUNCTION TO OBTAIN AN URL OF GOOGLE MAPS WITH THE CLOSESTS RESTAURANTS OF THE PARK CHOSEN BY THE USER


def restaurantes_google_maps(input_parque,interaction_min_dataset):
    final_restaurantes_url = str(interaction_min_dataset.loc[(interaction_min_dataset[("Place of interest")]==input_parque), "g_maps"].tolist()[0])
    return final_open_maps_url


# In[60]:


#DEPRECATED FUNCTION TO ADD VOICE INTO THE TERMINAL
def speak_wikiparque(text_speak, location_speak):
    input_speak = gtts.gTTS(text_speak, lang="es")
    input_speak.save(location_speak)
    speak = playsound(location_speak)
    return speak


# In[2]:


#interaction_min_dataset["CONTENT-URL"]


<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __ih_datamadpt1121_project_m1__

Ironhack Madrid - Data Analytics Part Time - November 2021 - Project Module 1

The current proyect consist on simulate the experience of an app through python code via Terminal UI. This "app" is about information around the Parks of Madrid.

It has 16 terminal commands to interact with the app asking for useful inforamtion:

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

- **Azure SQL Database.** The database contains information from the BiciMAD stations including their location (i.e.: latitude / longitude). In order to access the database you may need the following credentials:
```
Server name:   sqlironhack
Database:      BiciMAD
```
> __IMPORTANT =>__ Username and password will be provided in class.


- **API REST.** We will use the API REST from the [Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/), where you can find the __Catálogo de datos__ with more than 70 datasets.

> __IMPORTANT =>__ Specific datasets will be assigned to each student in order to perform the challenges.


---

## **Main Challenge:**

You must create a Python App (**Data Pipeline**) that allow their potential users to find the nearest BiciMAD station to a set of places of interest. The output table should look similar to:

| Place of interest | Type of place (*) | Place address | BiciMAD station | Station location |
|---------|----------|-------|------------|----------|
| Auditorio Carmen Laforet (Ciudad Lineal)   | Centros Culturales | Calle Jazmin, 46 | Legazpi | Calle Bolívar, 3 |
| Centro Comunitario Casino de la Reina | Centros municipales de enseñanzas artísticas | Calle Casino, 3 | Chamartin | Calle Rodríguez Jaén, 40 |
| ...     | ...            | ...        | ...      | ...        |
> __(*)__ There is a list of datasets each one with different places. A specific dataset will be assigned to each student. 


**Your project must meet the following requirements:**

- It must be contained in a GitHub repository which includes a README file that explains the aim and content of your code. You may follow the structure suggested [here](https://github.com/potacho/data-project-template).

- It must create, at least, a `.csv` file including the requested table (i.e. Main Challenge). Alternatively, you may create an image, pdf, plot or any other output format that you may find convenient. You may also send your output by e-mail, upload it to a cloud repository, etc. 

- It must provide, at least, two options for the final user to select when executing using `argparse`: **(1)** To get the table for every 'Place of interest' included in the dataset (or a set of them), **(2)** To get the table for a specific 'Place of interest' imputed by the user.

**Additionally:**

- You must prepare a 4 minutes presentation (ppt, canva, etc.) to explain your project (Instructors will provide further details about the content of the presentation).

- The last slide of your presentation must include your candidate for the **'Ironhack Data Code Beauty Pageant'**. 


---

### **Bonus 1:**

You may include in your table the availability of bikes in each station.

---

### **Bonus 2:**

You may improve the usability of your app by using [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/).

---

### **Bonus 3:**

Feel free to enrich your output data with any data you may find relevant (e.g.: wiki info for every place of interest).

--- 

## **Project Main Stack**

- [Azure SQL Database](https://portal.azure.com/)

- [SQL Alchemy](https://docs.sqlalchemy.org/en/13/intro.html) (alternatively you can use _Azure Data Studio_)

- [Requests](https://requests.readthedocs.io/)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- Module `geo_calculations.py`

- [Argparse](https://docs.python.org/3.7/library/argparse.html)












 


 


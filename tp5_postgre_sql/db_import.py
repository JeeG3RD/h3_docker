import pandas as pd

import psycopg2
HOST = "127.0.0.1"
USER = "root"
PASSWORD = "passw0rd"
DATABASE = "nasa"

df_nasa = pd.read_csv("data/nasa.csv")

df_nasa = df_nasa[['Neo Reference ID', 'Est Dia in Miles(min)','Est Dia in Miles(max)', 'Jupiter Tisserand Invariant', 'Eccentricity', 'Semi Major Axis', 'Hazardous']]

#df_nasa = df_nasa.sample(1000)

arrayInserts = []

for i in range(0, (df_nasa.shape[0])):

    req = "Insert into astroids values("

    for each in df_nasa.columns:
        req += str(df_nasa.loc[i][each])
        req += ","
    
    req += ")"
    arrayInserts.append(req)

# Connexion à la bdd
conn = psycopg2.connect("host={} dbname={} user={} password={}".format(HOST, DATABASE, USER, PASSWORD))
db = conn.cursor()

#Insertion des données
for req in arrayInserts:
    db.execute(req)

db.commit()

#Affichage de l'intégralité de la bdd

db.execute("select * from astroids")
print(db.fecthall())
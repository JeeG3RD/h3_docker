import pandas as pd
from classes.db import *

df_nasa = pd.read_csv("df_nasa/nasa.csv")

df_nasa = df_nasa.drop(['Est Dia in KM(min)', 'Est Dia in KM(max)', 'Est Dia in M(min)', 'Est Dia in M(max)', 'Est Dia in Feet(min)', 'Est Dia in Feet(max)', 'Miss Dist.(Astronomical)', 'Miss Dist.(lunar)', 'Miss Dist.(kilometers)', "Relative Velocity km per sec", "Equinox", "Orbiting Body"], axis="columns")

for (colName, coldf_nasa) in df_nasa.iteritems():
    df_nasa = df_nasa.rename(columns={colName :colName.replace(" ", "")})

myDb = DB("root", "azerty", "localhost")

myDb.connect()

myDb.createDB()
myDb.importData()

arrayInserts = []

for i in range(0, (df_nasa.shape[0])):

    req = "Insert into asteroids values(NULL,"

    for each in df_nasa.columns:
        if (each == "CloseApproachDate" or each == "OrbitDeterminationDate"):
            req += "'" + str(df_nasa.loc[i][each]) + "'"
        else:
            req += str(df_nasa.loc[i][each])
        
        if (each != "Hazardous"):
            req += ","
    
    req += ")"
    arrayInserts.append(req)

for req in arrayInserts:
    myDb.execQuery(req)






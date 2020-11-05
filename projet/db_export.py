import pandas as pd
from classes.db import *

myDb = DB("root", "azerty", "localhost")

myDb.connect_db("nasa")

sqlData = myDb.exportData("asteroids")
columns = myDb.getColumns("nasa")

newDF = pd.DataFrame(sqlData)

index = 0;
for each in newDF.columns:
    newDF = newDF.rename(columns={each: columns[index]})
    index+=1

newDF = newDF.drop("Id", axis="columns")



newDF.to_csv ('data/exports/export_nasa.csv', index = False) # place 'r' before the path name to avoid any errors in the path

#print(newDF.info())
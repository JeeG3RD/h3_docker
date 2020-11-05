import pandas as pd
import joblib
import uvicorn
import json
from fastapi import FastAPI

api = FastAPI()

knn_model = joblib.load("knn_model.plk")
rfc_model = joblib.load("rfc_model.plk")

@api.get("/")
async def home():
    return "Fast API - Nasa Astroids / Gerdy Jérome - H3 Hitema"

@api.get("/knn")
async def knn_predict(MinimumOrbitIntersection : float=None, EstDiainMiles_min:float=None, EstDiainMiles_max:float=None, AbsoluteMagnitude:float=None, OrbitID:int=None):
    data = {
        "MinimumOrbitIntersection": [MinimumOrbitIntersection],
        "EstDiainMiles(min)" : [EstDiainMiles_min],
        "EstDiainMiles(max)" : [EstDiainMiles_max],
        "AbsoluteMagnitude" : [AbsoluteMagnitude],
        "OrbitID" : [OrbitID]
        }
    

    df = pd.DataFrame(data)
    pred = knn_model.predict(df)
    proba = knn_model.predict_proba(df)

    if pred == 1:
        danger="oui"
    else:
        danger="non"

    proba_danger = float(proba[0,1])

    result = {
        "asteroide_dangereux": danger,
        "risque_dangereux": str(round(proba_danger*100, 2)) + " %"
    }
    return json.loads(json.dumps(result))

@api.get("/rfc")
async def rfc_predict(MinimumOrbitIntersection : float=None, EstDiainMiles_min:float=None, EstDiainMiles_max:float=None, AbsoluteMagnitude:float=None, OrbitID:int=None):
    data = {
        "MinimumOrbitIntersection": [MinimumOrbitIntersection],
        "EstDiainMiles(min)" : [EstDiainMiles_min],
        "EstDiainMiles(max)" : [EstDiainMiles_max],
        "AbsoluteMagnitude" : [AbsoluteMagnitude],
        "OrbitID" : [OrbitID]
        }
    

    df = pd.DataFrame(data)
    pred = rfc_model.predict(df)
    proba = rfc_model.predict_proba(df)

    if pred == 1:
        danger="oui"
    else:
        danger="non"

    proba_danger= float(proba[0,1])

    result = {
        "asteroide_dangereux": danger,
        "risque_dangereux": str(round(proba_danger*100, 2)) + " %"
    }
    return json.loads(json.dumps(result))

#uvicorn.run(api, host="0.0.0.1", port="5000")
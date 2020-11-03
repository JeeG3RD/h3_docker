from fastapi import FastAPI
import uvicorn
import joblib
import json

myApp = FastAPI()

#reutilisation du model entrainé dans le tp 2
model = joblib.load("model.pkl")

@myApp.get("/")
def home():
    return("Hello World")

# Définition de la route /prediction


@myApp.get("/prediction")
async def returnPred(text: str = None): #L'URL devra etre sous form 127.0.0.1/predictions?text=valeur
    pred = model.predict_proba([text])[0]

    #Conversion des  données au format JSON
    results = {
        "hate_speech": round(pred[0]*100, 2),
        "offensive_language": round(pred[1]*100, 2),
        "neither": round(pred[2]*100, 2)
    }

    results_json = json.dumps(results)

    #Retour du JSON
    return json.loads(results_json)


uvicorn.run(myApp, host="127.0.0.1", port="8000")
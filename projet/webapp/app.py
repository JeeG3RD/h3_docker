import streamlit
import joblib
import pandas as pd
#import 
knn_model = joblib.load("knn_model.plk")
rfc_model = joblib.load("rfc_model.plk")
#Import du modèle entrainé


#Récupération de la saisie utilisateur
input_M_O_I = streamlit.text_input("Minimum Orbit Intersection :", "")
input_E_D_MIN = streamlit.text_input("Est Dia in Miles Min :", "")
input_E_D_MAX = streamlit.text_input("Est Dia in Miles Max :", "")
input_A_M = streamlit.text_input("Absolute Magnitude :", "")
input_O_I = streamlit.text_input("Orbit ID :", "")

btn_KNN = streamlit.button("Prédiction de KNN")
btn_RFC = streamlit.button("Prédiction de RFC")

if (btn_KNN):
    streamlit.text("Prédiction de RFC")

    data = {
        "MinimumOrbitIntersection": [input_M_O_I],
        "EstDiainMiles(min)" : [input_E_D_MIN],
        "EstDiainMiles(max)" : [input_E_D_MAX],
        "AbsoluteMagnitude" : [input_A_M],
        "OrbitID" : [input_O_I]
    }

    df = pd.DataFrame(data)
    pred = knn_model.predict(df)
    proba = knn_model.predict_proba(df)

    if pred == 1:
        danger="oui"
    else:
        danger="non"

    proba_danger= float(proba[0,1])

    result = {
        "asteroide_dangereux": danger,
        "risque_dangereux": str(round(proba_danger*100, 2)) + " %"
    }

    streamlit.text("Astéroïde dangereux : " + danger)
    streamlit.text("Pourcentage de risque d'être dangereux : " + str(round(proba_danger*100, 2)) + " %")

if (btn_RFC):
    streamlit.text("Prédiction de RFC")

    data = {
        "MinimumOrbitIntersection": [input_M_O_I],
        "EstDiainMiles(min)" : [input_E_D_MIN],
        "EstDiainMiles(max)" : [input_E_D_MAX],
        "AbsoluteMagnitude" : [input_A_M],
        "OrbitID" : [input_O_I]
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

    streamlit.text("Astéroïde dangereux : " + danger)
    streamlit.text("Pourcentage de risque d'être dangereux : " + str(round(proba_danger*100, 2)) + " %")
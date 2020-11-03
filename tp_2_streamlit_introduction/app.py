import streamlit
import joblib

#Import du modèle entrainé
model = joblib.load("model.pkl")

#Récupération de la saisie utilisateur
text_input = streamlit.text_input("Saisir un texte :", "")

if(text_input):
    #Calcul de la probabilité d'offensivité du texte
    pred = model.predict_proba(text_input)


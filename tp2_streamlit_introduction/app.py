import streamlit
import joblib
#import 

#Import du modèle entrainé
model = joblib.load("model.pkl")

#Récupération de la saisie utilisateur
text_input = streamlit.text_input("Saisir un texte :", "")

if(text_input):
    #Calcul de la probabilité d'offensivité du texte
    pred = model.predict_proba([text_input])[0]

    streamlit.text("Results : ")
    streamlit.text("Hate speech : " + str(round(pred[0]*100, 2)) + " %")
    streamlit.text("Offensive language" + str(round(pred[1]*100, 2)) + " %")
    streamlit.text("Neither" + str(round(pred[2]*100, 2)) + " %")


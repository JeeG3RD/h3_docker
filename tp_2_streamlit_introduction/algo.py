import pandas as pd
import sklearn
import joblib

from sklearn.pipeline import make_pipeline
from sklearn.pipeline import make_pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

from stop_words import get_stop_words

#Import du dataset
df_labels = pd.read_csv("data/labels.csv")

#Suppression de la première colonne sans nom
df_labels = df_labels.drop(["Unnamed: 0"], axis=1)

#Suppresion des NAN
df_labels = df_labels.dropna()

#Définition de la feature et de la target
x = df_labels["tweet"]
y= df_labels["class"]

#Pipeline
clf = make_pipeline(
    TfidfVectorizer(stop_words=get_stop_words('en')),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)

#Training de l'algo
clf = clf.fit(x, y)

#Sort le fichier du model entrainé
joblib.dump(clf, "model.pkl")




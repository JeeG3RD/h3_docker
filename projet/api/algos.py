import pandas as pd
import joblib

from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../data/nasa.csv")

df = df.drop(['Est Dia in KM(min)', 'Est Dia in KM(max)', 'Est Dia in M(min)', 'Est Dia in M(max)', 'Est Dia in Feet(min)', 'Est Dia in Feet(max)', 'Miss Dist.(Astronomical)', 'Miss Dist.(lunar)', 'Miss Dist.(kilometers)', "Relative Velocity km per sec", "Equinox", "Orbiting Body"], axis="columns")
for (colName, colData) in df.iteritems():
    df = df.rename(columns={colName :colName.replace(" ", "")})

df.dropna()

df = df.apply(LabelEncoder().fit_transform)

x = df[["MinimumOrbitIntersection", "EstDiainMiles(min)", "EstDiainMiles(max)", "AbsoluteMagnitude", "OrbitID"]]
y = df["Hazardous"]


knn = KNN(n_neighbors=5, weights="distance", p=1)
knn.fit(x,y)

joblib.dump(knn, "knn_model.plk")

rfc = RFC()
rfc.fit(x,y)

joblib.dump(rfc, "rfc_model.plk")



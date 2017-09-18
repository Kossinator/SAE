from ML3.eigeneKI import KNN_Classifier
from ML2.aufgabeB import read_csv


data = read_csv("../data/ML_2.csv")

clf = KNN_Classifier(5)

X = []
y = []

for d in data:
    X.append([d[0], d[1]])
    y.append(d[2])

clf.fit(X, y)

print(clf.predict([[60, 2]]))
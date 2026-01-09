import csv
from sklearn.neural_network import MLPClassifier

X = []
Y = []

cesta = r"3. strojove_uceni\data\bmi.csv"

with open(cesta, "r", encoding="utf-8") as file:
    for radek in csv.DictReader(file):
        Y.append(int(radek["Index"]))

        if radek["Gender"] == "Male":
            gender = 0
        else:
            female = 1

        height = int(radek["Height"])
        weight = int(radek["Weight"])

        X.append([gender, height, weight])

X_train = X[:round(0.8*len(X))] 
Y_train = Y[:round(0.8*len(Y))] 

X_test = X[round(0.8*len(X)):]
Y_test = Y[round(0.8*len(Y)):]

sit = MLPClassifier(
    hidden_layer_sizes=(5,4,2),
    activation="relu",
    max_iter=1_000
)

sit.fit(X_train, Y_train)

predikce = print(sit.predict(X_test))

pocet = len(predikce)

spravne = 0

for i in range(pocet):
    if predikce[i] == Y_test[i]:
        spravne += 1
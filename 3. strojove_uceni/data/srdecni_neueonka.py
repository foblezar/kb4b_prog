import csv

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix


X = []  
Y = []  

with open("3. strojove_uceni/data/heart.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        age = int(row["age"])
        sex = int(row["sex"])
        cp = int(row["cp"])
        trestbps = int(row["trestbps"])
        chol = int(row["chol"])
        fbs = int(row["fbs"])
        exang = int(row["exang"])
        oldpeak = float(row["oldpeak"])
        slope = int(row["slope"])
        ca = int(row["ca"]) 
        thal= int(row["thal"])

        heart_disease = int(row["heart_disease"])

        X.append([age, sex, cp, trestbps, chol, fbs, exang, oldpeak, slope, ca, thal])
        Y.append(heart_disease)


# ---------- Ruční rozdělení na trénování a testování ----------
rows = len(X)
split = round(0.8 * rows)

trening_X = X[:split]
trening_Y = Y[:split]

test_X = X[split:]
test_Y = Y[split:]


neural_network = MLPClassifier(
    hidden_layer_sizes=(14, 8, 8, 8),
    activation="relu",
    max_iter=1000,
    random_state=4
)

neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print(f"Procento spravnych odpovedi: {correct / len(results)*100}%")

print(confusion_matrix(test_Y, results))


import csv


from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


X = []  
Y = []  

with open("uciml/mushroom-classification", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cap_surface = float(row["cap-surface"])
        cap_color = float(row["cap-color"])

        if row[""] == "":
            cap_shape = "f"
        else:
            gcap_shape = "x"

        mushroom_category = int(row["Index"])

        X.append([gender, height, weight])
        Y.append(mushroom_category)



trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42)


neural_network = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    activation="relu",
    max_iter=2000,
    verbose=True,
    random_state=4
)

neural_network.fit(trening_X, trening_Y)


results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))


ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()

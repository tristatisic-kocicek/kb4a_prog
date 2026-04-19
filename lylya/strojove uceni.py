import csv
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

X = []  
Y = []  

with open("../uciml/mushroom-classification", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cap_color = float(row["cap-color"])
        cap_surface = float(row["cap-surface"])
        gill_color = float(row["gill-color"])
        gill_size = float(row["gill-size"])
        stalk_color = float(row["stalk-color"])
        veil_type = float(row["veil-type"])
        odor = float(row["odor"])

        cap_shape = int(row["cap-shape"])

        X.append([cap_color, cap_surface, gill_color, gill_size, stalk_color, veil_type, odor])
        Y.append(cap_shape)

trening_X, test_X, trening_Y, test_Y = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42
)

neural_network = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    max_iter=2000,
    verbose=True,
    random_state=42
)

neural_network.fit(trening_X, trening_Y)

results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1

print(f"Přesnost modelu: {correct / len(results) * 100:.2f}%")
print(f"Správně klasifikováno: {correct}/{len(results)}")

ConfusionMatrixDisplay.from_predictions(test_Y, results)
plt.title("Confusion Matrix - Predikce Typu Čepice Houby")
plt.show()

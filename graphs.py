import matplotlib.pyplot as plt
import pandas as pd

from pvt import detect_pvt
from structure_detection import detect_structure
from hybrid_model import hybrid_detect

# ----------------------------
# LOAD DATA
# ----------------------------
data = pd.read_csv("dataset.csv", on_bad_lines='skip')

queries = data["query"]
labels = data["label"]

design_query = "SELECT * FROM users WHERE id=?"

# ----------------------------
# PREDICTIONS
# ----------------------------
pvt_pred = []
struct_pred = []
hybrid_pred = []

for q in queries:
    pvt_pred.append(detect_pvt(q))
    struct_pred.append(detect_structure(design_query, q))
    hybrid_pred.append(hybrid_detect(q))

# ----------------------------
# ACCURACY FUNCTION
# ----------------------------
def calculate_accuracy(true, pred):
    correct = 0
    for i in range(len(true)):
        if true[i] == pred[i]:
            correct += 1
    return correct / len(true)

# ----------------------------
# CALCULATE ACCURACY
# ----------------------------
pvt_acc = calculate_accuracy(labels, pvt_pred)
struct_acc = calculate_accuracy(labels, struct_pred)
hybrid_acc = calculate_accuracy(labels, hybrid_pred)

# parameterized → assumed perfect prevention
param_acc = 1.0

methods = ["PVT", "Structure", "Hybrid","Parameterized"]
scores = [pvt_acc, struct_acc, hybrid_acc, param_acc]

# ----------------------------
# PLOT 1: Detection Rate
# ----------------------------
plt.figure()

bars = plt.bar(methods, scores)

plt.title("Detection / Prevention Effectiveness Comparison")
plt.ylabel("Accuracy")

#  ADD % LABELS
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.02,
        f"{height*100:.1f}%",
        ha='center',
        fontsize=10,
        fontweight='bold'
    )

plt.ylim(0, 1.1)

plt.show()
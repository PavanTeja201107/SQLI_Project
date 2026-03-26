import pandas as pd
import time
import warnings
from sklearn.exceptions import UndefinedMetricWarning

warnings.filterwarnings("ignore", category=UndefinedMetricWarning)
from sklearn.metrics import confusion_matrix, classification_report

from pvt import detect_pvt
from structure_detection import detect_structure
from parameterized_query import safe_query
from hybrid_model import hybrid_detect

# Load dataset
data = pd.read_csv("dataset.csv")

queries = data["query"]
labels = data["label"]

design_query = "SELECT * FROM users WHERE id=?"

# Predictions
pvt_pred = []
struct_pred = []
param_pred = []
hybrid_pred = []

# Runtime trackers
pvt_time = 0
struct_time = 0
param_time = 0
hybrid_time = 0

# Run experiments
for q in queries:

    # PVT
    start = time.perf_counter()
    pvt_pred.append(detect_pvt(q))
    pvt_time += time.perf_counter() - start

    # Structure
    start = time.perf_counter()
    struct_pred.append(detect_structure(design_query, q))
    struct_time += time.perf_counter() - start

    # Parameterized (execution time only)
    data_result, runtime = safe_query(1)
    param_pred.append(0)   # always safe (prevention)
    param_time += runtime

    # Hybrid (multi-class)
    start = time.perf_counter()
    hybrid_pred.append(hybrid_detect(q))
    hybrid_time += time.perf_counter() - start

# -----------------------------
# Runtime Results
# -----------------------------
print("\n--- Runtime Comparison ---")
print("PVT runtime:", pvt_time)
print("Structure runtime:", struct_time)
print("Parameterized runtime:", param_time)
print("Hybrid runtime:", hybrid_time)

# -----------------------------
# Evaluation (Hybrid Model)
# -----------------------------
print("\n---- Hybrid Model Evaluation ----")

cm = confusion_matrix(labels, hybrid_pred, labels=[0,1,2])
print("\nConfusion Matrix:\n", cm)

print("\nClassification Report:\n")
print(classification_report(labels, hybrid_pred, target_names=["Normal","SQLi","XSS"]))
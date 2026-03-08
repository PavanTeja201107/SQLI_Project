import pandas as pd
import time
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from pvt import detect_pvt
from structure_detection import detect_structure
from parameterized_query import safe_query
from hybrid_model import hybrid_detect

data = pd.read_csv("dataset.csv")

queries = data["query"]
labels = data["label"]

design_query = "SELECT * FROM users WHERE id=?"

pvt_pred = []
struct_pred = []
param_pred = []
hybrid_pred = []

pvt_time = 0
struct_time = 0
param_time = 0
hybrid_time = 0

for q in queries:

    start=time.perf_counter()
    pvt_pred.append(detect_pvt(q))
    pvt_time+=time.perf_counter()-start

    start=time.perf_counter()
    struct_pred.append(detect_structure(design_query,q))
    struct_time+=time.perf_counter()-start

    data_result, runtime = safe_query(1)
    param_pred.append(0)
    param_time += runtime

    start=time.perf_counter()
    hybrid_pred.append(hybrid_detect(q))
    hybrid_time+=time.perf_counter()-start

print("\n--- Runtime Comparison ---")

print("PVT runtime:",pvt_time)
print("Structure runtime:",struct_time)
print("Parameterized runtime:",param_time)
print("Hybrid runtime:",hybrid_time)

print("\n---- Hybrid Model Evaluation ----")

cm = confusion_matrix(labels, hybrid_pred)

precision = precision_score(labels, hybrid_pred)

recall = recall_score(labels, hybrid_pred)

print("Confusion Matrix:\n", cm)

print("Precision:", precision)

print("Recall:", recall)
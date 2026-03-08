# Hybrid SQL Injection Detection System

## Project Description
This project demonstrates a **Hybrid SQL Injection Detection System** that detects SQL injection attacks in a web application using three algorithmic techniques:

1. **Pattern Validation Technique (PVT)** – Detects common SQL injection patterns such as `' OR 1=1`, `--`, and `UNION SELECT`.
2. **Structure Comparison** – Compares the expected SQL query structure with the runtime query using keyword vectors and similarity analysis.
3. **Parameterized Query** – Prevents SQL injection by separating SQL query logic from user inputs.

A **Hybrid Model** combines these techniques to improve detection accuracy. The project also includes:
- A vulnerable Flask login web application
- Real-time SQL injection detection
- Attack logging (`attack_log.txt`)
- Security dashboard showing detected attacks
- Experimental evaluation with a dataset of SQL queries

---

## Steps to Run the Project

### 1. Install Required Libraries

pip install flask pandas numpy matplotlib scikit-learn

### 2. Generate SQL Query Dataset

python dataset_generator.py

This creates `dataset.csv` containing normal and SQL injection queries.

### 3. Run Algorithm Evaluation

python experiment.py

This evaluates the detection algorithms and prints runtime, confusion matrix, precision, and recall.

### 4. Generate Performance Graphs

python graphs.py

This displays graphs comparing detection rate, recall, and runtime.

### 5. Run the Web Application Demo

cd flask_demo
python app.py

Open in browser: http://127.0.0.1:5000

---

## Testing

### Normal Login

username: admin
password: admin123

Result → **Login Successful**

### SQL Injection Attack

username: admin' --
password: anything

Result → **SQL Injection Attack Detected**

Detected attacks are stored in: attack_log.txt

---

## Security Dashboard
View detected attacks at:

http://127.0.0.1:5000/dashboard

The dashboard displays the total number of detected attacks and the logged attack queries.

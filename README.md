# Hybrid Web Attack Detection System (SQLi + XSS)

## Project Description
This project implements a **Hybrid Web Attack Detection System** capable of detecting:

- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)

using multiple algorithmic techniques combined into a **hybrid model**.

---

## Techniques Used

1. **Pattern Validation Technique (PVT)**  
   Detects known malicious patterns such as:
   - `' OR 1=1`
   - `--`
   - `UNION SELECT`
   - script-based payloads (XSS)

2. **Structure Comparison (Vector + Cosine Similarity)**  
   Compares expected SQL query structure with runtime query using:
   - weighted keyword vectors
   - cosine similarity (angle-based detection)

3. **Parameterized Queries**  
   Prevents SQL injection by separating SQL logic from user input.

4. **XSS Detection Module**  
   Detects malicious script patterns such as:
   - `<script>`
   - `onerror=`
   - `alert()`

---

## Hybrid Model

The hybrid model combines all techniques:

- SQL Injection → detected using PVT + Structure
- XSS → detected using script pattern matching
- Final classification:
    0 → Normal
    1 → SQL Injection
    2 → XSS
---

---

## Features

- Real-time attack detection
- Multi-class classification (Normal / SQLi / XSS)
- Attack logging (`attack_log.txt`)
- Secure login using parameterized queries
- Flask-based web application demo
- Security dashboard
- Performance evaluation using:
- Runtime
- Confusion matrix
- Precision / Recall / F1-score

---

## Steps to Run the Project

### 1. Install Required Libraries

pip install flask pandas numpy matplotlib scikit-learn

### 2. Generate SQL Query Dataset

python dataset_generator.py

This creates `dataset.csv` containing normal and SQL injection and XSS queries.

### 3. Run Algorithm Evaluation

python experiment.py

This evaluates the detection algorithms and prints runtime, confusion matrix, precision, and recall.

Outputs:
- Runtime comparison (PVT, Structure, Parameterized, Hybrid)
- Confusion matrix
- Classification report

---

### 4. Generate Performance Graphs

python graphs.py
Displays:
- Detection accuracy
- Runtime comparison

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

### XSS Attack

username: <script>alert(1)</script>
password: anything

Result → 🚨 XSS Attack Detected

---

Result → **SQL Injection Attack Detected**

Detected attacks are stored in: attack_log.txt

---

## Security Dashboard
View detected attacks at:

http://127.0.0.1:5000/dashboard

The dashboard displays the total number of detected attacks and the logged attack queries.


---

## Conclusion

This project demonstrates how combining multiple algorithmic techniques improves detection accuracy for web attacks. The hybrid approach successfully detects both SQL injection and XSS attacks while minimizing false positives.

---

## Future Work

- Add DoS attack detection
- Real-time monitoring dashboard
- Machine learning-based detection
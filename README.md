# Hybrid SQL Injection Detection System

## Project Description
This project demonstrates a **Hybrid SQL Injection Detection System** that detects SQL injection attacks in a web application using three algorithmic techniques:

1. **Pattern Validation Technique (PVT)** – Detects common SQL injection patterns such as `' OR 1=1`, `--`, and `UNION SELECT`.
2. **Structure Comparison** – Compares the expected SQL query structure with the runtime query using keyword vectors and similarity analysis.
3. **Parameterized Query** – Prevents SQL injection by separating SQL query logic from user inputs.

A **Hybrid Model** combines these techniques to improve detection accuracy.

---

##  NEW EXTENSIONS (END-SEM FEATURES)

This project has been extended beyond SQL Injection detection to include:

### 1️⃣ Cross-Site Scripting (XSS) Detection
- Detects malicious JavaScript payloads such as:
  - `<script>alert(1)</script>`
  - `<img onerror=alert(1)>`
- Uses pattern-based filtering for suspicious HTML/JS tags
- Integrated into hybrid model

---

### 2️⃣ Denial of Service (DoS) Detection
- Detects high-frequency request bursts from the same IP
- Uses **Sliding Window Algorithm**
- Tracks requests in real-time

---

### 3️⃣ Sliding Window Algorithm (Advanced)
- Maintains timestamps of requests per IP
- Removes outdated requests dynamically
- Detects bursts accurately without resetting counters

 Logic:
Only requests within last TIME_WINDOW seconds are considered

---

### 4️⃣ IP Blacklisting System
- Automatically blocks IPs exceeding request threshold
- Stores:
  - IP Address
  - Request Count
  - Timestamp

 Stored in:
blocked_ips_log.txt

---

### 5️⃣ DoS Attack Simulator
- Simulates real attack traffic using multiple IPs
- Sends repeated requests using headers:
X-Forwarded-For
- Helps test detection system effectively

---

### 6️⃣ Security Dashboard Enhancement
Dashboard now shows:
- Detected SQL Injection attacks
- Detected XSS attacks
- Detected DoS attacks
- Blocked IP addresses with request count

---

## 🧠 System Architecture

User Input  
↓  
DoS Detection (Sliding Window)  
↓  
SQLi + XSS Hybrid Detection  
↓  
Safe Query Execution  
↓  
Logging + Dashboard  

---

##  Steps to Run the Project

### 1. Install Required Libraries

pip install flask pandas numpy matplotlib scikit-learn requests

---

### 2. Generate SQL Query Dataset

python dataset_generator.py

This creates `dataset.csv` containing:
- Normal queries
- SQL Injection queries
- XSS queries

---

### 3. Run Algorithm Evaluation

python experiment.py

Outputs:
- Runtime comparison
- Confusion matrix
- Accuracy metrics

---

### 4. Generate Performance Graphs

python graphs.py

Displays:
- Detection rate
- Recall
- Runtime comparison

---

### 5. Run the Web Application

cd flask_demo  
python app.py  

Open browser:  
http://127.0.0.1:5000  

---

### 6. Simulate DoS Attack

python dos_simulator.py

This sends multiple rapid requests from simulated IPs.

---

##  Testing Scenarios

###  Normal Login

username: admin  
password: admin123  

Result → Login Successful  

---

###  SQL Injection Attack

username: admin' --  
password: anything  

Result → SQL Injection Attack Detected  

---

###  XSS Attack

username: `<script>alert(1)</script>`  
password: test  

Result → XSS Attack Detected  

---

###  DoS Attack

Run:
python dos_simulator.py  

Result → DoS Attack Detected  

---

##  Security Dashboard

View detected attacks at:  
http://127.0.0.1:5000/dashboard  

Displays:
- Total number of detected attacks
- Logged attack queries
- Blocked IP list

---

##  Logs

### Attack Log
attack_log.txt  
Stores:
- SQLi / XSS / DoS attacks  

---

### Blocked IP Log
blocked_ips_log.txt  
Stores:
- IP address  
- Number of requests  
- Timestamp  

---

##  Key Concepts Used

- Pattern Matching (Regex)  
- Vector-based Structure Comparison  
- Sliding Window Algorithm  
- Rate Limiting  
- IP Blacklisting  
- Secure Query Execution (Parameterized Queries)  

---

##  Advantages of Hybrid Model

- Higher detection accuracy  
- Reduced false positives  
- Multi-layer security  
- Real-time attack detection  

---

##  Limitations

- Does not fully handle distributed (DDoS) attacks  
- Rule-based (no machine learning adaptation)  
- Depends on threshold tuning  

---

## 🔮 Future Enhancements

- Machine Learning-based anomaly detection  
- Real-time visualization dashboard  
- Token Bucket algorithm for rate limiting  
- Distributed attack detection  
- Auto IP unblocking mechanism  

---

## 📌 Conclusion

This project demonstrates a complete web security framework capable of detecting multiple types of attacks in real-time with high accuracy using lightweight algorithmic techniques.
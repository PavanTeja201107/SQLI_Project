import random
import pandas as pd

# Normal queries
normal_queries = [
    "SELECT * FROM users WHERE id=1",
    "SELECT * FROM users WHERE username='admin'",
    "SELECT * FROM products WHERE price=100",
    "SELECT name FROM users WHERE id=5"
]

# SQL Injection queries
sqli_queries = [
    "SELECT * FROM users WHERE id=1 OR 1=1",
    "SELECT * FROM users WHERE username='admin'--",
    "SELECT * FROM users WHERE id=1 OR 'a'='a'",
    "SELECT * FROM users WHERE id=2 UNION SELECT password FROM users",
    "SELECT * FROM users WHERE id=5; DROP TABLE users"
]

# XSS queries
xss_queries = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<body onload=alert(1)>",
    "<script>document.cookie</script>"
]

data = []

# Generate 300 each
for i in range(300):
    data.append([random.choice(normal_queries), 0])

for i in range(300):
    data.append([random.choice(sqli_queries), 1])

for i in range(300):
    data.append([random.choice(xss_queries), 2])

# Shuffle dataset
random.shuffle(data)

df = pd.DataFrame(data, columns=["query", "label"])

df.to_csv("dataset.csv", index=False)

print("Dataset generated with 900 queries (Normal + SQLi + XSS)")
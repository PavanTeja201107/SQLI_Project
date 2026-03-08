import random
import pandas as pd

normal_queries = [
"SELECT * FROM users WHERE id=1",
"SELECT * FROM users WHERE id=5",
"SELECT name FROM users WHERE id=10",
"SELECT * FROM products WHERE price=100",
"SELECT email FROM users WHERE id=3"
]

injection_queries = [
"SELECT * FROM users WHERE id=1 OR 1=1",
"SELECT * FROM users WHERE name='admin'--",
"SELECT * FROM users WHERE id=2 UNION SELECT password FROM users",
"SELECT * FROM users WHERE id=1 OR 'a'='a'",
"SELECT * FROM users WHERE id=5; DROP TABLE users"
]

data = []

for i in range(500):

    q = random.choice(normal_queries)
    data.append([q,0])

for i in range(500):

    q = random.choice(injection_queries)
    data.append([q,1])

random.shuffle(data)

df = pd.DataFrame(data,columns=["query","label"])

df.to_csv("dataset.csv",index=False)

print("Dataset created with",len(df),"queries")
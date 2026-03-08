import re

patterns = [
    r"--",
    r"or\s+1=1",
    r"union\s+select",
    r"drop\s+table",
    r"'\s*or\s*'",
]

def detect_pvt(query):

    query = query.lower()

    for pattern in patterns:

        if re.search(pattern, query):
            return 1

    return 0
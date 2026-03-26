import re

patterns = [
    r"--",
    r"\bor\s+1=1\b",
    r"\bunion\s+select\b",
    r"\bdrop\s+table\b",
    r"'\s*or\s*'",
    r"\bor\b",
    r"\band\b"
]

def detect_pvt(query):

    query = query.lower()

    for pattern in patterns:
        if re.search(pattern, query):
            return 1

    return 0
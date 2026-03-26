import re

def detect_xss(input_text):

    input_text = input_text.lower()

    patterns = [
        r"<script.*?>.*?</script>",
        r"onerror\s*=",
        r"onload\s*=",
        r"alert\s*\(",
        r"javascript:",
        r"<img.*?>",
        r"<iframe.*?>"
    ]

    for pattern in patterns:
        if re.search(pattern, input_text):
            return 1

    return 0
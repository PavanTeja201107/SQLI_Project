import numpy as np
import math

def extract_keywords(query):

    keywords = ["select", "from", "where", "union", "drop", "or"]

    query = query.lower()

    return [k for k in keywords if k in query]


def detect_structure(design_query, runtime_query):

    design_k = extract_keywords(design_query)
    runtime_k = extract_keywords(runtime_query)

    # count extra suspicious keywords
    extra = len(set(runtime_k) - set(design_k))

    if extra >= 2:
        return 1

    return 0
import numpy as np
import math

keywords = {
"select":3,
"from":1,
"where":1,
"union":3,
"drop":5,
"and":2,
"or":2
}

def extract_vector(query):

    query = query.lower()

    vector = []

    for word in keywords:
        vector.append(query.count(word) * keywords[word])

    return np.array(vector)


def detect_structure(design_query, runtime_query):

    dv = extract_vector(design_query)
    rv = extract_vector(runtime_query)

    dot = np.dot(dv, rv)

    mag1 = np.linalg.norm(dv)
    mag2 = np.linalg.norm(rv)

    if mag1 == 0 or mag2 == 0:
        return 0

    cos = dot / (mag1 * mag2)

    angle = math.degrees(math.acos(cos))

    if angle > 25:
        return 1

    return 0
from pvt import detect_pvt
from structure_detection import detect_structure

design_query = "SELECT * FROM users WHERE username=? AND password=?"

def hybrid_detect(query):

    pvt_result = detect_pvt(query)

    structure_result = detect_structure(design_query, query)

    # Only detect injection if BOTH detect suspicious behaviour

    if pvt_result == 1 or structure_result == 1:
        return 1

    return 0
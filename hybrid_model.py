from pvt import detect_pvt
from structure_detection import detect_structure
from xss_detection import detect_xss
design_query = "SELECT * FROM users WHERE username=? AND password=?"

def hybrid_detect(query):

    pvt_result = detect_pvt(query)
    structure_result = detect_structure(design_query, query)
    xss_result = detect_xss(query)

    if xss_result == 1:
        return 2   # XSS

    if pvt_result == 1 or structure_result == 1:
        return 1   # SQLi

    return 0       # SAFE
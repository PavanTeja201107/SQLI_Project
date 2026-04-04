from pvt import detect_pvt
from structure_detection import detect_structure
from xss_detection import detect_xss
from dos_detection import detect_dos
design_query = "SELECT * FROM users WHERE username=? AND password=?"

def hybrid_detect(query, ip=None):

    pvt_result = detect_pvt(query)
    structure_result = detect_structure(design_query, query)
    xss_result = detect_xss(query)

    # XSS
    if xss_result == 1:
        return 2

    # SQLi
    if pvt_result == 1 or structure_result == 1:
        return 1

    # DoS (only if IP provided)
    if ip is not None:
        if detect_dos(ip) == 1:
            return 3   # DoS

    return 0
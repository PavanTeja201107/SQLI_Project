import time

request_log = {}
blocked_ips = {}

TIME_WINDOW = 5
MAX_REQUESTS = 5

def detect_dos(ip):

    current_time = time.time()

    # 🚨 already blocked
    if ip in blocked_ips:
        return 2, blocked_ips[ip]["count"]

    # initialize
    if ip not in request_log:
        request_log[ip] = []

    # add request
    request_log[ip].append(current_time)

    # sliding window cleanup
    request_log[ip] = [
        t for t in request_log[ip]
        if current_time - t <= TIME_WINDOW
    ]

    # 🚨 threshold exceeded
    if len(request_log[ip]) > MAX_REQUESTS:

        blocked_ips[ip] = {
            "count": len(request_log[ip]),
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        return 1, len(request_log[ip])

    return 0, 0
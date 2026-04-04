import time

request_log = {}
blocked_ips = {}

TIME_WINDOW = 5
MAX_REQUESTS = 5
BLOCK_TIME = 10   # ⬅️ unblock after 10 seconds


def detect_dos(ip):

    current_time = time.time()

    # ----------------------------------------
    # 🧹 REMOVE OLD BLOCKED IPS
    # ----------------------------------------
    if ip in blocked_ips:
        blocked_time = blocked_ips[ip]["blocked_at"]

        if current_time - blocked_time > BLOCK_TIME:
            del blocked_ips[ip]   # ✅ UNBLOCK
        else:
            return 2, blocked_ips[ip]["count"]

    # ----------------------------------------
    # INIT
    # ----------------------------------------
    if ip not in request_log:
        request_log[ip] = []

    request_log[ip].append(current_time)

    # ----------------------------------------
    # SLIDING WINDOW CLEANUP
    # ----------------------------------------
    request_log[ip] = [
        t for t in request_log[ip]
        if current_time - t <= TIME_WINDOW
    ]

    # ----------------------------------------
    # 🚨 THRESHOLD CHECK
    # ----------------------------------------
    if len(request_log[ip]) > MAX_REQUESTS:

        blocked_ips[ip] = {
            "count": len(request_log[ip]),
            "blocked_at": current_time
        }

        return 1, len(request_log[ip])

    return 0, 0
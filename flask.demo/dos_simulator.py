import requests
import time

URL = "http://127.0.0.1:5000"

# use sequential IPs
for i in range(1, 6):   # 5 IPs

    ip = f"192.168.1.{i}"

    print(f"\n--- Attacking with IP: {ip} ---")

    # send multiple requests from SAME IP
    for j in range(7):   # exceed MAX_REQUESTS (5)

        headers = {
            "X-Forwarded-For": ip
        }

        try:
            requests.get(URL, headers=headers)
            print(f"Request {j+1} from {ip}")
        except:
            pass

        time.sleep(0.2)
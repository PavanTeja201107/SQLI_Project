import sys
import os
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from flask import redirect, url_for
from flask import Flask, render_template, request
import sqlite3

from hybrid_model import hybrid_detect
from dos_detection import detect_dos

app = Flask(__name__)

LOG_FILE = "../attack_log.txt"


# ----------------------------------------
# LOGGING FUNCTIONS
# ----------------------------------------
def log_attack(query):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {query}\n")


def log_blocked_ip(ip, count):
    with open("../blocked_ips_log.txt", "a") as f:
        f.write(f"{ip} | Requests={count} | Time={datetime.datetime.now()}\n")


# ----------------------------------------
# GLOBAL DoS DETECTION
# ----------------------------------------
@app.before_request
def check_dos():

    # ✅ ONLY apply DoS to login route
    if request.path != "/":
        return

    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    status, count = detect_dos(ip)

    if status == 1:
        log_attack(f"DoS | IP={ip}")
        log_blocked_ip(ip, count)
        return render_template("login.html", alert=True, success=False)

    elif status == 2:
        return render_template("login.html", alert=True, success=False)

# ----------------------------------------
# LOGIN ROUTE
# ----------------------------------------

@app.route("/", methods=["GET", "POST"])
def login():

    alert = request.args.get("alert") == "1"
    success = request.args.get("success") == "1"

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # ----------------------------
        # STEP 1: SAFE LOGIN CHECK
        # ----------------------------
        conn = sqlite3.connect("../database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        result = cursor.fetchall()
        conn.close()

        if result:
            return redirect(url_for("login", success=1))

        # ----------------------------
        # STEP 2: ATTACK DETECTION
        # ----------------------------
        query = username + " " + password
        attack_type = hybrid_detect(query)

        if attack_type != 0:

            if attack_type == 1:
                attack_name = "SQLi"
            elif attack_type == 2:
                attack_name = "XSS"

            log_attack(f"{attack_name} | {query}")

            return redirect(url_for("login", alert=1))

        # ----------------------------
        # STEP 3: NORMAL WRONG LOGIN
        # ----------------------------
        return redirect(url_for("login"))

    return render_template("login.html", alert=alert, success=success)

# ----------------------------------------
# DASHBOARD
# ----------------------------------------
@app.route("/dashboard")
def dashboard():

    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()

    with open(LOG_FILE) as f:
        attacks = f.readlines()

    if not os.path.exists("../blocked_ips_log.txt"):
        open("../blocked_ips_log.txt", "w").close()

    with open("../blocked_ips_log.txt") as f:
        blocked = f.readlines()

    attacks.reverse()
    blocked.reverse()

    return render_template("dashboard.html",
                           attacks=attacks,
                           blocked=blocked,
                           count=len(attacks))


# ----------------------------------------
# RUN
# ----------------------------------------
app.run(debug=True)
import sys
import os
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask,render_template,request
import sqlite3

from hybrid_model import hybrid_detect

app = Flask(__name__)

LOG_FILE = "../attack_log.txt"


def log_attack(query):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE,"a") as f:
        f.write(f"{timestamp} | {query}\n")


@app.route("/",methods=["GET","POST"])

def login():

    alert = False
    success = False

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

        # ✅ VALID USER → LOGIN SUCCESS
        if result:
            return render_template("login.html", alert=False, success=True)

        # ----------------------------
        # STEP 2: ATTACK DETECTION
        # ----------------------------
        query = username + " " + password

        attack_type = hybrid_detect(query)

        if attack_type != 0:   # 0 = SAFE

            log_attack(f"{attack_type} | {query}")

            return render_template("login.html", alert=True, success=False)

        # ----------------------------
        # STEP 3: NORMAL WRONG LOGIN
        # ----------------------------
        return render_template("login.html", alert=False, success=False)

    return render_template("login.html", alert=False, success=False)

@app.route("/dashboard")

def dashboard():

    if not os.path.exists(LOG_FILE):
        open(LOG_FILE,"w").close()

    with open(LOG_FILE) as f:
        attacks=f.readlines()

    attacks.reverse()

    return render_template("dashboard.html",attacks=attacks,count=len(attacks))


app.run(debug=True)
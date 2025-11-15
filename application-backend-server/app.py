# application-backend-server/app.py
from flask import Flask, jsonify, request
import json
import os
import pymysql

app = Flask(__name__)

# =========================
# CẤU HÌNH DATABASE (MariaDB)
# =========================
DB_HOST = os.environ.get("DB_HOST", "relational-database-server")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASS", "root")
DB_NAME = os.environ.get("DB_NAME", "studentdb")
DB_PORT = int(os.environ.get("DB_PORT", 3306))


def get_db_conn():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME,
        port=DB_PORT,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


# =========================
# ROUTE ĐƠN GIẢN /hello
# =========================
@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from backend!"})


# =========================
# ROUTE /student (GET + POST)
# =========================
@app.route("/student", methods=["GET", "POST"])
def student():
    if request.method == "GET":
        # Read from DB
        try:
            conn = get_db_conn()
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, name, major, gpa FROM students ORDER BY id"
                )
                rows = cur.fetchall()
            conn.close()
            return jsonify(rows)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # POST -> add student to DB
    data = request.get_json(force=True)
    name = data.get("name")
    major = data.get("major")
    gpa = data.get("gpa")

    if not name or not major:
        return jsonify({"error": "name and major required"}), 400

    try:
        conn = get_db_conn()
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO students (name, major, gpa) VALUES (%s, %s, %s);",
                (name, major, float(gpa) if gpa else None),
            )
            conn.commit()
            new_id = cur.lastrowid
        conn.close()
        return (
            jsonify(
                {
                    "id": new_id,
                    "name": name,
                    "major": major,
                    "gpa": gpa,
                }
            ),
            201,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# ROUTE /secure – DEMO KEYCLOAK
# =========================
@app.route("/secure")
def secure():
    """
    Endpoint bảo vệ:
    - Nếu không có Bearer token -> 401
    - Nếu có Bearer token -> trả message OK (demo)
    """
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return jsonify({"error": "Missing Bearer token"}), 401

    token = auth.split(" ", 1)[1]

    return jsonify(
        {
            "message": "Secure resource OK",
            "token_length": len(token),
        }
    )


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)

from flask import Blueprint, request, jsonify
from app.db import get_db

data_bp = Blueprint("data", __name__)


# Insert
@data_bp.route("/api/data", methods=["POST"])
def insert_data():

    data = request.json

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return {"error": "Invalid input"}, 400

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name,email) VALUES (%s,%s)",
        (name, email)
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"message": "User added"}, 201


# Fetch
@data_bp.route("/api/data", methods=["GET"])
def fetch_data():

    conn = get_db()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows), 200

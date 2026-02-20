from flask import Blueprint, request, jsonify
from app.db import get_db

query_bp = Blueprint("query", __name__)


@query_bp.route("/api/query", methods=["POST"])
def run_query():

    data = request.json
    query = data.get("query")

    if not query:
        return {"error": "Query required"}, 400

    try:

        conn = get_db()
        cur = conn.cursor(dictionary=True)

        cur.execute(query)

        if query.lower().startswith("select"):
            result = cur.fetchall()
        else:
            conn.commit()
            result = {"rows_affected": cur.rowcount}

        cur.close()
        conn.close()

        return jsonify(result), 200

    except Exception as e:
        return {"error": str(e)}, 500

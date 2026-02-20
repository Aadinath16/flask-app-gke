from flask import Blueprint, current_app

metrics_bp = Blueprint("metrics", __name__)


@metrics_bp.route("/api/metrics/200")
def ok():

    current_app.logger.info("200 OK endpoint called")

    return {"msg": "OK"}, 200


@metrics_bp.route("/api/metrics/400")
def bad():

    current_app.logger.warning("400 Bad Request simulated")

    return {"msg": "Bad Request"}, 400


@metrics_bp.route("/api/metrics/500")
def error():

    try:
        raise Exception("Simulated Internal Server Error")

    except Exception as e:

        current_app.logger.error(
            f"500 Internal Server Error: {str(e)}",
            exc_info=True
        )

        return {"msg": "Server Error"}, 500

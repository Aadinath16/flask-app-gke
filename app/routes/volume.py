from flask import Blueprint
import os

volume_bp = Blueprint("volume", __name__)

DATA_DIR = "/data"
LOG_FILE = f"{DATA_DIR}/app.log"

os.makedirs(DATA_DIR, exist_ok=True)


def write_log(msg):

    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")


@volume_bp.route("/api/volume/write")
def write():

    write_log("Test log from volume API")

    return {"message": "Written to volume"}, 200


@volume_bp.route("/api/volume/read")
def read():

    if not os.path.exists(LOG_FILE):
        return {"logs": []}

    with open(LOG_FILE) as f:
        data = f.readlines()

    return {"logs": data}, 200

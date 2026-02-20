import mysql.connector
from flask import current_app


def get_db():

    config = current_app.config

    # Cloud SQL (Workload Identity)
    if config.get("DB_CONN_NAME"):

        return mysql.connector.connect(
            user=config["DB_USER"],
            password=config["DB_PASSWORD"],
            database=config["DB_NAME"],
            unix_socket=f"/cloudsql/{config['DB_CONN_NAME']}"
        )

    # Local / VM
    return mysql.connector.connect(
        host=config["DB_HOST"],
        port=config["DB_PORT"],
        user=config["DB_USER"],
        password=config["DB_PASSWORD"],
        database=config["DB_NAME"]
    )


# -----------------------------------
# DB Initialization (Auto Create Table)
# -----------------------------------

def init_db():

    conn = get_db()
    cursor = conn.cursor()

    # Check if table exists
    cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_schema = %s
        AND table_name = 'users'
    """, (current_app.config["DB_NAME"],))

    exists = cursor.fetchone()[0]

    if exists == 0:

        current_app.logger.info("Users table not found. Creating...")

        cursor.execute("""
            CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()

        current_app.logger.info("Users table created successfully")

    else:
        current_app.logger.info("Users table already exists")

    cursor.close()
    conn.close()

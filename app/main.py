from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
# from app.db import init_db

from flask import send_from_directory


from app.config import get_config

from app.routes.data import data_bp
from app.routes.query import query_bp
from app.routes.metrics import metrics_bp
from app.routes.volume import volume_bp
from app.logger import setup_logger



def create_app():



    app = Flask(__name__)
    app.config.from_object(get_config())
    # Setup logging
    app.logger = setup_logger()
    # Initialize database (auto-create tables)
    with app.app_context():
        init_db()




    # Prometheus
    PrometheusMetrics(app)

    # Register routes
    app.register_blueprint(data_bp)
    app.register_blueprint(query_bp)
    app.register_blueprint(metrics_bp)
    app.register_blueprint(volume_bp)

    # @app.route("/")
    # def ui():
    #     return send_from_directory("static", "index.html")

    # Health
    @app.route("/health")
    def health():
        return {"status": "UP"}, 200
        

    @app.after_request
    def log_response(response):

        code = response.status_code

        if code >= 500:
            app.logger.error(f"Response {code}")

        elif code >= 400:
            app.logger.warning(f"Response {code}")

        else:
            app.logger.info(f"Response {code}")

        return response


    return app


app = create_app()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

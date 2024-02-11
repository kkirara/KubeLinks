from flask import Flask
from flask_healthz import healthz
from kubernetes import config as kube_config

from kubelinks_app.home.routes import home_bp
import kubelinks_app.config as config


def create_app(config=config.ProdactionConfig):

    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(healthz, url_prefix="/healthz")
    app.register_blueprint(home_bp)

    try:
        kube_config.load_config()
    except Exception as e:
        app.logger.error(f'CONFIG: {e}')

    return app


if __name__ == 'main':
    app = create_app()
    app.run()

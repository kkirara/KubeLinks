from flask import Flask
from flask_healthz import healthz
from kubernetes import config as kube_config

from kubelinks_app.home.routes import home_bp
import kubelinks_app.config as config


def create_app(config=config.ProdactionConfig):

    app = Flask(__name__, static_url_path=f'{config.BASE_PATH}/static')
    app.config.from_object(config)

    app.register_blueprint(home_bp, url_prefix=config.BASE_PATH)
    app.register_blueprint(healthz, url_prefix=f"{config.BASE_PATH}/healthz")

    try:
        kube_config.load_config()
    except Exception as e:
        app.logger.error(f'CONFIG: {e}')

    return app


if __name__ == 'main':
    app = create_app()
    app.run()

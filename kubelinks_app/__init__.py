from flask import Flask
import os
from kubernetes import config
from kubelinks_app.home.routes import home_bp
from flask_healthz import healthz

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()

app = Flask(__name__)
app.logger.setLevel(LOGLEVEL)
app.config["HEALTHZ"] = {
    "live": lambda: None,
    "ready": lambda: None,
}
app.register_blueprint(healthz, url_prefix="/healthz")
app.register_blueprint(home_bp)

error = None
try:
    config.load_config()
except Exception as e:
    error = e
    app.logger.error(f'CONFIG: {e}')

if __name__ == 'main':
    app.run()

from flask import Flask
import os
from kubernetes import config
from kubelinks_app.home.routes import home_bp

app = Flask(__name__)
app.register_blueprint(home_bp)
LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
app.logger.setLevel(LOGLEVEL)

error = None

try:
    config.load_config()
except Exception as e:
    error = e
    app.logger.error(f'CONFIG: {e}')

if __name__ == 'main':
    app.run()

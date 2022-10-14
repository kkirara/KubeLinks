from flask import Flask


def create_app(config_filename=None):
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)

    from .home import routes
    app.register_blueprint(routes.home_bp)

    return app

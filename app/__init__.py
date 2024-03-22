from flask import Flask


def create_app(config_filename='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    
    from .views import bp
    app.register_blueprint(bp)
    
    return app
    
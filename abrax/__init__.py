from flask import Flask, render_template
from abrax.main.controller import main

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(main)

    return app
import os 
from flask import Flask, jsonify


# FLUTTERWAVE SANDBOX API URL: https://ravesandboxapi.flutterwave.com

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    #Register Payment Blueprint
    from . import payments
    app.register_blueprint(payments.payments_blueprint)


    @app.route('/')
    def index():
        return jsonify(status="OK")

    return app
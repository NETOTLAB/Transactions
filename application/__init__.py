import os 
import logging
from flask import Flask, jsonify

# FLUTTERWAVE SANDBOX API URL: https://ravesandboxapi.flutterwave.com

def create_app(test_config=None):

    #Configure Logging before creating the appp instance
    logging.basicConfig(
        filename='application.log',
        format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        level=logging.DEBUG
    )

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    #Register Payment Blueprint
    from . import payments
    app.register_blueprint(payments.payments_blueprint)


    @app.route('/')
    def index():
        app.logger.debug("Hello i'm able to log")
        return jsonify(status="OK")

    return app
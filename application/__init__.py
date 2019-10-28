import os 
import logging
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import config

db = SQLAlchemy()
migrate = Migrate()
# FLUTTERWAVE SANDBOX API URL: https://ravesandboxapi.flutterwave.com

def create_app(test_config=None):

    #Configure Logging before creating the appp instance
    logging.basicConfig(
        filename='logs/application.log',
        format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        level=logging.DEBUG
    )

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.DevConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    

    #Register Payment Blueprint
    from . import payments
    app.register_blueprint(payments.payments_blueprint)


    @app.route('/')
    def index():
        app.logger.debug("Hello i'm able to log")
        return jsonify(status="OK")

    return app
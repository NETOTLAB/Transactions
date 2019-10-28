import os
from flask import Blueprint, request, jsonify, Response
from flask.json import loads
from flask import current_app
from .utils.validations import *
from .utils.mobilemoney import send_to_flutterwave


payments_blueprint =  Blueprint('payments', __name__)


@payments_blueprint.route('/depositwithmobilemoney', methods=['POST'])
def deposit_with_mobile_money():
    data = request.get_json()
    
    #Validate the Data
    validate =  validate_all_required_data(data)
    if validate is not True:
        return jsonify(status='error', message=validate[1])

    #Request mobile payment to Flutterwave
    result = send_to_flutterwave(data)


    return jsonify(result)


@payments_blueprint.route('/flutterwavewebhook', methods=['POST'])
def flutterwavewebhook():
    flutterhook_data =  request.get_json()
    current_app.logger.debug("Received headers")
    current_app.logger.debug(request.headers)
    hash =  request.headers.get['HTTP_VERIF_HASH']
    
    if hash is None:
        current_app.logger.debug("someOne tried to send Flutterwave webhook with no HASH")
        #TO-DO
        #Log everything
        pass
    if hash != os.getenv("FLUTTERWAVE_WEBHOOK_HASH"):
        current_app.logger.debug("someOne tried to send Flutterwave webhook  with fake HASH")
        #TO-DO
        #Log everything
        pass
    if hash == os.getenv("FLUTTERWAVE_WEBHOOK_HASH"):
        #TO-DO
        #Query Db and confirm the data
        return Response(status=200)

@payments_blueprint.route('/test', methods=['POST', 'GET'])
def test():
    current_app.logger.debug("I'm logging into The blueprint")
    print("Runnning")
    return Response(status=200)

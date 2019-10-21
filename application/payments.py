from flask import Blueprint, request, jsonify
from flask.json import loads
from .utils.validations import *
from .utils.mobilemoney import send_to_flutterwave


payments_blueprint =  Blueprint('payments', __name__)


@payments_blueprint.route('/paywithmobilemoney', methods=['POST'])
def pay_with_mobile_money():
    data = request.get_json()
    
    #Validate the Data
    validate =  validate_all_required_data(data)
    if validate is not True:
        return jsonify(status='error', message=validate[1])

    #Request mobile payment to Flutterwave
    result = send_to_flutterwave(data)


    return jsonify(result)



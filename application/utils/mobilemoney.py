import requests
import os
import uuid
import time

def send_to_flutterwave(data):
    
    #Prepare full required data
    PBFPubKey = os.getenv('FLUTTERWAVE_PUBKEY')
    currency = "RWF"
    payment_type = "mobilemoneygh"
    country = "NG"
    network = "RWF"
    txRef = "MC-" + str(uuid.uuid4())

    epoch_time = int(time.time())
    orderRef = "MC_" + str(epoch_time) + str(data['phonenumber'])
    
    is_mobile_money_gh = 1

    data['PBFPubKey'] = PBFPubKey
    data['currency'] = currency
    data['payment_type'] = payment_type
    data['country'] = country
    data['network'] = network
    data['txRef'] = txRef
    data['orderRef'] = orderRef
    data['is_mobile_money_gh'] = 1

    print(data)
    return data
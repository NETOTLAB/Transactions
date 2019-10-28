import requests
import os
import uuid
import time
import base64
import json
import hashlib
from Crypto.Cipher import DES3


"""this is the getKey function that generates an encryption Key for you by passing your Secret Key as a parameter."""
def getKey():
    seckey = os.getenv("FLUTTERWAVE_SECKEY")
    #seckey = "FLWSECK-6b32914d4d60c10d0ef72bdad734134a-X"
    hashedseckey = hashlib.md5(seckey.encode("utf-8")).hexdigest()
    hashedseckeylast12 = hashedseckey[-12:]
    seckeyadjusted = seckey.replace('FLWSECK-', '')
    seckeyadjustedfirst12 = seckeyadjusted[:12]
    return seckeyadjustedfirst12 + hashedseckeylast12

"""This is the encryption function that encrypts your payload by passing the text and your encryption Key."""
def encryptData(key, plainText):
    blockSize = 8
    padDiff = blockSize - (len(plainText) % blockSize)
    cipher = DES3.new(key, DES3.MODE_ECB)
    plainText = "{}{}".format(plainText, "".join(chr(padDiff) * padDiff))
    encrypted = base64.b64encode(cipher.encrypt(plainText.encode("utf8")))
    return encrypted



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

    
    
    #ENCRYPT DATA
    hashed_sec_key = getKey()
    encrypted_data = encryptData(hashed_sec_key, json.dumps(data))

    payload = {
        "PBFPubKey": PBFPubKey,
        "client": encrypted_data.decode("utf-8"),
        "alg": "3DES-24"
    }
    endpoint = "https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/charge"
    
    print("############# THIS ONE")
    print(json.dumps(payload))
    print("#######################")
    response =  requests.post(endpoint, headers={'content-type': 'application/json',}, data=json.dumps(payload))
    print(response.json())

    return json.dumps(payload)
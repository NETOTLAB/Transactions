def validate_amount_to_pay(price):
    if price < 5000:
        return False
    return True

def validate_all_required_data(data):
    error = ""
    if 'amount' not in data.keys():
        error = "No 'amount' to pay in the Data you send"
        return (False, error)

    if not validate_amount_to_pay(data['amount']):
        error = "Amount to pay too low"
        return (False, error)

    if 'phonenumber' not in data.keys():
        error = "No Phonenumber to debit from customer"
        return (False, error)

    if 'email' not in data.keys():
        error = "No email to debit from customer"
        return (False, error)

    if 'id' not in data.keys():
        error = "No ID to debit from customer"
        return (False, error)

    return True
from . import db 


class Wallet(db.Model):
    """ Model for every client and how much he/she hold in his/her deposit"""
    user_id = db.Column(db.Integer, unique=True)
    balance = db.column(db.Integer, nullable=False)

    def __repr__(self):
        return "<user {}>".format(self.user_id)



class DepositTransaction(db.Model):
    """ model for all Deposit transactions """
    
    __tablename__ =  'deposittransaction'
    
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    amount = db.Column(db.Integer, nullable=False)
    payment_type = db.Column(db.String(15), nullable=False)
    email =  db.Column(db.String(20), nullable=True)
    txRef =  db.Column(db.String(), primary_key=True, nullable=False)
    orderRef = db.Column(db.String(), nullable=False)
    verified  = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return "<txRef {}>".format(self.txRef) 

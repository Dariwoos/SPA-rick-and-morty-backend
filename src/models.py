from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80), unique=False, nullable=False)
    bank_account = db.Column(db.String(120), unique=False, nullable=True)
    loan = db.Column(db.String(80), unique=False, nullable=False)
    dues = db.Column(db.String(80), unique=False, nullable=False)
    payments = db.Column(db.String(80), unique=False, nullable=False)
    balance = db.Column(db.Integer, unique=False, nullable=False)


    def __init__(self,name,bank_account,loan,dues,payments,balance):
        self.name = name
        self.bank_account = bank_account
        self.loan = loan
        self.dues = dues
        self.payments = payments
        self.balance = balance


    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "bank_account": self.bank_account,
            "loan":self.loan,
            "dues":self.dues,
            "payments":self.payments,
            "balance":self.balance
            # do not serialize the password, its a security breach
        }
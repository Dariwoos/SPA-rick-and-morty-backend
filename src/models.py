from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_account = db.Column(db.String(120), unique=False, nullable=False)
    loan = db.Column(db.String(80), unique=False, nullable=False)
    dues = db.Column(db.String(80), unique=False, nullable=False)
    payments = db.Column(db.String(80), unique=False, nullable=False)
    balance = db.Column(db.String(80), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "bank_account": self.email,
            "loan":self.loan,
            "dues":self.dues,
            "payments":self.payments,
            "balance":self.balance
            # do not serialize the password, its a security breach
        }
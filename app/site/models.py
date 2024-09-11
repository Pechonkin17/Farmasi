from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    @staticmethod
    def phone_exists(phone):
        return db.session.query(db.exists().where(Contact.phone == phone)).scalar()
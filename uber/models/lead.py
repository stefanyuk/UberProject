from uber import db


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone_number = db.Column(db.String)
    email = db.Column(db.String)

    @classmethod
    def create(cls, data):
        lead = cls(**data)
        db.session.add(lead)
        db.session.commit()

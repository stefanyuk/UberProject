from uber import db


class Lead(db.Model):
    """Model to save Lead information to the database"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone_number = db.Column(db.String)
    email = db.Column(db.String)

    @classmethod
    def create(cls, data):
        """Creates new lead record in the db"""
        lead = cls(**data)
        db.session.add(lead)
        db.session.commit()

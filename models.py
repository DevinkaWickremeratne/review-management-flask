from app import db

class Conference(db.Model):
    __tablename__ = 'conferences'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    speakers = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255), nullable=False)
    overall_rating = db.Column(db.Float, nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'location': self.location,
            'speakers': self.speakers,
            'website': self.website,
            'overall_rating': self.overall_rating
        }
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'))
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'conference_id': self.conference_id,
            'description': self.description,
            'rating': self.rating
        }

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

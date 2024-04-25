import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

class Conference(db.Model):
    __tablename__ = 'conferences'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    speakers = db.Column(db.JSON, nullable=False)
    website = db.Column(db.String(255), nullable=False)
    overall_rating = db.Column(db.Numeric(3,1), nullable=False)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'))
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Numeric(3,1), nullable=False)

@app.route('/conferences', methods=['GET'])
def get_conferences():
    conferences = Conference.query.all()
    conference_list = []
    for conference in conferences:
        conference_data = {
            'id': conference.id,
            'name': conference.name,
            'description': conference.description,
            'startDate': str(conference.start_date),
            'endDate': str(conference.end_date),
            'location': conference.location,
            'speakers': conference.speakers,
            'website': conference.website,
            'rating': float(conference.overall_rating)
        }
        conference_list.append(conference_data)
    return jsonify(conference_list)

@app.route('/conference/<int:conference_id>', methods=['GET'])
def get_conference(conference_id):
    conference = Conference.query.get(conference_id)
    if conference:
        return jsonify({
            'id': conference.id,
            'name': conference.name,
            'description': conference.description,
            'startDate': str(conference.start_date),
            'endDate': str(conference.end_date),
            'location': conference.location,
            'speakers': conference.speakers,
            'website': conference.website,
            'rating': str(conference.overall_rating)  
        })
    else:
        return jsonify({'message': 'Conference not found'}), 404
    
@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    review_list = []
    for review in reviews:
        review_data = {
            'id': review.id,
            'user_id': review.user_id,
            'conference_id': review.conference_id,
            'description': review.description,
            'rating': float(review.rating)
        }
        review_list.append(review_data)
    return jsonify(review_list)

@app.route('/conferences/<int:conference_id>/reviews', methods=['GET'])
def get_reviews_for_conference(conference_id):
    reviews = Review.query.filter_by(conference_id=conference_id).all()
    if not reviews:
        return jsonify({'message': 'No reviews found for the conference with ID {}'.format(conference_id)}), 404

    review_list = []
    for review in reviews:
        review_data = {
            'id': review.id,
            'user_id': review.user_id,
            'conference_id': review.conference_id,
            'description': review.description,
            'rating': float(review.rating)
        }
        review_list.append(review_data)
    
    return jsonify(review_list)


if __name__ == '__main__':
    app.run(debug=True)

import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Conference as ConferenceModel,Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

db = SQLAlchemy(app)

@app.route('/conferences', methods=['GET'])
def get_conferences():
    conferences = ConferenceModel.query.all()
    return jsonify([conference.serialize() for conference in conferences])

@app.route('/conferences/<int:conference_id>', methods=['GET'])
def get_conference(conference_id):
    conference = ConferenceModel.query.get(conference_id)
    if not conference:
            return jsonify({'message': 'Conference not found'}), 404
    return jsonify(conference.serialize())

@app.route('/conferences/<int:conference_id>/reviews', methods=['GET'])
def get_reviews_for_conference(conference_id):
    reviews = Review.query.filter_by(conference_id=conference_id).all()
    return jsonify([review.serialize() for review in reviews])

if __name__ == '__main__':
    app.run()

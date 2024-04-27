import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restx import Api, Resource, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
db = SQLAlchemy(app)
CORS(app)

api = Api(app, version='1.0', title='Conference API', description='API for managing conferences and reviews')

# Models
user_model = api.model('User', {
    'id': fields.Integer(required=True, description='The user ID'),
    'username': fields.String(required=True, description='The username'),
    'email': fields.String(required=True, description='The email')
})

conference_model = api.model('Conference', {
    'id': fields.Integer(required=True, description='The conference ID'),
    'name': fields.String(required=True, description='The conference name'),
    'description': fields.String(required=True, description='The conference description'),
    'start_date': fields.Date(required=True, description='The conference start date'),
    'end_date': fields.Date(required=True, description='The conference end date'),
    'location': fields.String(required=True, description='The conference location'),
    'speakers': fields.List(fields.String, required=True, description='List of speakers'),
    'website': fields.String(required=True, description='The conference website'),
    'overall_rating': fields.Float(required=True, description='The conference overall rating')
})

review_model = api.model('Review', {
    'id': fields.Integer(required=True, description='The review ID'),
    'user_id': fields.Integer(required=True, description='The user ID'),
    'conference_id': fields.Integer(required=True, description='The conference ID'),
    'description': fields.String(required=True, description='The review description'),
    'rating': fields.Float(required=True, description='The review rating')
})

# Routes
@api.route('/conferences')
class ConferenceList(Resource):
    @api.doc('list_conferences')
    @api.marshal_with(conference_model)
    def get(self):
        """List all conferences"""
        conferences = Conference.query.all()
        return conferences

@api.route('/conference/<int:conference_id>')
class Conference(Resource):
    @api.doc('get_conference')
    @api.marshal_with(conference_model)
    def get(self, conference_id):
        """Get a conference by ID"""
        conference = Conference.query.get(conference_id)
        if not conference:
            api.abort(404, "Conference {} not found".format(conference_id))
        return conference

@api.route('/reviews')
class ReviewList(Resource):
    @api.doc('list_reviews')
    @api.marshal_list_with(review_model)
    def get(self):
        """List all reviews"""
        reviews = Review.query.all()
        return reviews

@api.route('/conferences/<int:conference_id>/reviews')
class ConferenceReviews(Resource):
    @api.doc('get_reviews_for_conference')
    @api.marshal_list_with(review_model)
    def get(self, conference_id):
        """List reviews for a specific conference"""
        reviews = Review.query.filter_by(conference_id=conference_id).all()
        if not reviews:
            api.abort(404, "No reviews found for conference {}".format(conference_id))
        return reviews

if __name__ == '__main__':
    app.run(debug=True)
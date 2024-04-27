from flask import jsonify
from flask_restx import Resource
from app import api, db
from models import Conference as ConferenceModel,Review

@api.route('/conferences')
class ConferenceList(Resource):
    @api.doc('list_conferences')
    def get(self):
        """List all conferences"""
        conferences = ConferenceModel.query.all()
        return jsonify([conference.serialize() for conference in conferences])

@api.route('/conference/<int:conference_id>')
class Conference(Resource):
    @api.doc('get_conference')
    def get(self, conference_id):
        """Get a conference by ID"""
        conference = ConferenceModel.query.get(conference_id)
        if not conference:
            return jsonify({'message': 'Conference not found'}), 404
        return jsonify(conference.serialize())
    
@api.route('/reviews')
class ReviewList(Resource):
    @api.doc('list_reviews')
    def get(self):
        """List all reviews"""
        reviews = Review.query.all()
        return jsonify([review.serialize() for review in reviews])

@api.route('/conferences/<int:conference_id>/reviews')
class ConferenceReviews(Resource):
    @api.doc('get_reviews_for_conference')
    def get(self, conference_id):
        """List reviews for a specific conference"""
        reviews = Review.query.filter_by(conference_id=conference_id).all()
        return jsonify([review.serialize() for review in reviews])
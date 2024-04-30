# Review Management Flask

This application provides a RESTful API to manage Conferences and their Reviews. The API is built with Python using Flask and SQLAlchemy.

## Endpoints

**GET /conferences**

This endpoint returns a list of all conferences.

**GET /conferences/{conference_id}**

This endpoint returns a specific conference by its ID.

**GET /conferences/{conference_id}/reviews**

This endpoint returns all reviews for a specific conference by the conference's ID.


# Review Management Flask

This application provides a simple RESTful API to manage Conferences and their Reviews. The API is built with Python using Flask and SQLAlchemy.

## Endpoints

### GET /conferences

This endpoint returns a list of all conferences.

**Example Request:**

```sh
GET /conferences
```

**Example Response:**

```json
[
    {
        "id": 1,
        "name": "Conference 1",
        "description": "This is a description of Conference 1",
        // other fields...
    },
    // other conferences...
]
```

**GET /conferences/{conference_id}**

This endpoint returns a specific conference by its ID.

**Example Request:**

```sh
GET /conferences/1
```

**Example Response:**

```json
{
    "id": 1,
    "name": "Conference 1",
    "description": "This is a description of Conference 1",
    // other fields...
}
```

If the conference with the given ID does not exist, it returns a 404 error with a message.

**Example Error Response:**

```json
{
    "message": "Conference not found"
}
```

**GET /conferences/{conference_id}/reviews**

This endpoint returns all reviews for a specific conference by the conference's ID.

**Example Request:**

```sh
GET /conferences/1/reviews
```

**Example Response:**

```json
[
    {
        "id": 1,
        "rating": 5,
        "comment": "Great conference!",
        "conference_id": 1
        // other fields...
    },
    // other reviews...
]
```

Please replace `{conference_id}` with the actual ID of the conference.
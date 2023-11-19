# Rest-API-PO


## Endpoints
    GET /users
        Returns a JSON-encoded list of users with a status code of 200.
    GET /users/<id>
        Returns a JSON-encoded user with the specified ID and a status code of 200.
    POST /users
        Accepts a request with a JSON body containing "name" and "lastname" fields, saves the user in temporary persistence, assigns a unique ID, and returns a status code of 201.
    PATCH /users/<id>
        Accepts a request with a JSON body containing "name" or "lastname" fields, modifies the user with the specified ID, and returns a status code of 204. Returns 400 for invalid requests.
    PUT /users/<id>
        Accepts a request with a JSON body containing "name" and "lastname" fields, either creates a new user or modifies an existing user with the specified ID, and returns a status code of 204.
    DELETE /users/<id>
        Deletes the user with the specified ID from temporary persistence and returns a status code of 204. Returns 400 if the user does not exist.

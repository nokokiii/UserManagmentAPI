# Api Endpoints

This is a list of all available endpoints.

## /users

### Method: `GET`

Return list of all users

Response:

- Status codes:

  - `200 OK` - when everything is ok

- Body:

  ```json
  [
      {"name": "Jeo", "lastname": "Doe", "rowid": 1},
      ...
  ]
  ```

### Method: `POST`

Create a new user

Request:

- Status codes:

  - `201 Created` - when creating a new user
  - `400 Bad Request` - when json body is invalid

- Body:

  ```json
  {
      "name": "Jeo", 
      "lastname": "Doe"
  }
  ```

## /users/{user_id}

### Method: `GET`

Return details of a specific user

Response:

- Status codes:

  - `200 OK` - when user exists
  - `404 Not Found` - when user does not exist

- Body:

  ```json
  {
      "name": "Jeo", 
      "lastname": "Doe"
  }
  ```

### Method: `PATCH`

Update details of an existing user

Request:

- Status codes:

  - `204 No Content` - when updating an existing user
  - `400 Bad Request` - when json body is invalid
  - `404 Not Found` - when user does not exist

### Method: `PUT`

Update an existing user or create a new one with a specific id

Request:

- Status codes:

  - `201 Created` - when creating a new user
  - `204 No Content` - when updating an existing user
  - `400 Bad Request` - when json body is invalid

### Method: `DELETE`

Delete an existing user

Request:

- Status codes:

  - `204 No Content` - when deleting an existing user
  - `404 Not Found` - when user does not exist

## /generate_users

### Method: `POST`

Generate example users. This endpoint is only for testing purposes.

Request:

- Status codes:

  - `201 Created` - when creating a new user

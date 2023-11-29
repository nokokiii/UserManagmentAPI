## Api Endpoints

### /users
- Method: `GET`
- Description: Return list of all users
- Response:
    - Status code: 200 OK
    - Body:
    ```json
    [
        {"name": "Jeo", "lastname": "Doe", "rowid": 1},
        ...
    ]
    ```

### /users/{user_id}
- Method: `GET`
- Description: Return details of a specific user
- Response:
    - Status code: 200 OK
    - Body:
    ```json
    {
        "name": "Jeo", 
        "lastname": "Doe"
    }
    ```

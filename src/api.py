from flask import Flask, jsonify, request

import src.api_functions as af
from src.db import create_db

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'}), 404


@app.route('/users', methods=['GET'])
def get_all_users():
    if all_users := af.get_all_users():
        return jsonify(all_users), 200
    return jsonify({'error': 'Intenal Error', 'message': 'There was promlem while connecting to database'}), 500


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user := af.get_user(user_id):
        return jsonify(user), 200
    return jsonify({'error': 'Not Found', 'message': 'The requested user does not exist.'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if 'name' in data and 'last_name' in data:
        if is_created := af.create_user(data['name'], data['last_name']):
            return jsonify(is_created), 201
        return jsonify({'error': 'Intenal Error', 'message': 'There was promlem while creating to database'}), 500
    return jsonify({'error': 'Bad Request','message': 'Missing values to create user'}), 400


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # TODO: Implement
    return jsonify(), 501


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # TODO: Implement
    return jsonify(), 501


create_db("users.db", example_users=True)
app.run(debug=True, port=5000, host='localhost')

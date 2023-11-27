from flask import Flask, jsonify, request

import src.api_functions as af
from src.db import create_db

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': 'The requested endpoint does not exist.'}), 404


@app.route('/users', methods=['GET'])
def get_all_users():
    if all_users := af.get_all_users():
        return jsonify(all_users), 200
    return jsonify({'error': 'Intenal error', 'message': 'There was promlem while connecting to database'}), 500


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user := af.get_user(user_id):
        return jsonify(user), 200
    return jsonify({'error': 'Not found', 'message': 'The requested user does not exist.'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    # TODO: Implement
    return jsonify(), 501


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

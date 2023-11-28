from flask import Flask, jsonify, request
from flask_cors import CORS

import src.api_functions as af
from src.db import create_db

app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'}), 404


@app.route('/users', methods=['GET'])
def get_all_users():
    response, status_code = af.get_all_users()
    return jsonify(response), status_code


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    response, status_code = af.get_user(user_id)
    return jsonify(response), status_code

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    response, status_code = af.create_user(data)
    return jsonify(response), status_code


@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.get_json()
    response, status_code = af.edit_user(user_id, data)
    return jsonify(response), status_code


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_add_user(user_id):
    data = request.get_json()
    response, status_code = af.edit_add_user(user_id, data)
    return jsonify(response), status_code


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    response, status_code = af.delete_user(user_id)
    return jsonify(response), status_code


app.run(debug=True, port=5000, host='localhost')

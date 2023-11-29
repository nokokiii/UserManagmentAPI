"""
This is the main file for the API. It contains all the routes and the main function to run the API.
"""

import logging
import os

from flask import Flask, jsonify, request

import api_functions as af
from db import add_example_users

app = Flask(__name__)

logging.basicConfig(filename='src/logs/api.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

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


@app.route('/generate_users', methods=['GET'])
def generate_users():
    add_example_users()
    return jsonify({"message": "Users generated successfully"}), 201
    

if __name__ == "__main__":
    app.run(port=5000, host='localhost')

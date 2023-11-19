from flask import Flask, jsonify

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': 'The requested endpoint does not exist.'}), 404


@app.route('/users', methods=['GET'])
def get_all_users():
    # TODO: Implement
    return jsonify()


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # TODO: Implement
    return jsonify()


@app.route('/users', methods=['POST'])
def create_user():
    # TODO: Implement
    return jsonify()


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # TODO: Implement
    return jsonify()


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # TODO: Implement
    return jsonify()


if __name__ == '__main__':
    app.run(debug=True)
    
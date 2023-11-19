from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_all_users():
    # TODO: Implement
    return jsonify()

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
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
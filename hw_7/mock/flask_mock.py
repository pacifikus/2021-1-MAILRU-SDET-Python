import threading

from flask import Flask, jsonify, request

from settings import DATA, MOCK_HOST, MOCK_PORT

app = Flask(__name__)


@app.route('/users/<name>', methods=['GET'])
def get_user_surname(name):
    if data := DATA.get(name):
        return {"surname": data['surname']}, 200
    else:
        return jsonify(f'Surname for user {name} not fount'), 404


@app.route('/users/<name>', methods=['PUT'])
def update_user_surname(name):
    if data := DATA.get(name):
        request_data = request.json
        data['surname'] = request_data['surname']
        data['age'] = request_data['age']
        DATA[name] = data
        return jsonify(data), 200
    else:
        return jsonify(f'User {name} not fount'), 404


@app.route('/users/<name>', methods=['DELETE'])
def delete_task(name):
    if DATA.get(name):
        del DATA[name]
        return jsonify({'deleted': True}), 200
    else:
        return jsonify(f'User {name} not fount'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': MOCK_HOST,
        'port': MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify('Exiting'), 200

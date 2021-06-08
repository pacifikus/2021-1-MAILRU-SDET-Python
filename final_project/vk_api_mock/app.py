import threading

from flask import Flask, jsonify, request

app = Flask(__name__)

DATA = {
    'qweqwe': 0
}

MOCK_HOST = '0.0.0.0'
MOCK_PORT = 5000


@app.route('/vk_id/<username>', methods=['GET'])
def get_user_vk_id(username):
    if username in DATA:
        return {"vk_id": DATA[username]}, 200
    else:
        return jsonify(DATA), 404


@app.route('/add_user/<username>', methods=['GET'])
def add_user(username):
    if username not in DATA:
        DATA[username] = len(DATA)
    return {username: DATA[username]}, 200


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

import json

import settings
from app.app import run_app
from client import Client


def test_mock_down():
    host, port = settings.APP_HOST, settings.APP_PORT
    run_app()

    client = Client(host=host, port=port)
    response = client.request('/users/Ivan', 'GET')

    client.request('/shutdown', 'GET')

    assert response['status_code'] == 500
    assert response['body'] == \
           '<p>The server encountered an internal error and was unable to' \
           ' complete your request. Either the server is overloaded or' \
           ' there is an error in the application.</p>'


def test_get_user(socket_client):
    response = socket_client.request('/users/Ivan', 'GET')
    body = json.loads(response['body'])

    assert response['status_code'] == 200
    assert body['surname'] == 'Ivanov'


def test_get_non_existent_user(socket_client):
    response = socket_client.request('/users/Anton', 'GET')

    assert response['status_code'] == 404


def test_update_user(socket_client):
    data = {
        'surname': 'Ivanov',
        'age': 45
    }
    headers = {'Content-Type': 'application/json'}
    response = socket_client.request(
        '/users/Ivan',
        'PUT',
        headers=headers,
        data=data
    )
    body = json.loads(response['body'])

    assert response['status_code'] == 200
    assert body['age'] == 45


def test_delete_user(socket_client):
    response_delete = socket_client.request('/users/Ivan', 'DELETE')
    body_delete = json.loads(response_delete['body'])

    response_get = socket_client.request('/users/Ivan', 'GET')
    body_get = json.loads(response_get['body'])

    assert response_delete['status_code'] == 200
    assert body_delete['deleted']
    assert body_get == 'User name Ivan not found'


def test_delete_non_existent_user(socket_client):
    response_delete = socket_client.request('/users/Ivan1', 'DELETE')

    assert response_delete['status_code'] == 404

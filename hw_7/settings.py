APP_HOST = '127.0.0.1'
APP_PORT = 8080

SOCKET_HOST = '127.0.0.1'
SOCKET_PORT = '8082'

MOCK_HOST = '127.0.0.1'
MOCK_PORT = 8083

APP_URL = f'http://{APP_HOST}:{APP_PORT}'
APP_SHUTDOWN_URL = f'http://{APP_HOST}:{APP_PORT}/shutdown'

DATA = {
    'Ivan': {
        'surname': 'Ivanov',
        'age': 11,
        'user_id': 1
    },
    'Petr': {
        'surname': 'Petrov',
        'age': 22,
        'user_id': 2
    },
    'Alex': {
        'surname': 'Semenov',
        'age': 33,
        'user_id': 2
    },
}

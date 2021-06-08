import json
import socket
from test_settings import ADMIN_USER, ADMIN_PASSWORD


class SocketClient:

    def __init__(self, host, port, login_mode=True):
        self.host = host
        self.port = port
        self.user = ADMIN_USER
        self.password = ADMIN_PASSWORD
        self.cookies = None
        self.headers = {"Host": f'http://{host}:{str(port)}'}
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36' \
                          ' (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)

        if login_mode:
            self.login_mode = True
            self.login()
        self.login_mode = False

    def login(self):
        url = f'/login'
        data = {
            'username': self.user,
            'password': self.password,
            'submit': 'Login'
        }
        self.headers['Content-Type'] = 'application/json'
        response = self.request(url, 'POST', self.headers, data)
        self.cookies = response['cookies']
        headers = {
            'Cookie': self.cookies
        }
        self.headers.update(headers)
        return response

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def get(self):
        total_data = []

        while True:
            data = self.client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                self.client.close()
                break

        total_data = ''.join(total_data).splitlines()
        result = {
            'status_code': int(total_data[0].split(" ")[1]),
            'body': total_data[-1],
            'cookies': ''
        }
        if self.login_mode:
            result['cookies'] = total_data[5].split(" ")[1]
        return result

    def request(self, url, method, headers={}, data=None):
        self.connect()
        request = f'{method} {url} HTTP/1.1\r\n'
        data = json.dumps(data)
        self.headers["Content-Length"] = len(data.encode('utf-8'))
        self.headers.update(headers)
        request += '\r\n'.join(f'{key}: {value}'
                               for key, value in self.headers.items())
        request += '\r\n\r\n'
        if data:
            request += data

        self.connect()
        self.client.send(request.encode())
        return self.get()
